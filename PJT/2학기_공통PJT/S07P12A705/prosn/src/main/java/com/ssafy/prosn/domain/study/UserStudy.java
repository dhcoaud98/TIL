package com.ssafy.prosn.domain.study;

import com.ssafy.prosn.domain.BaseEntity;
import com.ssafy.prosn.domain.user.User;
import lombok.*;

import javax.persistence.*;

/**
 * created by yeomyeong on 2022/07/25
 * updated by yeomyeong on 2022/08/08
 */

@Entity
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class UserStudy extends BaseEntity{

    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "study_group_id")
    private StudyGroup studyGroup;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id")
    private User user;

    @Builder
    public UserStudy(User user, StudyGroup studyGroup) {
        this.user = user;
        this.studyGroup = studyGroup;
    }
}
