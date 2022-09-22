package com.ssafy.prosn.dto;

import com.ssafy.prosn.domain.profile.scrap.Scrap;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.util.ArrayList;
import java.util.List;

@Getter
@AllArgsConstructor
@NoArgsConstructor
public class ScrapResponseDto {
    private List<Content> content = new ArrayList<>();
    private int totalPages;
    private Long totalElements;

    public static ScrapResponseDto of(List<Scrap> scraps, int totalPages, Long totalElements) {
        ScrapResponseDto result = new ScrapResponseDto();
        for (Scrap scrap : scraps) {
            result.content.add(new Content(scrap.getId(), scrap.getPost().getTitle()));
        }
        result.totalPages = totalPages;
        result.totalElements = totalElements;
        return result;
    }

    private static class Content {
        private Long pid;
        private String title;

        public Content(Long pid, String title) {
            this.pid = pid;
            this.title = title;
        }

        public Content() {
        }

        public Long getPid() {
            return pid;
        }

        public void setPid(Long pid) {
            this.pid = pid;
        }

        public String getTitle() {
            return title;
        }

        public void setTitle(String title) {
            this.title = title;
        }
    }
}
