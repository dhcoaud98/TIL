package com.ssafy.prosn.service;

import com.ssafy.prosn.domain.comment.Comment;
import com.ssafy.prosn.dto.CommentRequestDto;

/**
 * created by seongmin on 2022/07/25
 * updated by seongmin on 2022/08/01
 */
public interface CommentService {
    Comment write(CommentRequestDto commentRequestDto, Long uid);
    void delete(Long id, Long uid);
}
