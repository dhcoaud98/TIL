package com.ssafy.prosn.dto;

import com.ssafy.prosn.domain.post.Tag;
import lombok.*;

import javax.validation.constraints.Min;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

/**
 * created by yeomyeong on 2022/07/28
 * updated by seongmin on 2022/08/11
 */
@Getter
@ToString(callSuper = true)
@NoArgsConstructor
@AllArgsConstructor
public class UserStudyResponseDto extends StudyResponseDto {
    //title, currentMem, totalMem, place, members, mainText, secretText
    private List<Member> members = new ArrayList<>();
    private String secretText;

    @Builder
    public UserStudyResponseDto(Long id, String title, int currentPerson, int maxPerson, String place, String mainText, List<Tag> tags, Long mId, String mName, String secretText, boolean secret) {
        super(id, title, currentPerson, maxPerson, place, mainText, tags, secret, mId, mName);
        this.secretText = secretText;
    }

    public void addMember(Long id, String name) {
        this.members.add(new Member(id, name));
    }

    private static class Member {
        private Long id;
        private String name;

        public Member(Long id, String name) {
            this.id = id;
            this.name = name;
        }

        public Member() {
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
