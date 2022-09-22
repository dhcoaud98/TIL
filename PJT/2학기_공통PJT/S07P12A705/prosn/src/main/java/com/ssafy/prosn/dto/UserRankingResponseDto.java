package com.ssafy.prosn.dto;

import com.ssafy.prosn.domain.user.User;
import lombok.*;

/**
 * created by seongmin on 2022/08/08
 */
@Getter
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class UserRankingResponseDto {
    private Long id;
    private String name;
    private Integer point;

    public static UserRankingResponseDto of(User user) {
        return UserRankingResponseDto.builder()
                .id(user.getId())
                .name(user.getName())
                .point(user.getPoint())
                .build();
    }
}
