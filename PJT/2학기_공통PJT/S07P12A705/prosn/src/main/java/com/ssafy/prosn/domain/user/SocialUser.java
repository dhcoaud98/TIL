package com.ssafy.prosn.domain.user;

import com.ssafy.prosn.oauth.Platform;
import lombok.*;

import javax.persistence.Entity;

/**
 * created by seongmin on 2022/07/19
 */
@Entity
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Getter
public class SocialUser extends User {

    private String oauthId;
    private Platform platform;

    @Builder
    public SocialUser(String name, String email, String oauthId, Platform platform) {
        super(name, email);
        this.oauthId = oauthId;
        this.platform = platform;
    }
}
