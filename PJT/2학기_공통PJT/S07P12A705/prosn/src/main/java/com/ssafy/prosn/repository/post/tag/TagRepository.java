package com.ssafy.prosn.repository.post.tag;

import com.ssafy.prosn.domain.post.Tag;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

/**
 * created by seongmin on 2022/07/22
 * updated by seongmin on 2022/07/25
 */
public interface TagRepository extends JpaRepository<Tag, Long> {
    Optional<Tag> findByCode(String code);
}
