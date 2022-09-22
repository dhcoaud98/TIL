package com.ssafy.prosn.controller;

import com.ssafy.prosn.domain.post.Post;
import com.ssafy.prosn.domain.post.PostType;
import com.ssafy.prosn.dto.*;
import com.ssafy.prosn.repository.post.ProblemRepository;
import com.ssafy.prosn.service.PostService;
import com.ssafy.prosn.service.UserService;
import com.ssafy.prosn.service.WorkbookService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpEntity;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.validation.Valid;
import java.util.List;
import java.util.Map;

import static org.springframework.http.HttpStatus.*;

/**
 * created by seongmin on 2022/07/28
 * updated by seongmin on 2022/08/09
 */
@RestController
@RequiredArgsConstructor
@Slf4j
@RequestMapping("/api/post")
public class PostController {
    private final PostService postService;
    private final UserService userService;
    private final WorkbookService workbookService;

    private final ProblemRepository problemRepository;
    @PostMapping("/problem")
    public ResponseEntity<?> writeProblem(@RequestBody @Valid ProblemRequestDto req) {
        Post post = postService.writeProblem(req, userService.getMyInfoBySecret().getId());
        return ResponseEntity.status(CREATED).build();
    }

    @PostMapping("/information")
    public ResponseEntity<?> writeInformation(@RequestBody @Valid InformationRequestDto req) {
        Post post = postService.writeInformation(req, userService.getMyInfoBySecret().getId());
        return ResponseEntity.status(CREATED).build();
    }

    // 페이징 처리 추가하기
    @GetMapping
    public ResponseEntity<?> getAllPost(Pageable pageable) {
        log.info("전체조회");
        PostResponseDto result = postService.showAllPost(pageable);
        return ResponseEntity.status(OK).body(result);
    }

    @GetMapping("/problem")
    public ResponseEntity<?> getAllProblem(Pageable pageable) {
        log.info("문제 전체 조회");
        log.info("페이징 정렬 = {}", pageable.getSort());
        log.info("페이징 = {}", pageable);
        ProblemWorkbookResponseDto problemWorkbookResponseDto = postService.showAllProblem(pageable);
        return ResponseEntity.status(OK).body(problemWorkbookResponseDto);

    }

    @GetMapping("/information")
    public ResponseEntity<?> getAllInformation(Pageable pageable) {
        log.info("정보 전체 조회");
        PostResponseDto result = postService.showAllInformation(pageable);
        return ResponseEntity.status(OK).body(result);
    }

    @GetMapping("/{id}")
    public ResponseEntity<?> getPost(@PathVariable(value = "id") Long id, HttpServletRequest req, HttpServletResponse res) {
        log.info("조회 id = {}", id);
        Cookie oldCookie = null;
        Cookie[] cookies = req.getCookies();
        if (cookies != null) {
            for (Cookie cookie : cookies) {
                if (cookie.getName().equals("postView")) {
                    oldCookie = cookie;
                }
            }
        }
        PostDetailResponseDto postDetailResponseDto = postService.showProblemDetail(id);
        if (oldCookie != null) {
            log.info("oldCookie.getValue() = {}", oldCookie.getValue());
            if (!oldCookie.getValue().contains("[" + id.toString() + "]")) {
                postService.updateViews(id);
                oldCookie.setValue(oldCookie.getValue() + "_[" + id + "]");
                oldCookie.setPath("/");
                oldCookie.setMaxAge(60 * 60 * 24);
                res.addCookie(oldCookie);
                postDetailResponseDto.setCookie(oldCookie);
            }
        } else {
            postService.updateViews(id);
            Cookie newCookie = new Cookie("postView", "[" + id + "]");
            newCookie.setPath("/");
            newCookie.setMaxAge(60 * 60 * 24);
            res.addCookie(newCookie);
            postDetailResponseDto.setCookie(newCookie);
        }

        return ResponseEntity.ok(postDetailResponseDto);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<?> deletePost(@PathVariable(value = "id") Long id) {
        log.info("삭제 id = {}", id);
        postService.delete(id, userService.getMyInfoBySecret().getId());
        return ResponseEntity.status(NO_CONTENT).build();
    }

    @PostMapping("/click")
    public ResponseEntity<?> likeDisLikeClick(@RequestBody @Valid LikeDisLikeRequestDto req) {
        log.info("좋아요 싫어요 req = {}", req);
        LikeDisLikeNumDto result = postService.likeDislikeClick(req, userService.getMyInfoBySecret().getId());
        return ResponseEntity.status(OK).body(result);
    }

    @GetMapping("/search")
    public ResponseEntity<?> search(@RequestParam String title, @RequestParam String code, @RequestParam PostType dtype, Pageable pageable) {
        log.info("title = {}", title);
        log.info("code = {}", code);
        return ResponseEntity.status(OK).body(postService.search(pageable, title, code, dtype));
    }

    @PostMapping("/workbook")
    public ResponseEntity<?> writeWorkbook(@RequestBody Map<String, String> req) {
        workbookService.save(Long.parseLong(req.get("pid")),
                userService.getMyInfoBySecret().getId(),
                req.get("title"));
        return ResponseEntity.status(CREATED).build();
    }

    @PatchMapping("/workbook")
    public ResponseEntity<?> updateWorkbook(@RequestBody Map<String, String> req) {
        workbookService.update(userService.getMyInfoBySecret().getId(),
                Long.parseLong(req.get("wid")),
                req.get("title"));
        return ResponseEntity.status(CREATED).build();
    }

    @GetMapping("/workbook")
    public ResponseEntity<?> getAllWorkbook(Pageable pageable) {
        log.info("문제집 조회");
        PostResponseDto result = workbookService.showAllWorkbook(pageable);
        return ResponseEntity.status(OK).body(result);
    }

    @GetMapping("/problem/ranking")
    public ResponseEntity<?> getPopularProblem() {
        List<PopularityProblemResponseDto> popularityProblemDtos = postService.popularProblem();
        return ResponseEntity.status(OK).body(popularityProblemDtos);
    }
}
