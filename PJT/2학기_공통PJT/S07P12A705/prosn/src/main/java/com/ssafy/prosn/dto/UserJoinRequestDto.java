package com.ssafy.prosn.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.ToString;

import javax.validation.constraints.Email;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.Pattern;

/**
 * created by seongmin on 2022/07/22
 */
@RequiredArgsConstructor
@Getter
@ToString
public class UserJoinRequestDto {
    @NotBlank(message = "이메일은 필수 입력 값입니다.")
    @Email
    private String email;
    @NotBlank(message = "아이디는 필수 입력 값입니다.")
    private String userId;
    @NotBlank(message = "비밀번호는 필수 입력 값입니다.")
    @Pattern(regexp = "(?=.*[0-9])(?=.*[a-zA-Z])(?=.*\\W)(?=\\S+$).{8,16}", message = "비밀번호는 8~16자 영문 대 소문자, 숫자, 특수문자를 사용하세요.")
    private String password;
    @NotBlank(message = "이름은 필수 입력 값입니다.")
    private String name;

    @Builder
    public UserJoinRequestDto(String email, String userId, String password, String name) {
        this.email = email;
        this.userId = userId;
        this.password = password;
        this.name = name;
    }
}
