package com.ssafy.prosn.repository.post;

import com.ssafy.prosn.domain.post.LikeDislike;
import com.ssafy.prosn.domain.post.Post;
import com.ssafy.prosn.domain.user.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface LikeDislikeRepository extends JpaRepository<LikeDislike, Long> {
    Long countByPostAndType(Post post, Boolean type);
    Optional<LikeDislike> findByPostAndUser(Post post, User user);
}
