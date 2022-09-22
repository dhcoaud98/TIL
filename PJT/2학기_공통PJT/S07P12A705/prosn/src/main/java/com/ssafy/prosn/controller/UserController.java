package com.ssafy.prosn.controller;

import com.ssafy.prosn.domain.user.LocalUser;
import com.ssafy.prosn.dto.*;
import com.ssafy.prosn.repository.user.LocalUserRepository;
import com.ssafy.prosn.repository.user.UserRepository;
import com.ssafy.prosn.security.JwtUtils;
import com.ssafy.prosn.service.FriendService;
import com.ssafy.prosn.service.MailService;
import com.ssafy.prosn.service.UserService;
import io.swagger.models.Response;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;

import java.util.Map;

import static org.springframework.http.HttpStatus.*;

/**
 * created by seongmin on 2022/07/27
 * updated by seongmin on 2022/08/09
 */
@RestController
@RequiredArgsConstructor
@Slf4j
@RequestMapping("/api/user")
public class UserController {

    private final UserService userService;
    private final LocalUserRepository localUserRepository;
    private final FriendService friendService;

    @GetMapping("/me")
    public ResponseEntity<?> getMyInfo() {
        UserResponseDto myInfoBySecurity = userService.getMyInfoBySecret();
        log.info("myInfoBySecurity = {}", myInfoBySecurity);
        return ResponseEntity.ok((myInfoBySecurity));
        // return ResponseEntity.ok(memberService.getMyInfoBySecurity());
    }

    @PostMapping("/join")
    public ResponseEntity<?> join(@RequestBody @Valid UserJoinRequestDto req) {
        userService.join(req);

        return ResponseEntity.ok("회원가입에 성공하였습니다.");
    }

    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestBody @Valid UserLoginRequestDto req) {
        return ResponseEntity.ok(userService.login(req));
    }

    @PostMapping("/resetPwd")
    public ResponseEntity<?> resetPassword(@RequestBody UserResetPasswordRequestDto reqDto) {
        LocalUser resetUser = localUserRepository.findByUserId(reqDto.getUserId())
                .orElseThrow(() -> new IllegalStateException("등록된 회원 정보가 없습니다."));

        if (!reqDto.getEmail().equals(localUserRepository.findEmailByUserId(resetUser.getUserId())))
            throw new IllegalStateException("등록된 회원 정보가 없습니다.");

        userService.resetPwd(resetUser);
        return ResponseEntity.ok("임시 비밀번호 발급 완료. 등록된 메일을 확인해주세요");
    }

    //비번 변경하는 것도 만들어야 할 것 같음

    @GetMapping("/ranking")
    public ResponseEntity<?> getRanking() {
        return ResponseEntity.status(OK).body(userService.ranking());
    }

    @PostMapping("/id/check")
    public ResponseEntity<?> idDuplicateCheck(@RequestBody Map<String, String> req) {
        userService.duplicateUserId(req.get("uid"));
        return ResponseEntity.status(OK).build();
    }

    @GetMapping("/following/{id}")
    public ResponseEntity<?> following(@PathVariable(value = "id") Long id) { // 팔로잉 할 사람의 id
        friendService.following(userService.getMyInfoBySecret().getId(), id);
        return ResponseEntity.status(OK).build();
    }

    @GetMapping("/following")
    public ResponseEntity<?> followingList(Pageable pageable) {
        return ResponseEntity.status(OK).body(friendService.getMyFollowing(userService.getMyInfoBySecret().getId(), pageable));
    }

    @GetMapping("/follower")
    public ResponseEntity<?> followerList(Pageable pageable) {
        return ResponseEntity.status(OK).body(friendService.getMyFollower(userService.getMyInfoBySecret().getId(), pageable));
    }

    @GetMapping("/info/{id}")
    public ResponseEntity<?> getUserInfo(@PathVariable(value = "id") Long id) {
        return ResponseEntity.status(OK).body(userService.getUserInfo(id));
    }

    @GetMapping("/post/{id}")
    public ResponseEntity<?> getUserPost(@PathVariable(value = "id") Long id, Pageable pageable) {
        PostDto userPost = userService.getUserPost(id, pageable);
        log.info("결과 = {}",userPost);
        log.info("결과 = {}",userPost.getContent().get(0));
        return ResponseEntity.status(OK).body(userPost);
    }

    @DeleteMapping("/logout")
    public ResponseEntity<?> logout() {
        userService.logout(userService.getMyInfoBySecret().getId());
        return ResponseEntity.status(OK).build();
    }

    @PostMapping("/reissue")
    public ResponseEntity<?> reissue(@RequestHeader(value = "Access-Token")String accessToken,
                                     @RequestHeader(value="Refresh-Token") String refreshToken) {
        TokenDto reissue = userService.reissue(new TokenRequestDto(accessToken, refreshToken));
        return ResponseEntity.status(OK).body(reissue);
    }
}
