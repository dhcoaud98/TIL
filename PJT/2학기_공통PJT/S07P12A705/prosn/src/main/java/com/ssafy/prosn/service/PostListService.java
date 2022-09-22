package com.ssafy.prosn.service;

import com.ssafy.prosn.dto.PostListFolderResponseDto;

import java.util.List;

/**
 * created by seongmin on 2022/08/04
 * updated by seongmin on 2022/08/05
 */
public interface PostListService {
    List<PostListFolderResponseDto> getPostListFolder(Long uid);

    Long make(Long uid, String title);

    void delete(Long uid, Long id);
}
