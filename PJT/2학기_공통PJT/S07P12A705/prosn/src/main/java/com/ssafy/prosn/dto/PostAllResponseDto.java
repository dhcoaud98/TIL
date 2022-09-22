package com.ssafy.prosn.dto;

import lombok.Builder;
import lombok.Getter;

/**
 * created by seongmin on 2022/07/25
 */
@Getter
public class PostAllResponseDto {
    private Long id;
    private UserResponseDto user;
    private String title;
    private Integer views;
    private Long numOfLikes;
    private Long numOfDislikes;

    @Builder
    public PostAllResponseDto(Long id, UserResponseDto user, String title, Integer views, Long numOfLikes, Long numOfDislikes) {
        this.id = id;
        this.user = user;
        this.title = title;
        this.views = views;
        this.numOfLikes = numOfLikes;
        this.numOfDislikes = numOfDislikes;
    }
}
