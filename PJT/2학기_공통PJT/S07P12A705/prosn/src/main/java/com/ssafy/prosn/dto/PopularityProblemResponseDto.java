package com.ssafy.prosn.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

/**
 * created by seongmin on 2022/08/10
 */
@AllArgsConstructor
@NoArgsConstructor
@Getter
public class PopularityProblemResponseDto {
    private PopularityProblemDto popularityProblem;
    private RateDto rateDto;
}
