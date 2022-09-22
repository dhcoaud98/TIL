package com.ssafy.prosn.domain.user;

import lombok.*;

import javax.persistence.Entity;

/**
 * created by seongmin on 2022/07/19
 * updated by yeomyeong on 2022/08/07 (updatePassword)
 */
@Entity
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Getter
public class LocalUser extends User {

    private String userId;
    private String password;

    @Builder
    public LocalUser(String name, String email, String userId, String password) {
        super(name, email);
        this.userId = userId;
        this.password = password;
    }

    public LocalUser updatePassword(String password) {
        this.password = password;
        return this;
    }
}
