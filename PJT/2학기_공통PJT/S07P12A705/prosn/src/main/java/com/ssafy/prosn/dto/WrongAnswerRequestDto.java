package com.ssafy.prosn.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;

/**
 * created by seongmin on 2022/07/29
 */
@AllArgsConstructor
@NoArgsConstructor
@Getter
public class WrongAnswerRequestDto {
    @NotNull(message = "문제는 필수 입력 값입니다.")
    private Long pid;
    @NotBlank(message = "골라서 틀린 값은 필수 입력 값입니다.")
    private String wrongAnswer;
}
