package com.ssafy.prosn.repository.user;

import com.ssafy.prosn.domain.user.Friend;
import com.ssafy.prosn.domain.user.User;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

/**
 * created by seongmin on 2022/08/08
 * updated by seongmin on 2022/08/11
 */
public interface FriendRepository extends JpaRepository<Friend, Long> {
    Page<Friend> findByFollower(User user, Pageable pageable); // 팔로잉 조회
    Page<Friend> findByFollowing(User user, Pageable pageable); // 팔로워 조회

    long countByFollower(User user);
    long countByFollowing(User user);
    Optional<Friend> findByFollowerAndFollowing(User follower, User following);

}
