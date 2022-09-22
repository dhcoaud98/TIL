package com.ssafy.prosn.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.RequiredArgsConstructor;

/**
 * created by seongmin on 2022/08/04
 */

@Getter
@RequiredArgsConstructor
@AllArgsConstructor
public class PostListFolderResponseDto {
    // PostList 폴더 아이디
    private Long id;
    // 폴더 이름
    private String title;
}
