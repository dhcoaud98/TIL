package com.ssafy.prosn.service;

import com.ssafy.prosn.domain.comment.Comment;
import com.ssafy.prosn.domain.post.Post;
import com.ssafy.prosn.domain.user.User;
import com.ssafy.prosn.dto.CommentRequestDto;
import com.ssafy.prosn.dto.UserResponseDto;
import com.ssafy.prosn.exception.BadRequestException;
import com.ssafy.prosn.exception.NotAccessUserException;
import com.ssafy.prosn.repository.comment.CommentRepository;
import com.ssafy.prosn.repository.post.PostRepository;
import com.ssafy.prosn.repository.user.UserRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

/**
 * created by seongmin on 2022/07/25
 * updated by seongmin on 2022/08/10
 */
@Slf4j
@RequiredArgsConstructor
@Transactional(readOnly = true)
@Service
public class CommentServiceImpl implements CommentService {

    private final UserRepository userRepository;
    private final CommentRepository commentRepository;
    private final PostRepository postRepository;

    @Override
    @Transactional
    public Comment write(CommentRequestDto commentRequestDto, Long uid) {
        Post post = postRepository.findById(commentRequestDto.getPid()).orElseThrow(() -> new BadRequestException("유효하지 않은 게시글입니다."));
        User user = userRepository.findById(uid).orElseThrow(() -> new BadRequestException("유효하지 않은 사용자입니다."));

        Comment comment = Comment.builder()
                .post(post)
                .user(user)
                .mainText(commentRequestDto.getMainText())
                .build();
        return commentRepository.save(comment);
    }

    @Override
    @Transactional
    public void delete(Long id, Long uid) {
        Comment comment = commentRepository.findById(id).orElseThrow(() -> new BadRequestException("유효하지 않은 댓글입니다."));
        if (!comment.getUser().getId().equals(uid))
            throw new NotAccessUserException("내가 쓴 댓글만 삭제 가능합니다.");

        commentRepository.deleteById(id);
    }
}
