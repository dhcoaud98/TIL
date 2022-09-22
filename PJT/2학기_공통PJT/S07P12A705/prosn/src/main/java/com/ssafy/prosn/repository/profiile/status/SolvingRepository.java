package com.ssafy.prosn.repository.profiile.status;

import com.ssafy.prosn.domain.post.Problem;
import com.ssafy.prosn.domain.profile.status.Solving;
import com.ssafy.prosn.domain.user.User;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

/**
 * created by yura on 2022/08/01
 * updated by seongmin on 2022/08/11
 */
public interface SolvingRepository extends JpaRepository<Solving, Long> {
    Page<Solving> findSolvingByUserId(Long userId, Pageable pageable);

    Optional<Solving> findByUserAndProblem(User user, Problem problem);

    List<Solving> findByProblem(Problem problem);

    Long countByUser(User user);

    Long countByUserAndFirstIsRight(User user, boolean firstIsRight);
}
