package com.ssafy.prosn.domain.post;

import com.ssafy.prosn.converter.BooleanToYNConverter;
import com.ssafy.prosn.domain.BaseEntity;
import com.ssafy.prosn.domain.comment.Comment;
import com.ssafy.prosn.domain.profile.status.Solving;
import com.ssafy.prosn.domain.user.User;
import lombok.*;
import org.hibernate.annotations.ColumnDefault;
import org.hibernate.annotations.DynamicInsert;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

/**
 * created by seongmin on 2022/07/19
 * updated by seongmin on 2022/08/15
 */
@Entity
@Inheritance(strategy = InheritanceType.JOINED)
@DiscriminatorColumn(name = "ptype")
@DynamicInsert
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Getter
public abstract class Post extends BaseEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String title;

    @Column(columnDefinition = "TEXT")
    private String mainText;

    @ColumnDefault("0")
    private Integer views;

//    @Version
//    private Long version;

    @ManyToOne
    @JoinColumn(name = "user_id")
    private User user;

    @OneToMany(mappedBy = "post")
    private List<LikeDislike> likeDislikes = new ArrayList<>();

    @OneToMany(mappedBy = "problem")
    private List<Solving> solvingList = new ArrayList<>();

    @OneToMany(mappedBy = "post", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<PostTag> postTags = new ArrayList<>();

    @OneToMany(mappedBy = "post", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    private List<Comment> comments = new ArrayList<>();

    @Convert(converter = BooleanToYNConverter.class)
    private boolean isDeleted;

    @ColumnDefault("0")
    private Long numOfLikes;
    @ColumnDefault("0")
    private Long numOfDislikes;

    @Column(insertable = false, updatable = false)
    @Enumerated(EnumType.STRING)
    private PostType ptype;

    public Post(String title, User user) {
        this.title = title;
        this.user = user;
    }

    public Post(String title, String mainText, User user) {
        this.title = title;
        this.mainText = mainText;
        this.user = user;
    }

    public void remove() {
        isDeleted = true;
    }

    public void renameTitle(String title) {
        this.title = title;
    }

    public void increaseLikeDislike(boolean type) {
        if (type) {
            this.numOfLikes++;
        } else {
            this.numOfDislikes++;
        }
    }

    public void decreaseLikeDislike(boolean type) {
        if (type) {
            this.numOfLikes--;
        } else {
            this.numOfDislikes--;
        }
    }

    public void addPostTag(PostTag postTag) {
        postTags.add(postTag);
        if (postTag.getPost() != this) {
            postTag.setPost(this);
        }
    }
}
