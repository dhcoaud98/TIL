package com.ssafy.prosn.dto;

import com.ssafy.prosn.domain.post.Post;
import com.ssafy.prosn.domain.user.User;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.ToString;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

/**
 * created by seongmin on 2022/08/08
 * updated by seongmin on 2022/08/11
 */
@AllArgsConstructor
@NoArgsConstructor
@Getter
@ToString
public class UserInfoDto {
    private Long id;
    private String name;
    private Integer point;
    private Long followerCount;
    private Long followingCount;
    private double correctRate;
    private Long problemSolvingCount;
    private Long writePostCount;

    public static UserInfoDto of(User user, Long followerCount, Long followingCount, double correctRate, Long problemSolvingCount, Long writePostCount) {
        return new UserInfoDto(
                user.getId(),
                user.getName(),
                user.getPoint(),
                followerCount,
                followingCount,
                correctRate,
                problemSolvingCount,
                writePostCount
        );
    }

}
