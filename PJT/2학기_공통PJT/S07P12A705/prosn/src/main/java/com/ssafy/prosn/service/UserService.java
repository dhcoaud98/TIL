package com.ssafy.prosn.service;

import com.ssafy.prosn.domain.user.LocalUser;
import com.ssafy.prosn.dto.*;
import org.springframework.data.domain.Pageable;

import java.util.List;

/**
 * created by seongmin on 2022/07/22
 * updated by seongmin on 2022/08/11
 */
public interface UserService {
    Long join(UserJoinRequestDto joinRequestDto);
    TokenDto login(UserLoginRequestDto loginRequestDto);
    TokenDto reissue(TokenRequestDto tokenRequestDto);
    void logout(Long id);
    UserResponseDto getMyInfoBySecret();
    LocalUser resetPwd(LocalUser user);
    List<UserRankingResponseDto> ranking();
    void duplicateUserId(String userId);
    UserInfoDto getUserInfo(Long uid);
    PostDto getUserPost(Long uid, Pageable pageable);
}
