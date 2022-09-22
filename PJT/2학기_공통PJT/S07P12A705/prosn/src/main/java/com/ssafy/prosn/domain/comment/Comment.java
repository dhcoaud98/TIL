package com.ssafy.prosn.domain.comment;

import com.ssafy.prosn.domain.BaseEntity;
import com.ssafy.prosn.domain.post.Post;
import com.ssafy.prosn.domain.user.User;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

/**
 * created by seongmin on 2022/07/19
 * updated by seongmin on 2022/07/20
 */
@Entity
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Getter
public class Comment extends BaseEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String mainText;

    @ManyToOne
    @JoinColumn(name = "user_id")
    private User user;

    @ManyToOne
    @JoinColumn(name = "post_id")
    private Post post;

    @OneToMany(mappedBy = "comment")
    private List<Reply> replies = new ArrayList<>();


    @Builder
    public Comment(String mainText, User user, Post post) {
        this.mainText = mainText;
        this.user = user;
        this.post = post;
    }
}
