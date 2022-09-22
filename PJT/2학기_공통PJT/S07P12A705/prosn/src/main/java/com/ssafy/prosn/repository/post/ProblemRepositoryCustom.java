package com.ssafy.prosn.repository.post;

import com.ssafy.prosn.dto.PopularityProblemDto;

import java.util.List;

/**
 * created by seongmin on 2022/08/10
 */
public interface ProblemRepositoryCustom {
    List<PopularityProblemDto> popularProblem();
}
