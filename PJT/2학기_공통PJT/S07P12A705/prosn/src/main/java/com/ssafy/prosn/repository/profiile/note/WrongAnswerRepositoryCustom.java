package com.ssafy.prosn.repository.profiile.note;

import com.ssafy.prosn.domain.user.User;
import com.ssafy.prosn.dto.NoteDto;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

/**
 * created by seongmin on 2022/08/07
 */
public interface WrongAnswerRepositoryCustom {
    Page<NoteDto> findWrongAnswer(User user, boolean isWrite, Pageable pageable, String tag);
}
