package com.ssafy.prosn.controller;

import com.ssafy.prosn.dto.CommentRequestDto;
import com.ssafy.prosn.service.CommentService;
import com.ssafy.prosn.service.UserService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;

/**
 * created by seongmin on 2022/07/29
 */
@RestController
@RequiredArgsConstructor
@Slf4j
@RequestMapping("/api/comment")
public class CommentController {

    private final CommentService commentService;
    private final UserService userService;

    @PostMapping
    public ResponseEntity<?> write(@RequestBody @Valid CommentRequestDto req) {
        log.info("댓글 작성 req = {}", req);
        commentService.write(req, userService.getMyInfoBySecret().getId());
        return ResponseEntity.status(HttpStatus.CREATED).build();
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<?> delete(@PathVariable(value = "id") Long id) {
        commentService.delete(id, userService.getMyInfoBySecret().getId());
        return ResponseEntity.status(HttpStatus.NO_CONTENT).build();
    }
}
