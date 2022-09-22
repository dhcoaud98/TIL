package com.ssafy.prosn.domain.post;

import com.ssafy.prosn.domain.BaseEntity;
import com.ssafy.prosn.domain.user.User;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;

/**
 * created by seongmin on 2022/07/19
 * updated by seongmin on 2022/07/25
 */
@Entity
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Getter
public class LikeDislike extends BaseEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "user_id")
    private User user;

    @ManyToOne
    @JoinColumn(name = "post_id")
    private Post post;

    private boolean type;

    @Builder
    public LikeDislike(User user, Post post, boolean type) {
        this.user = user;
        this.post = post;
        this.type = type;
    }

    public void change() {
        this.type = !this.type;
    }
}
