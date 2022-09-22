package com.ssafy.prosn.controller;

import com.ssafy.prosn.domain.profile.note.WrongAnswer;
import com.ssafy.prosn.dto.*;
import com.ssafy.prosn.service.UserService;
import com.ssafy.prosn.service.WrongAnswerService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

import static org.springframework.http.HttpStatus.*;

/**
 * created by seongmin on 2022/08/01
 * updated by seongmin on 2022/08/11
 */
@RestController
@RequiredArgsConstructor
@Slf4j
@RequestMapping("/api/wrongAnswer")
public class WrongAnswerController {

    private final WrongAnswerService wrongAnswerService;
    private final UserService userService;

    // 틀린 문제는 바로 오답노트에 저장하도록 수정
//    @PostMapping
//    public ResponseEntity<?> save(@RequestBody @Valid WrongAnswerRequestDto req) {
//        WrongAnswer result = wrongAnswerService.save(req, userService.getMyInfoBySecret().getId());
//        log.info("result = {}", result);
//        return ResponseEntity.status(CREATED).build();
//    }

    @PatchMapping
    public ResponseEntity<?> write(@RequestBody @Valid WrongNoteRequestDto req) {
        wrongAnswerService.write(req, userService.getMyInfoBySecret().getId());
        return ResponseEntity.status(CREATED).build();
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<?> delete(@PathVariable(value = "id") Long id) {
        wrongAnswerService.delete(id, userService.getMyInfoBySecret().getId());
        return ResponseEntity.status(OK).build();
    }

    // 오답노트 전체 조회
    @GetMapping("/all")
    public ResponseEntity<?> getNote(Pageable pageable, @RequestParam boolean isWrite) {
        NoteResponseDto result = wrongAnswerService.getNote(userService.getMyInfoBySecret().getId(), pageable, isWrite);
        return ResponseEntity.status(OK).body(result);
    }

    @GetMapping("/tag")
    public ResponseEntity<?> getNoteByTag(Pageable pageable, @RequestParam boolean isWrite, @RequestParam String tag) {
        NoteResponseDto result = wrongAnswerService.getNoteByTag(userService.getMyInfoBySecret().getId(), pageable, isWrite, tag);
        return ResponseEntity.status(OK).body(result);
    }

    @GetMapping("/{id}")
    public ResponseEntity<?> getNoteDetail(@PathVariable(value = "id") Long id) {
        WrongAnswerNoteDetailResponseDto result = wrongAnswerService.getNoteDetail(id, userService.getMyInfoBySecret().getId());
        log.info("result = {}", result);
        return ResponseEntity.status(OK).body(result);
    }

}
