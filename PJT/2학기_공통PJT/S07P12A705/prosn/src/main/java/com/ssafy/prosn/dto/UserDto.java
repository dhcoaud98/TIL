package com.ssafy.prosn.dto;

import com.ssafy.prosn.domain.user.User;
import lombok.*;

import java.util.ArrayList;
import java.util.List;

/**
 * created by seongmin on 2022/08/08
 */
@AllArgsConstructor
@NoArgsConstructor
@Getter
@ToString
public class UserDto {
    private List<Content> content = new ArrayList<>();
    private int totalPages;
    private Long totalElements;

    public void addUser(List<User> users, int totalPages, Long totalElements) {
        for (User user : users) {
            this.content.add(new Content(user.getId(), user.getName(), user.getPoint()));
        }
        this.totalPages = totalPages;
        this.totalElements = totalElements;
    }

    private static class Content {
        private Long id;
        private String name;
        private Integer point;

        public Content() {
        }

        public Content(Long id, String name, Integer point) {
            this.id = id;
            this.name = name;
            this.point = point;
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

        public Integer getPoint() {
            return point;
        }

        public void setPoint(Integer point) {
            this.point = point;
        }
    }
}
