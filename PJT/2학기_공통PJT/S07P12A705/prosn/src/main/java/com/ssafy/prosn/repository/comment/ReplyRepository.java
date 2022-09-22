package com.ssafy.prosn.repository.comment;

import com.ssafy.prosn.domain.comment.Reply;
import org.springframework.data.jpa.repository.JpaRepository;

/**
 * created by seongmin on 2022/07/20
 */
public interface ReplyRepository extends JpaRepository<Reply, Long> {
}
