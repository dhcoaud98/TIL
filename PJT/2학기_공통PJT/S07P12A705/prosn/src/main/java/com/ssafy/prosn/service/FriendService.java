package com.ssafy.prosn.service;

import com.ssafy.prosn.dto.UserDto;
import org.springframework.data.domain.Pageable;

/**
 * created by seongmin on 2022/08/08
 */
public interface FriendService {
    void following(Long uid, Long fid);
    UserDto getMyFollower(Long uid, Pageable pageable);
    UserDto getMyFollowing(Long uid, Pageable pageable);
}
