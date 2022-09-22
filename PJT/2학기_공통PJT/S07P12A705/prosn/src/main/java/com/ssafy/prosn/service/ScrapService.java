package com.ssafy.prosn.service;

import com.ssafy.prosn.domain.profile.scrap.Scrap;
import com.ssafy.prosn.dto.ScrapDto;
import com.ssafy.prosn.dto.ScrapResponseDto;
import org.springframework.data.domain.Pageable;

import java.util.List;

/**
 * created by seongmin on 2022/08/04
 */
public interface ScrapService {
    Scrap save(Long pid, Long lid, Long uid); // 포스트 id와 postList(폴더) id
    ScrapResponseDto getScrapList(Long lid, Pageable pageable); // id는 postList(폴더) 아이디

    void delete(Long uid, Long id);
}
