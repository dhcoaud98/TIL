package com.ssafy.prosn.repository.user;

import com.ssafy.prosn.domain.user.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

/**
 * created by seongmin on 2022/07/20
 * updated by seongmin on 2022/08/08
 */
public interface UserRepository extends JpaRepository<User, Long> {

    // user를 point 내림차순으로 조회
    @Query("SELECT u FROM User u order by point desc")
    List<User> findRanking();
    List<User> findTop5ByOrderByPointDesc();
}
