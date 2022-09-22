package com.ssafy.prosn.controller;

import com.ssafy.prosn.domain.profile.scrap.Scrap;
import com.ssafy.prosn.dto.UserResponseDto;
import com.ssafy.prosn.service.PostListService;
import com.ssafy.prosn.service.ScrapService;
import com.ssafy.prosn.service.UserService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;
import java.util.Map;

import static org.springframework.http.HttpStatus.*;

/**
 * created by seongmin on 2022/08/05
 * updated by seongmin on 2022/08/08
 */
@RestController
@RequiredArgsConstructor
@Slf4j
@RequestMapping("/api/scrap")
public class ScrapController {

    private final UserService userService;
    private final ScrapService scrapService;
    private final PostListService postListService;

    @PostMapping("/folder")
    public ResponseEntity<?> makeFolder(@RequestBody Map<String, String> req) {
        UserResponseDto userInfo = userService.getMyInfoBySecret();
        postListService.make(userInfo.getId(), req.get("title"));
        return ResponseEntity.status(CREATED).build();
    }

    @DeleteMapping("/folder/{id}")
    public ResponseEntity<?> deleteFolder(@PathVariable(value = "id") Long id) {
        UserResponseDto userInfo = userService.getMyInfoBySecret();
        postListService.delete(userInfo.getId(), id);
        return ResponseEntity.status(OK).build();
    }

    @GetMapping("/folder")
    public ResponseEntity<?> getFolderList() {
        UserResponseDto userInfo = userService.getMyInfoBySecret();
        return ResponseEntity.status(OK).body(postListService.getPostListFolder(userInfo.getId()));
    }

    @PostMapping
    public ResponseEntity<?> scraps(@RequestBody Map<String,String> req) {
        log.info("pid = {}", req.get("pid"));
        UserResponseDto userInfo = userService.getMyInfoBySecret();
        scrapService.save(Long.parseLong(req.get("pid")), Long.parseLong(req.get("lid")), userInfo.getId());
        return ResponseEntity.status(CREATED).build();
    }

    @GetMapping("/{id}") // folder(postList) id
    public ResponseEntity<?> getScrapList(@PathVariable(value = "id") Long id, Pageable pageable) {
        return ResponseEntity.status(OK).body(scrapService.getScrapList(id, pageable));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<?> deleteScrap(@PathVariable(value = "id") Long id) {
        UserResponseDto userInfo = userService.getMyInfoBySecret();
        scrapService.delete(userInfo.getId(), id);
        return ResponseEntity.status(OK).build();
    }

//    private static class ScrapRequest {
//        @NotNull(message = "스크랩 하려는 게시글은 필수 값입니다.")
//        Long pid;
//        @NotNull(message = "스크랩 하려는 폴더는 필수 값입니다.")
//        Long lid;
//
//        public ScrapRequest(Long pid, Long lid) {
//            this.pid = pid;
//            this.lid = lid;
//        }
//
//        public ScrapRequest() {
//        }
//
//        @Override
//        public String toString() {
//            return "ScrapRequest{" +
//                    "pid=" + pid +
//                    ", lid=" + lid +
//                    '}';
//        }
//    }


}
