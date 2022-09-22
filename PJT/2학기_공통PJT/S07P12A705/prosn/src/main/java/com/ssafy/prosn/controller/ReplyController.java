package com.ssafy.prosn.controller;

import com.ssafy.prosn.dto.CommentRequestDto;
import com.ssafy.prosn.dto.ReplyRequestDto;
import com.ssafy.prosn.dto.UserResponseDto;
import com.ssafy.prosn.service.ReplyService;
import com.ssafy.prosn.service.UserService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpEntity;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;

/**
 * created by seongmin on 2022/08/01
 */
@RestController
@RequiredArgsConstructor
@Slf4j
@RequestMapping("/api/reply")
public class ReplyController {

    private final ReplyService replyService;
    private final UserService userService;

    @PostMapping
    public ResponseEntity<?> write(@RequestBody @Valid ReplyRequestDto req) {
        log.info("답글 작성 req = {}", req);
        UserResponseDto user = userService.getMyInfoBySecret();
        return ResponseEntity.ok(replyService.write(req, user.getId()));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<?> delete(@PathVariable(value = "id") Long id) {
        UserResponseDto user = userService.getMyInfoBySecret();
        replyService.delete(id, user.getId());
        return ResponseEntity.ok(HttpEntity.EMPTY);
    }
}
