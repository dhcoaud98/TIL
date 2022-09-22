package com.ssafy.prosn.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.validation.constraints.*;
import java.time.LocalDate;
import java.util.List;

/**
 * created by yeomyeong on 2022/07/26
 * updated by yeomyeong on 2022/08/07
 */
@Getter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class StudyGroupRequestDto {
    private Long id;
    @NotBlank(message = "제목은 필수 입력 값입니다.")
    private String title;
    @Min(1)
    @NotNull(message = "최대인원수는 필수 입력 값입니다.")
    private int maxPerson;
    private LocalDate expiredDate;
    @NotBlank(message = "장소는 필수 입력 값입니다.")
    private String place;
    @NotBlank(message = "설명은 필수 입력 값입니다.")
    private String mainText;
    @NotBlank(message = "세부내용은 필수 입력 값입니다.")
    private String secretText;
    @NotNull(message = "태그는 1개 이상 선택해야 합니다.")
    private List<String> tags;

}
