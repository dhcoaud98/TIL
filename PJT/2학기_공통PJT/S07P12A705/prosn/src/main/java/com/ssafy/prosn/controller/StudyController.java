package com.ssafy.prosn.controller;

import com.ssafy.prosn.domain.study.StudyGroup;

import com.ssafy.prosn.dto.*;
import com.ssafy.prosn.repository.study.StudyGroupRepository;
import com.ssafy.prosn.repository.study.UserStudyRepository;
import com.ssafy.prosn.service.StudyService;
import com.ssafy.prosn.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.web.PageableDefault;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.Map;

import static org.springframework.http.HttpStatus.*;


/**
 * created by yeomyeong on 2022/08/01
 * updated by yeomyeong on 2022/08/08
 */

@RestController
@RequiredArgsConstructor
@RequestMapping("/api/study")
public class StudyController {

    private final UserService userService;
    private final StudyService studyService;
    private final StudyGroupRepository studyGroupRepository;
    private final UserStudyRepository userStudyRepository;

    //스터디 그룹
    //생성
    @PostMapping
    public ResponseEntity<?> createStudy(@RequestBody @Valid StudyGroupRequestDto dto) {
        UserResponseDto user = userService.getMyInfoBySecret();
        return ResponseEntity.status(OK).body(studyService.create(dto, user.getId()));
    }

    //목록 조회
    @GetMapping
    public ResponseEntity<?> studyGroupList(@PageableDefault(size = 5) Pageable pageable) {
        Page<StudyGroupListResponseDto> page = studyGroupRepository.showStudyGroupList(pageable);
        return ResponseEntity.status(OK).body(page);
    }

    //상세내용
    @GetMapping("/{studyid}")
    public ResponseEntity<?> showStudy(@PathVariable(value = "studyid") Long studyid) {
        UserResponseDto user = userService.getMyInfoBySecret();
        return ResponseEntity.status(OK).body(studyService.showStudyGroup(user.getId(), studyid));
    }

    //수정
    @PutMapping
    public ResponseEntity<?> updateStudy(@RequestBody @Valid StudyGroupRequestDto dto) {
        StudyGroup studyGroup = studyGroupRepository.findById(dto.getId()).orElseThrow(() -> new IllegalStateException("존재하지 않는 스터디입니다"));
        if (!studyGroup.getUser().getId().equals(userService.getMyInfoBySecret().getId())) {
            throw new IllegalStateException("스터디를 수정할 권한이 없습니다.");
        }
        return ResponseEntity.status(OK).body(studyService.update(studyGroup.getId(), dto));
    }

    //삭제
    @DeleteMapping("/{studyid}")
    public ResponseEntity<?> deleteStudy(@PathVariable(value = "studyid") Long studyid) {
        StudyGroup studyGroup = studyGroupRepository.findById(studyid).orElseThrow(() -> new IllegalStateException("존재하지 않는 스터디입니다"));
        if (!studyGroup.getUser().getId().equals(userService.getMyInfoBySecret().getId())) {
            throw new IllegalStateException("스터디를 삭제할 권한이 없습니다.");
        }
        studyService.deleteStudy(studyGroup);
        return ResponseEntity.status(OK).build();
    }

    //내스터디
    //목록 조회
    @GetMapping("/me")
    public ResponseEntity<?> myStudyGroupList(@PageableDefault(size = 5) Pageable pageable) {
        UserResponseDto user = userService.getMyInfoBySecret();
        return ResponseEntity.status(OK).body(userStudyRepository.findByUserId(user.getId(), pageable));
    }

    //가입
    @PostMapping("/me/{studyid}")
    public ResponseEntity<?> joinStudy(@PathVariable(value = "studyid") Long studyid) {
        UserResponseDto user = userService.getMyInfoBySecret();
        StudyGroup studyGroup = studyGroupRepository.findById(studyid).orElseThrow(() -> new IllegalStateException("존재하지 않는 스터디입니다"));
        studyService.joinStudy(user.getId(), studyGroup);
        return ResponseEntity.status(CREATED).build();
    }

    //탈퇴
    @DeleteMapping("/me/{studyid}")
    public ResponseEntity<?> removeStudy(@PathVariable(value = "studyid") Long studyid) {
        UserResponseDto user = userService.getMyInfoBySecret();
        StudyGroup studyGroup = studyGroupRepository.findById(studyid).orElseThrow(() -> new IllegalStateException("존재하지 않는 스터디입니다"));
        studyService.removeStudy(user.getId(), studyGroup);
        return ResponseEntity.status(OK).build();
    }
}
