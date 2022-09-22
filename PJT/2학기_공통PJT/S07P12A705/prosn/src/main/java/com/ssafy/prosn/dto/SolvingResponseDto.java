package com.ssafy.prosn.dto;

import com.ssafy.prosn.domain.post.PostTag;
import com.ssafy.prosn.domain.post.Tag;
import com.ssafy.prosn.domain.profile.status.Solving;
import com.ssafy.prosn.domain.user.LocalUser;
import com.ssafy.prosn.domain.user.User;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.util.ArrayList;
import java.util.List;

/**
 * created by yura on 2022/08/01
 * updated by seongmin on 2022/08/11
 */
@AllArgsConstructor
@NoArgsConstructor
@Getter
public class SolvingResponseDto {
    private List<Content> content = new ArrayList<>();
    private int totalPages;
    private Long totalElements;

    public void addSolving(List<Solving> solvingList, int totalPages, Long totalElements) {
        for (Solving solving : solvingList) {
            List<PostTag> postTags = solving.getProblem().getPostTags();
            List<String> tags = new ArrayList<>();
            for (PostTag postTag : postTags) {
                tags.add(postTag.getTag().getCode());
            }
            this.content.add(new Content(solving.getProblem().getId(), tags, solving.getProblem().getTitle(), solving.isRight()));
            this.totalPages = totalPages;
            this.totalElements = totalElements;
        }
    }

    private static class Content {
        private Long postId;
        private List<String> tags;
        private String title;
        private boolean isRight;

        public Content(Long postId, List<String> tags, String title, boolean isRight) {
            this.postId = postId;
            this.tags = tags;
            this.title = title;
            this.isRight = isRight;
        }

        public Content() {
        }

        public Long getPostId() {
            return postId;
        }

        public void setPostId(Long postId) {
            this.postId = postId;
        }

        public List<String> getTags() {
            return tags;
        }

        public void setTags(List<String> tags) {
            this.tags = tags;
        }

        public String getTitle() {
            return title;
        }

        public void setTitle(String title) {
            this.title = title;
        }

        public boolean isRight() {
            return isRight;
        }

        public void setRight(boolean right) {
            isRight = right;
        }
    }
}
