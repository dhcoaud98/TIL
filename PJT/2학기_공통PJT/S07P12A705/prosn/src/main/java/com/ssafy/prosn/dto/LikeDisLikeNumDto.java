package com.ssafy.prosn.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

/**
 * created by seongmin on 2022/08/12
 */
@Getter
@AllArgsConstructor
@NoArgsConstructor
public class LikeDisLikeNumDto {
    private Long numOfLikes;
    private Long numOfDislikes;
}
