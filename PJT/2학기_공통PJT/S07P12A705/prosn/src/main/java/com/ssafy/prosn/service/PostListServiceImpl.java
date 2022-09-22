package com.ssafy.prosn.service;

import com.ssafy.prosn.domain.profile.scrap.PostList;
import com.ssafy.prosn.domain.user.User;
import com.ssafy.prosn.dto.PostListFolderResponseDto;
import com.ssafy.prosn.exception.BadRequestException;
import com.ssafy.prosn.exception.NotAccessUserException;
import com.ssafy.prosn.repository.profiile.scrap.PostListRepository;
import com.ssafy.prosn.repository.user.UserRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;

/**
 * created by seongmin on 2022/08/04
 * updated by seongmin on 2022/08/08
 */
@Service
@RequiredArgsConstructor
@Transactional(readOnly = true)
@Slf4j
public class PostListServiceImpl implements PostListService {

    private final PostListRepository postListRepository;
    private final UserRepository userRepository;

    @Override
    public List<PostListFolderResponseDto> getPostListFolder(Long uid) {
        User user = userRepository.findById(uid).orElseThrow(() -> new BadRequestException("유효하지 않은 사용자입니다."));
        List<PostList> postLists = postListRepository.findByUser(user);
        List<PostListFolderResponseDto> result = new ArrayList<>();
        for (PostList postList : postLists) {
            result.add(new PostListFolderResponseDto(postList.getId(), postList.getTitle()));
        }

        return result;
    }

    @Override
    @Transactional
    public Long make(Long uid, String title) {
        User user = userRepository.findById(uid).orElseThrow(() -> new BadRequestException("유효하지 않은 사용자입니다."));
        PostList savePostList = postListRepository.save(PostList.builder()
                .user(user)
                .title(title).build());
        return savePostList.getId();
    }

    @Override
    @Transactional
    public void delete(Long uid, Long id) {
        User user = userRepository.findById(uid).orElseThrow(() -> new BadRequestException("유효하지 않은 사용자입니다."));
        PostList postList = postListRepository.findById(id).orElseThrow(() -> new BadRequestException("유효하지 않은 폴더입니다."));
        if (!postList.getUser().equals(user)) {
            throw new NotAccessUserException("삭제 할 권한이 없습니다.");
        }
        postListRepository.delete(postList);
    }
}
