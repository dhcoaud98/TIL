package com.ssafy.prosn.dto;

import com.ssafy.prosn.domain.post.PostTag;
import lombok.*;

import java.util.ArrayList;
import java.util.List;

/**
 * created by seongmin on 2022/08/07
 */
@AllArgsConstructor
@NoArgsConstructor
@Getter
@ToString
public class NoteResponseDto {
    private List<Content> content = new ArrayList<>();
    private int totalPages;
    private Long totalElements;

    public void addNote(List<NoteDto> notes, int totalPages, Long totalElements) {
        for (NoteDto note : notes) {
            List<PostTag> postTags = note.getProblem().getPostTags();
            List<String> tags = new ArrayList<>();
            for (PostTag postTag : postTags) {
                tags.add(postTag.getTag().getCode());
            }
            this.content.add(new Content(note.getId(), note.getTitle(), note.isWrite(), tags));
            this.totalPages = totalPages;
            this.totalElements = totalElements;
        }
    }

    private static class Content {
        private Long id;
        private String title;
        private boolean isWrite;
        private List<String> tags;

        public Content() {
        }

        public Content(Long id, String title, boolean isWrite, List<String> tags) {
            this.id = id;
            this.title = title;
            this.isWrite = isWrite;
            this.tags = tags;
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

        public boolean isWrite() {
            return isWrite;
        }

        public void setWrite(boolean write) {
            isWrite = write;
        }

        public List<String> getTags() {
            return tags;
        }

        public void setTags(List<String> tags) {
            this.tags = tags;
        }
    }
}
