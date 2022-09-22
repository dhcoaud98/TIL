package com.ssafy.prosn.dto;

import com.ssafy.prosn.domain.post.*;
import lombok.*;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

/**
 * created by seongmin on 2022/08/07
 * updated by seongmin on 2022/08/15
 */
@AllArgsConstructor
@NoArgsConstructor
@Getter
@ToString
public class PostResponseDto {
    private List<Content> content = new ArrayList<>();
    private int totalPages;
    private Long totalElements;

    public void addPost(List<? extends Post> posts, int totalPages, Long totalElements) {

        for (Post post : posts) {
            List<String> tags = new ArrayList<>();
            for (PostTag postTag : post.getPostTags()) {
                tags.add(postTag.getTag().getCode());
            }

            if (post instanceof Workbook) {
                Workbook workBook = (Workbook) post;

                List<ProblemInfo> problems = new ArrayList<>();
                for (ProblemWorkbook problemWorkbook : workBook.getProblemWorkbooks()) {
                    Problem problem = problemWorkbook.getProblem();
                    problems.add(new ProblemInfo(problem.getId(), problem.getTitle()));
                }
                this.content.add(Content.builder()
                        .id(workBook.getId())
                        .ptype(workBook.getPtype())
                        .writer(new UserResponseDto(workBook.getUser().getId(), workBook.getUser().getName()))
                        .title(workBook.getTitle())
                        .mainText(workBook.getMainText())
                        .views(workBook.getViews())
                        .numOfLikes(workBook.getNumOfLikes())
                        .numOfDislikes(workBook.getNumOfDislikes())
                        .tags(tags)
                        .created(workBook.getCreated())
                        .updated(workBook.getUpdated())
                        .problems(problems).build());
            } else {
                this.content.add(new Content(
                        post.getId(),
                        post.getPtype(),
                        new UserResponseDto(post.getUser().getId(), post.getUser().getName()),
                        post.getTitle(),
                        post.getMainText(),
                        post.getViews(),
                        post.getNumOfLikes(),
                        post.getNumOfDislikes(),
                        tags,
                        post.getCreated(),
                        post.getUpdated()
                ));
            }

        }
        this.totalPages = totalPages;
        this.totalElements = totalElements;
    }

    @Getter
    @Setter
    private static class Content {
        private Long id;
        private PostType ptype;
        private UserResponseDto writer;
        private String title;
        private String mainText;
        private Integer views;
        private Long numOfLikes;
        private Long numOfDislikes;
        private List<String> tags;
        private LocalDateTime created;
        private LocalDateTime updated;
        private List<ProblemInfo> problems;


        @Builder
        public Content(Long id, PostType ptype, UserResponseDto writer, String title, String mainText, Integer views, Long numOfLikes, Long numOfDislikes, List<String> tags, LocalDateTime created, LocalDateTime updated, List<ProblemInfo> problems) {
            ConstructorHelper(id, ptype, writer, title, mainText, views, numOfLikes, numOfDislikes, tags, created, updated);
            this.problems = problems;
        }

        private void ConstructorHelper(Long id, PostType ptype, UserResponseDto writer, String title, String mainText, Integer views, Long numOfLikes, Long numOfDislikes, List<String> tags, LocalDateTime created, LocalDateTime updated) {
            this.id = id;
            this.ptype = ptype;
            this.writer = writer;
            this.title = title;
            this.mainText = mainText;
            this.views = views;
            this.numOfLikes = numOfLikes;
            this.numOfDislikes = numOfDislikes;
            this.tags = tags;
            this.created = created;
            this.updated = updated;
        }

        public Content(Long id, PostType ptype, UserResponseDto writer, String title, String mainText, Integer views, Long numOfLikes, Long numOfDislikes, List<String> tags, LocalDateTime created, LocalDateTime updated) {
            ConstructorHelper(id, ptype, writer, title, mainText, views, numOfLikes, numOfDislikes, tags, created, updated);
        }
    }

    @Getter
    @Setter
    private static class ProblemInfo {
        private Long id;
        private String title;

        public ProblemInfo(Long id, String title) {
            this.id = id;
            this.title = title;
        }

    }
}
