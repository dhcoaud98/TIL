package com.ssafy.prosn.dto;

import lombok.*;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;
import java.util.List;

/**
 * created by seongmin on 2022/07/25
 * updated by seongmin on 2022/08/05
 */
@Getter
@ToString
@AllArgsConstructor
@NoArgsConstructor
public class ProblemRequestDto extends PostRequestDto {
    private String ex1;
    private String ex2;
    private String ex3;
    private String ex4;
    @NotBlank(message = "답은 필수 입력 값입니다.")
    private String answer;
    private String mainText;

    @Builder
    public ProblemRequestDto(String title, List<String> tags, String ex1, String ex2, String ex3, String ex4, String answer, String mainText) {
        super(title, tags);
        this.ex1 = ex1;
        this.ex2 = ex2;
        this.ex3 = ex3;
        this.ex4 = ex4;
        this.answer = answer;
        this.mainText = mainText;
    }
}
