package com.ssafy.prosn.dto;

import com.ssafy.prosn.domain.post.Problem;
import lombok.*;

/**
 * created by seongmin on 2022/07/29
 * updated by seongmin on 2022/08/07
 */
@AllArgsConstructor
@NoArgsConstructor
@Getter
@Builder
@ToString
public class NoteDto {
    private Long id;
    private String title;
    private boolean isWrite;
    private Problem problem;
}
