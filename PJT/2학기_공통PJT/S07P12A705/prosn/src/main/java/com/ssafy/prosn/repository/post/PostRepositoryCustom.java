package com.ssafy.prosn.repository.post;

import com.ssafy.prosn.domain.post.Post;
import com.ssafy.prosn.domain.post.PostTag;
import com.ssafy.prosn.domain.post.PostType;
import com.ssafy.prosn.dto.PostDto;
import com.ssafy.prosn.dto.ProblemDto;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import java.util.List;

/**
 * created by seongmin on 2022/07/22
 * updated by seongmin on 2022/08/10
 */
public interface PostRepositoryCustom {
    Page<ProblemDto> searchPost(boolean isDeleted, Pageable pageable,String title, String code, PostType ptype);
    Page<ProblemDto> getProblemWorkbook(boolean isDeleted, Pageable pageable);
}
