package com.ssafy.prosn.domain.profile.scrap;

import com.ssafy.prosn.domain.BaseEntity;
import com.ssafy.prosn.domain.post.Post;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;

/**
 * created by seongmin on 2022/07/20
 * updated by seongmin on 2022/08/04
 */
// ProblemList와 Post를 연결해주는 엔티티
@Entity
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Getter
public class Scrap extends BaseEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "post_id")
    private Post post;

    @ManyToOne
    @JoinColumn(name = "post_list_id")
    private PostList postList;

    @Builder
    public Scrap(Post post, PostList postList) {
        this.post = post;
        this.postList = postList;
    }
}
