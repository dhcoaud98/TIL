package com.ssafy.prosn.service;

import com.ssafy.prosn.domain.comment.Comment;
import com.ssafy.prosn.domain.comment.Reply;
import com.ssafy.prosn.domain.user.User;
import com.ssafy.prosn.dto.ReplyRequestDto;
import com.ssafy.prosn.exception.BadRequestException;
import com.ssafy.prosn.exception.NotAccessUserException;
import com.ssafy.prosn.repository.comment.CommentRepository;
import com.ssafy.prosn.repository.comment.ReplyRepository;
import com.ssafy.prosn.repository.user.UserRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Optional;

/**
 * created by seongmin on 2022/07/28
 * updated by seongmin on 2022/08/01
 */
@Slf4j
@RequiredArgsConstructor
@Transactional(readOnly = true)
@Service
public class ReplyServiceImpl implements ReplyService {
    private final UserRepository userRepository;
    private final CommentRepository commentRepository;
    private final ReplyRepository replyRepository;

    @Override
    @Transactional
    public Reply write(ReplyRequestDto replyRequestDto, Long uid) {
        User user = userRepository.findById(uid).orElseThrow(() -> new BadRequestException("유효하지 않은 사용자입니다."));
        Comment comment = commentRepository.findById(replyRequestDto.getCid())
                .orElseThrow(() -> new BadRequestException("유효하지 않은 댓글입니다."));

        Reply reply = Reply.builder()
                .user(user)
                .comment(comment)
                .mainText(replyRequestDto.getMainText())
                .build();
        return replyRepository.save(reply);
    }

    @Override
    @Transactional
    public void delete(Long id, Long uid) {
        Optional<Reply> reply = replyRepository.findById(id);
        reply.orElseThrow(() -> new BadRequestException("유효하지 않은 답글입니다."));
        if (!reply.get().getUser().getId().equals(uid)) throw new NotAccessUserException("내가 쓴 답글만 삭제 가능합니다.");

        replyRepository.deleteById(id);
    }
}
