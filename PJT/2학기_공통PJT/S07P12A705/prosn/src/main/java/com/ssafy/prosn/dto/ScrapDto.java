package com.ssafy.prosn.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.RequiredArgsConstructor;

/**
 * created by seongmin on 2022/08/04
 */

@Getter
@RequiredArgsConstructor
@AllArgsConstructor
public class ScrapDto {
    private Long pid;
    private String title;
}
