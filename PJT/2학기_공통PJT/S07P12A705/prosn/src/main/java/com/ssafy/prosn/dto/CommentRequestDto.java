package com.ssafy.prosn.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.RequiredArgsConstructor;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;

/**
 * created by seongmin on 2022/07/25
 * updated by seongmin on 2022/08/01
 */
@Getter
@RequiredArgsConstructor
public class CommentRequestDto {
//    @NotNull(message = "사용자는 필수 입력값입니다.")
//    private Long uid;
    @NotNull(message = "게시글은 필수 입력값입니다.")
    private Long pid;
    @NotBlank(message = "댓글은 필수 입력값입니다.")
    private String mainText;

    @Builder
    public CommentRequestDto(Long pid, String mainText) {
        this.pid = pid;
        this.mainText = mainText;
    }
}
