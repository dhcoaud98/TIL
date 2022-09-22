package com.ssafy.prosn.dto;

import com.ssafy.prosn.domain.post.Post;
import com.ssafy.prosn.domain.post.PostTag;
import com.ssafy.prosn.domain.post.PostType;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.ToString;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

/**
 * created by seongmin on 2022/08/09
 */

@AllArgsConstructor
@NoArgsConstructor
@Getter
@ToString
public class PostDto {
    private List<Content> content = new ArrayList<>();
    private int totalPages;
    private Long totalElements;

    public static PostDto of(List<Post> posts, int totalPages, Long totalElements) {
        PostDto postDto = new PostDto();
        postDto.totalElements = totalElements;
        postDto.totalPages = totalPages;
        for (Post post : posts) {
            List<String> tags = new ArrayList<>();
            for (PostTag postTag : post.getPostTags()) {
                tags.add(postTag.getTag().getCode());
            }
            postDto.content.add(new Content(
                    post.getId(),
                    post.getTitle(),
                    post.getCreated(),
                    post.getUpdated(),
                    post.getPtype(),
                    tags,
                    post.getNumOfLikes(),
                    post.getNumOfDislikes()
            ));
        }
        return postDto;
    }
    private static class Content {
        private Long id;
        private String title;
        private LocalDateTime created;
        private LocalDateTime updated;
        private PostType ptype;
        private List<String> tags;
        private Long numOfLikes;
        private Long numOfDislikes;

        public Content(Long id, String title, LocalDateTime created, LocalDateTime updated, PostType ptype, List<String> tags, Long numOfLikes, Long numOfDislikes) {
            this.id = id;
            this.title = title;
            this.created = created;
            this.updated = updated;
            this.ptype = ptype;
            this.tags = tags;
            this.numOfLikes = numOfLikes;
            this.numOfDislikes = numOfDislikes;
        }

        public Long getId() {
            return id;
        }

        public void setId(Long id) {
            this.id = id;
        }

        public String getTitle() {
            return title;
        }

        public void setTitle(String title) {
            this.title = title;
        }

        public LocalDateTime getCreated() {
            return created;
        }

        public void setCreated(LocalDateTime created) {
            this.created = created;
        }

        public LocalDateTime getUpdated() {
            return updated;
        }

        public void setUpdated(LocalDateTime updated) {
            this.updated = updated;
        }

        public PostType getPtype() {
            return ptype;
        }

        public void setPtype(PostType ptype) {
            this.ptype = ptype;
        }

        public List<String> getTags() {
            return tags;
        }

        public void setTags(List<String> tags) {
            this.tags = tags;
        }

        public Long getNumOfLikes() {
            return numOfLikes;
        }

        public void setNumOfLikes(Long numOfLikes) {
            this.numOfLikes = numOfLikes;
        }

        public Long getNumOfDislikes() {
            return numOfDislikes;
        }

        public void setNumOfDislikes(Long numOfDislikes) {
            this.numOfDislikes = numOfDislikes;
        }
    }

}
