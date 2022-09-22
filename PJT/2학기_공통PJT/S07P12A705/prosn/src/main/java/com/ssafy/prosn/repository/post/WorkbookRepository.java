package com.ssafy.prosn.repository.post;

import com.ssafy.prosn.domain.post.Workbook;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

/**
 * created by seongmin on 2022/08/08
 */
public interface WorkbookRepository extends JpaRepository<Workbook, Long> {
    Page<Workbook> findAll(Pageable pageable);
}
