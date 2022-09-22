package com.ssafy.prosn.service;

import com.ssafy.prosn.domain.post.Workbook;
import com.ssafy.prosn.dto.PostResponseDto;
import org.springframework.data.domain.Pageable;

/**
 * created by seongmin on 2022/08/08
 */
public interface WorkbookService {

    Workbook save(Long pid, Long uid, String title); // problemList(폴더) 아이디, 사용자 아이디
    PostResponseDto showAllWorkbook(Pageable pageable);

    Workbook update(Long uid, Long wid, String title);
}
