package com.ssafy.prosn.dto;

import com.ssafy.prosn.domain.post.Tag;
import lombok.*;

import java.util.List;

/**
 * created by yeomyeong on 2022/07/31
 * updated by seongmin on 2022/08/11
 */

@Getter
@AllArgsConstructor
@NoArgsConstructor
public class StudyResponseDto {
    private Long id;
    private String title;
    private int currentPerson;
    private int maxPerson;
    private String place;
    private String mainText;
    private List<Tag> tags;
    private boolean secret;
    private Long masterId;
    private String masterName;
}
