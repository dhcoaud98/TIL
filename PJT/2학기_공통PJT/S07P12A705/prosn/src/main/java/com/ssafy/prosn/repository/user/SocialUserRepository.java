package com.ssafy.prosn.repository.user;

import com.ssafy.prosn.domain.user.SocialUser;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface SocialUserRepository extends JpaRepository<SocialUser, Long> {
    Optional<SocialUser> findByOauthId(String oauthId);
}
