package com.ssafy.prosn.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

/**
 * created by seongmin on 2022/07/27
 * updated by seongmin on 2022/08/11
 */

@AllArgsConstructor
@NoArgsConstructor
@Builder
@Getter
public class TokenRequestDto {
    private String accessToken;
    private String refreshToken;
}
