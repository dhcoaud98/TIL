package com.ssafy.prosn.dto;

import com.ssafy.prosn.domain.post.Post;
import com.ssafy.prosn.domain.post.Tag;
import lombok.*;

import java.util.List;

/**
 * created by seongmin on 2022/07/29
 * updated by seongmin on 2022/08/01
 */
@AllArgsConstructor
@NoArgsConstructor
@Getter
@ToString
@Builder
public class WrongAnswerNoteDetailResponseDto {
    private Long id;
    private Long pid;
    private String title;
    private List<Tag> tags;
    private String mainText;
    private String example1;
    private String example2;
    private String example3;
    private String example4;
    private String answer;
    private boolean isDeleted;

    private String wrongAnswer;
    private String reason;
    private String studyContent;
    private String memo;
    private boolean isWrite;
}
