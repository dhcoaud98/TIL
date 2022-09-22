package com.ssafy.prosn.dto;


import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

/**
 * created by seongmin on 2022/08/10
 */
@Getter
@AllArgsConstructor
@NoArgsConstructor
public class RateDto {
    private double correctRate;
    private int submitCount;
}
