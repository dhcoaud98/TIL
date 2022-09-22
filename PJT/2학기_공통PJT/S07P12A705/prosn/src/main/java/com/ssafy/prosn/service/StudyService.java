package com.ssafy.prosn.service;

import com.ssafy.prosn.domain.study.StudyGroup;

import com.ssafy.prosn.dto.*;
import org.springframework.transaction.annotation.Transactional;

/**
 * created by yeomyeong on 2022/07/25
 * updated by yeomyeong on 2022/08/04
 */
public interface StudyService{

    //스터디 생성
    StudyGroup create(StudyGroupRequestDto studyGroupdDto, Long uid);
    //스터디 내용 수정
    StudyGroup update(Long studyGroupId, StudyGroupRequestDto newData);
    //스터디 내용 조회
    StudyResponseDto showStudyGroup(Long userId, Long studyGroupId);
    //스터디 삭제
    @Transactional
    void deleteStudy(StudyGroup studyGroup);
    //스터디 가입
    Long joinStudy(Long userId, StudyGroup studyGroup);
    //스터디 탈퇴
    void removeStudy(Long userId, StudyGroup studyGroup);
}
