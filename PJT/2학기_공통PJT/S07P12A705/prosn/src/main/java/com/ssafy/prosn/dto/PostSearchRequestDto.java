package com.ssafy.prosn.dto;

import com.ssafy.prosn.domain.post.PostType;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.RequiredArgsConstructor;

/**
 * created by seongmin on 2022/07/28
 * updated by seongmin on 2022/08/09
 */
@Getter
@RequiredArgsConstructor
@AllArgsConstructor
public class PostSearchRequestDto {
    private String title;
    private String code;
    private PostType dtype;
}
