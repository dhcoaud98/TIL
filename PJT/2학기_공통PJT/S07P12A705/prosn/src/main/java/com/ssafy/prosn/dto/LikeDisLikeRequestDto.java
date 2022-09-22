package com.ssafy.prosn.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.validation.constraints.NotNull;

/**
 * created by seongmin on 2022/07/28
 * updated by seongmin on 2022/08/09
 */
@AllArgsConstructor
@NoArgsConstructor
@Getter
@Builder
public class LikeDisLikeRequestDto {
    @NotNull(message = "게시글은 필수 입력 값입니다.")
    private Long pid;
    @NotNull(message = "좋아요 싫어요 타입은 필수 입력 값입니다.")
    private boolean type;
}
