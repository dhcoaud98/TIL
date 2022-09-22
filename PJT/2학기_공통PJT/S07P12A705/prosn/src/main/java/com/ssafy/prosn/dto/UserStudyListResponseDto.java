package com.ssafy.prosn.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.ToString;

/**
 * created by yeomyeong on 2022/07/28
 * updated by yeomyeong on 2022/08/05
 */
@Getter
public class UserStudyListResponseDto {
    private Long id;
    private String title;
    private String mainText;

    @Builder
    public UserStudyListResponseDto(Long id, String title, String mainText) {
        this.id = id;
        this.title = title;
        if (mainText.length() > 20)
            this.mainText = mainText.substring(0, 20);
        else
            this.mainText = mainText;
    }
}
