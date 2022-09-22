package com.ssafy.prosn.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.validation.constraints.NotNull;

/**
 * created by seongmin on 2022/07/29
 */
@AllArgsConstructor
@NoArgsConstructor
@Getter
public class WrongNoteRequestDto {
    @NotNull(message = "오답노트 아이디는 필수 입력 값입니다.")
    private Long id;
    private String reason;
    private String studyContent;
    private String memo;
}
