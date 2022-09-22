package com.ssafy.prosn.service;

import com.ssafy.prosn.domain.profile.note.WrongAnswer;
import com.ssafy.prosn.dto.*;
import org.springframework.data.domain.Pageable;

import java.util.List;

/**
 * created by seongmin on 2022/07/29
 * updated by seongmin on 2022/08/06
 */
public interface WrongAnswerService {

    WrongAnswer save(WrongAnswerRequestDto dto, Long uid);

    void write(WrongNoteRequestDto dto, Long uid);

    void delete(Long id, Long uid);

    NoteResponseDto getNote(Long uid, Pageable pageable, boolean isWrite);
    NoteResponseDto getNoteByTag(Long uid, Pageable pageable, boolean isWrite, String tag);
    WrongAnswerNoteDetailResponseDto getNoteDetail(Long id, Long uid);
}
