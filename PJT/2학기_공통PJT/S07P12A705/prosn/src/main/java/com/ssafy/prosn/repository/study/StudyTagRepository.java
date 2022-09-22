package com.ssafy.prosn.repository.study;

import com.ssafy.prosn.domain.study.StudyGroup;
import com.ssafy.prosn.domain.study.StudyTag;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
/**
 * created by yeomyeong on 2022/08/07
 */
public interface StudyTagRepository extends JpaRepository<StudyTag, Long> {
    List<StudyTag> findPostTagByStudy(StudyGroup study);
    void deleteByStudyId(Long studyId);
}
