package com.ssafy.prosn.repository.user;

import com.ssafy.prosn.domain.user.LocalUser;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.Optional;

/**
 * created by seongmin on 2022/07/20
 * updated by yeomyeong on 2022/08/07 (line 20~)
 */
public interface LocalUserRepository extends JpaRepository<LocalUser, Long> {
    Optional<LocalUser> findByUserId(String uid);
    boolean existsByEmail(String email);

    boolean existsByUserId(String userId);

    @Query("select email from LocalUser l where l.userId = :uid")
    String findEmailByUserId(@Param("uid") String uid);
}
