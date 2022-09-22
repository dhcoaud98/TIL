package com.ssafy.prosn.dto;

import com.ssafy.prosn.domain.post.PostType;
import com.ssafy.prosn.domain.post.ProblemWorkbook;
import lombok.*;

import java.util.ArrayList;
import java.util.List;

/**
 * created by seongmin on 2022/08/17
 */
@Getter
public class WorkbookDetailResponseDto extends PostDetailResponseDto {

    private List<ProblemInfo> problemInfos = new ArrayList<>();

    @Builder
    public WorkbookDetailResponseDto(Long id, String title, Long numOfLikes, Long numOfDislikes, List<CommentDto> comments, Integer views, UserResponseDto user, List<String> tags, List<ProblemWorkbook> problemWorkbook, PostType type) {
        super(id, title, numOfLikes, numOfDislikes, comments, views, user, tags, type);
        for (ProblemWorkbook workbook : problemWorkbook) {
            this.problemInfos.add(new ProblemInfo(workbook.getProblem().getId(), workbook.getProblem().getTitle()));
        }
    }

    @Getter
    @Setter
    @AllArgsConstructor
    private static class ProblemInfo {
        private Long id;
        private String title;

    }
}
