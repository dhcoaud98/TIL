package com.ssafy.prosn.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.ToString;

/**
 * created by yeomyeong on 2022/08/01
 * updated by yeomyeong on 2022/08/02
 */
@Getter
public class StudyGroupListResponseDto {
    private Long id;
    private String title;
    private int currentPerson;
    private int MaxPerson;

    @Builder
    public StudyGroupListResponseDto(Long id, String title, int currentPerson, int maxPerson) {
        this.id = id;
        this.title = title;
        this.currentPerson = currentPerson;
        this.MaxPerson = maxPerson;
    }
}
