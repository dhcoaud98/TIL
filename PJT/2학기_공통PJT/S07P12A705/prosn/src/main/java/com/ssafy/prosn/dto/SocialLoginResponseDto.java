package com.ssafy.prosn.dto;

import com.ssafy.prosn.oauth.Platform;
import lombok.*;

/**
 * created by yura on 2022/08/08
 */
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class SocialLoginResponseDto {
    private String oauthId;
    private Platform platform;
    private String email;
    private String name;
    private String accessToken;
    private String refreshToken;

}
