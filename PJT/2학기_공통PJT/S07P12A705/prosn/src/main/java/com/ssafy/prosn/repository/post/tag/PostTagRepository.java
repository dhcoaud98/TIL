package com.ssafy.prosn.repository.post.tag;

import com.ssafy.prosn.domain.post.Post;
import com.ssafy.prosn.domain.post.PostTag;
import com.ssafy.prosn.domain.post.Tag;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

/**
 * created by seongmin on 2022/07/22
 */
public interface PostTagRepository extends JpaRepository<PostTag, Long> {
    List<PostTag> findPostTagByPost(Post post);
}
