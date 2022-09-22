package com.ssafy.prosn.repository.profiile.scrap;

import com.ssafy.prosn.domain.post.Post;
import com.ssafy.prosn.domain.profile.scrap.PostList;
import com.ssafy.prosn.domain.profile.scrap.Scrap;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

/**
 * created by seongmin on 2022/08/04
 * updated by seongmin on 2022/08/11
 */
public interface ScrapRepository extends JpaRepository<Scrap, Long> {
    List<Scrap> findByPostList(PostList postList);
    Page<Scrap> findByPostList(PostList postList, Pageable pageable);
    Optional<Scrap> findByPostAndPostList(Post post, PostList postList);
}
