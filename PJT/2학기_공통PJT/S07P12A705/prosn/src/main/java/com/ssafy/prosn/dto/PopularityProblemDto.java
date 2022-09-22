package com.ssafy.prosn.dto;

import lombok.*;

/**
 * created by seongmin on 2022/08/10
 */
@AllArgsConstructor
@NoArgsConstructor
@Getter
@Builder
@ToString
public class PopularityProblemDto {
    private Long id;
    private String title;
    private Long numOfLikes;
    private Integer views;
    private Long submissionNum;

    public static PopularityProblemDto of(Long id, String title, Long numOfLikes, Integer views, Long submissionNum) {
        return new PopularityProblemDto(id, title, numOfLikes, views, submissionNum);
    }
}
