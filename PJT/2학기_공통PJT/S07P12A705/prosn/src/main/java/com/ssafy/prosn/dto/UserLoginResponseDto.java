package com.ssafy.prosn.dto;

import com.ssafy.prosn.domain.user.LocalUser;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class UserLoginResponseDto {
    private String userId;
    private String name;

    public static UserLoginResponseDto of(LocalUser user) {
        return UserLoginResponseDto.builder()
                .userId(user.getUserId())
                .name(user.getName())
                .build();
    }
}
