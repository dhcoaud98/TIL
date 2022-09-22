package com.ssafy.prosn.repository.post;

import com.ssafy.prosn.domain.post.Problem;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

/**
 * created by seongmin on 2022/07/22
 * updated by seongmin on 2022/08/10
 */
public interface ProblemRepository extends JpaRepository<Problem, Long>, ProblemRepositoryCustom {
    @Query("select p from Problem  p where p.isDeleted = FALSE")
    List<Problem> findAllProblem();

    Page<Problem> findByIsDeleted(boolean isDeleted, Pageable pageable);
}
