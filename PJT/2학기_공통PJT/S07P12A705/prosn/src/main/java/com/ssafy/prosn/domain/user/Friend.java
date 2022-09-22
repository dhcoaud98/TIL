package com.ssafy.prosn.domain.user;

import com.ssafy.prosn.domain.BaseEntity;
import lombok.*;

import javax.persistence.*;

/**
 * created by seongmin on 2022/08/08
 */
@Entity
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Getter
public class Friend extends BaseEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "follower_id")
    private User follower;

    @ManyToOne
    @JoinColumn(name = "following_id")
    private User following;

    @Builder
    public Friend(User follower, User following) {
        this.follower = follower;
        this.following = following;
    }
}
