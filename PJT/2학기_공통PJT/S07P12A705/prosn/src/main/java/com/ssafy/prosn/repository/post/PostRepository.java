package com.ssafy.prosn.repository.post;

import com.ssafy.prosn.domain.post.Post;
import com.ssafy.prosn.domain.user.User;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Lock;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import javax.persistence.LockModeType;
import java.util.List;

/**
 * created by seongmin on 2022/07/20
 * updated by seongmin on 2022/08/11
 */
public interface PostRepository extends JpaRepository<Post, Long>, PostRepositoryCustom {
    @Query("select p from Post  p where p.isDeleted = FALSE")
    List<Post> findAllPost();

    Page<Post> findByIsDeleted(boolean isDeleted, Pageable pageable);
    Page<Post> findByIsDeletedAndUser(boolean isDeleted, User user, Pageable pageable);

    Long countByUser(User user);
    @Modifying
//    @Lock(LockModeType.OPTIMISTIC)
    @Query("update Post p set p.views = p.views + 1 where p.id = :id")
    int updateViews(@Param("id") Long id);
}
