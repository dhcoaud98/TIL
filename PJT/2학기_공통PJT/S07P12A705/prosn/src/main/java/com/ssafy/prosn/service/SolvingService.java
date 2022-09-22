package com.ssafy.prosn.service;

import com.ssafy.prosn.domain.profile.status.Solving;
import com.ssafy.prosn.dto.RateDto;
import com.ssafy.prosn.dto.SolvingRequestDto;
import com.ssafy.prosn.dto.SolvingResponseDto;
import org.springframework.data.domain.Pageable;

import java.util.List;

/**
 * created by yura on 2022/08/01
 * updated by seongmin on 2022/08/06
 */
public interface SolvingService {
    SolvingResponseDto showAllSolving(Long uid, Pageable pageable);
    void problemSolving(Long uid, SolvingRequestDto dto);
    RateDto getRate(Long pid);
}
