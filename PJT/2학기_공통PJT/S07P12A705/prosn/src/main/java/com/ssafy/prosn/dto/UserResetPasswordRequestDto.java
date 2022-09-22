package com.ssafy.prosn.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.RequiredArgsConstructor;

import javax.validation.constraints.NotBlank;

/**
 * created by yeomyeong on 2022/08/07
 */

@RequiredArgsConstructor
@Getter
public class UserResetPasswordRequestDto {
    @NotBlank(message = "아이디는 필수 입력 값입니다.")
    private String userId;
    @NotBlank(message = "이메일은 필수 입력 값입니다.")
    private String email;

    @Builder
    public UserResetPasswordRequestDto(String userId, String email) {
        this.userId = userId;
        this.email = email;
    }
}
