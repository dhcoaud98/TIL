package com.ssafy.prosn.repository.post;

import com.ssafy.prosn.domain.post.Information;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

/**
 * created by seongmin on 2022/08/07
 */
public interface InformationRepository extends JpaRepository<Information, Long> {
    @Query("select i from Information  i where i.isDeleted = FALSE")
    List<Information> findAllInformation();

    Page<Information> findByIsDeleted(boolean isDeleted, Pageable pageable);
}
