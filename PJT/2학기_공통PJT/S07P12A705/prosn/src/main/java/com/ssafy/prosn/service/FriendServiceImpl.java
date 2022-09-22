package com.ssafy.prosn.service;

import com.ssafy.prosn.domain.user.Friend;
import com.ssafy.prosn.domain.user.User;
import com.ssafy.prosn.dto.UserDto;
import com.ssafy.prosn.exception.BadRequestException;
import com.ssafy.prosn.repository.user.FriendRepository;
import com.ssafy.prosn.repository.user.UserRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

/**
 * created by seongmin on 2022/08/08
 */
@Service
@Transactional(readOnly = true)
@RequiredArgsConstructor
@Slf4j
public class FriendServiceImpl implements FriendService {

    private final UserRepository userRepository;
    private final FriendRepository friendRepository;

    @Override
    @Transactional
    public void following(Long uid, Long fid) {
        User user = userRepository.findById(uid).orElseThrow(() -> new BadRequestException("유효하지 않은 사용자입니다."));
        User friend = userRepository.findById(fid).orElseThrow(() -> new BadRequestException("유효하지 않은 사용자입니다."));
        if (user.equals(friend)) {
            throw new BadRequestException("자기 자신은 팔로잉 할 수 없습니다.");
        }
        Optional<Friend> check = friendRepository.findByFollowerAndFollowing(user, friend);
        if (check.isPresent()) {
            friendRepository.delete(check.get());
        } else {
            friendRepository.save(Friend.builder()
                    .follower(user)
                    .following(friend)
                    .build());
        }
    }

    @Override
    public UserDto getMyFollower(Long uid, Pageable pageable) {
        User user = userRepository.findById(uid).orElseThrow(() -> new BadRequestException("유효하지 않은 사용자입니다."));
        Page<Friend> followers = friendRepository.findByFollowing(user, pageable);
        UserDto result = new UserDto();
        List<Friend> content = followers.getContent();
        List<User> userContent = new ArrayList<>();
        for (Friend friend : content) {
            userContent.add(friend.getFollower());
        }
        result.addUser(userContent, result.getTotalPages(), result.getTotalElements());
        return result;
    }

    @Override
    public UserDto getMyFollowing(Long uid, Pageable pageable) {
        User user = userRepository.findById(uid).orElseThrow(() -> new BadRequestException("유효하지 않은 사용자입니다."));
        Page<Friend> followings = friendRepository.findByFollower(user, pageable);
        UserDto result = new UserDto();
        List<Friend> content = followings.getContent();
        List<User> userContent = new ArrayList<>();
        for (Friend friend : content) {
            userContent.add(friend.getFollowing());
        }
        result.addUser(userContent, result.getTotalPages(), result.getTotalElements());
        return result;
    }
}
