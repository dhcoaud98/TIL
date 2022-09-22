package com.ssafy.prosn.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
/**
 * created by seongmin on 2022/07/27
 * updated by seongmin on 2022/08/11
 */
@Getter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class TokenDto {
    private String grantType;
    private String accessToken;
    private Long tokenExpiresIn;
    private String refreshToken;
    private Long refreshTokenExpiresIn;
    private Long id;
    private String name;

    public void setIdAndName(Long id, String name) {
        this.id = id;
        this.name = name;
    }
}
