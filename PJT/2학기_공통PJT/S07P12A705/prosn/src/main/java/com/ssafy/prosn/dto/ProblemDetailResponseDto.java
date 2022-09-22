package com.ssafy.prosn.dto;

import com.ssafy.prosn.domain.comment.Comment;
import com.ssafy.prosn.domain.post.PostType;
import com.ssafy.prosn.domain.post.Tag;
import lombok.Builder;
import lombok.Getter;
import lombok.RequiredArgsConstructor;

import java.util.List;

/**
 * created by seongmin on 2022/07/25
 * updated by seongmin on 2022/08/10
 */
@Getter
@RequiredArgsConstructor
public class ProblemDetailResponseDto extends PostDetailResponseDto {
    private String mainText;
    private String example1;
    private String example2;
    private String example3;
    private String example4;
    private String answer;
    private Double correctRate;
    private Integer submitCnt;


    @Builder
    public ProblemDetailResponseDto(Long id, String title, Long numOfLikes, Long numOfDislikes, List<CommentDto> comments, Integer views, UserResponseDto user, List<String> tags, String mainText, String example1, String example2, String example3, String example4, String answer, PostType type, double correctRate, int submitCnt) {
        super(id, title, numOfLikes, numOfDislikes, comments, views, user, tags, type);
        this.mainText = mainText;
        this.example1 = example1;
        this.example2 = example2;
        this.example3 = example3;
        this.example4 = example4;
        this.answer = answer;
        this.correctRate = correctRate;
        this.submitCnt = submitCnt;
    }
}
