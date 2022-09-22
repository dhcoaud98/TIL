package com.ssafy.prosn.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.RequiredArgsConstructor;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;

/**
 * created by seongmin on 2022/07/28
 * updated by seongmin on 2022/08/01
 */
@Getter
@RequiredArgsConstructor
@Builder
@AllArgsConstructor
public class ReplyRequestDto {
//    @NotNull(message = "사용자는 필수 입력값입니다.")
//    private Long uid;
    @NotNull(message = "댓글은 필수 입력값입니다.")
    private Long cid;
    @NotBlank(message = "답글은 필수 입력값입니다.")
    private String mainText;
}
