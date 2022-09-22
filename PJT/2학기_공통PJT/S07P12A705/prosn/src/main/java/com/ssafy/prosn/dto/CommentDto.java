package com.ssafy.prosn.dto;

import com.ssafy.prosn.domain.comment.Comment;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

/**
 * created by seongmin on 2022/08/10
 */
@Getter
@AllArgsConstructor
@NoArgsConstructor
public class CommentDto {
    private Long id;
    private User user;
    private String mainText;
    private LocalDateTime created;

    public static CommentDto of(Comment comment) {
        return new CommentDto(
                comment.getId(),
                new User(comment.getUser().getId(), comment.getUser().getName()),
                comment.getMainText(),
                comment.getCreated()
        );
    }

    private static class User {
        private Long id;
        private String name;

        public User() {
        }

        public User(Long id, String name) {
            this.id = id;
            this.name = name;
        }

        public Long getId() {
            return id;
        }

        public void setId(Long id) {
            this.id = id;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }
    }
}
