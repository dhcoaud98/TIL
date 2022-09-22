package com.ssafy.prosn.service;

import com.ssafy.prosn.domain.post.Post;
import com.ssafy.prosn.domain.post.PostType;
import com.ssafy.prosn.dto.*;
import org.springframework.data.domain.Pageable;

import java.util.List;

/**
 * created by seongmin on 2022/07/25
 * updated by seongmin on 2022/08/12
 */
public interface PostService {
    Post writeProblem(ProblemRequestDto problemDto, Long uid);

    Post writeInformation(InformationRequestDto informationDto, Long uid);

    void delete(Long id, Long uid);

    PostDetailResponseDto showProblemDetail(Long id);

    PostResponseDto showAllPost(Pageable pageable);

    ProblemWorkbookResponseDto showAllProblem(Pageable pageable);

    PostResponseDto showAllInformation(Pageable pageable);

    LikeDisLikeNumDto likeDislikeClick(LikeDisLikeRequestDto likeDisLikeDto, Long uid);

    ProblemWorkbookResponseDto search(Pageable pageable, String title, String code, PostType dtype);

    int updateViews(Long id);

    List<PopularityProblemResponseDto> popularProblem();

}
