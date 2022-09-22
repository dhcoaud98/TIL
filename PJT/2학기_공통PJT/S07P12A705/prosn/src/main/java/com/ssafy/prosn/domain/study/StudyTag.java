package com.ssafy.prosn.domain.study;

import com.ssafy.prosn.domain.post.Tag;
import lombok.AccessLevel;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;

/**
 * created by yeomyeong on 2022/08/07
 */
@Entity
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Getter
public class StudyTag {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "study_group_id")
    private StudyGroup study;

    @ManyToOne
    @JoinColumn(name = "tag")
    private Tag tag;

    public StudyTag(StudyGroup study, Tag tag) {
        this.study = study;
        this.tag = tag;
    }
}
