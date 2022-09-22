package com.ssafy.prosn.service;

import com.ssafy.prosn.domain.post.PostTag;
import com.ssafy.prosn.domain.post.Problem;
import com.ssafy.prosn.domain.post.Tag;
import com.ssafy.prosn.domain.profile.note.WrongAnswer;
import com.ssafy.prosn.domain.user.User;
import com.ssafy.prosn.dto.*;
import com.ssafy.prosn.exception.BadRequestException;
import com.ssafy.prosn.exception.NotAccessUserException;
import com.ssafy.prosn.repository.post.ProblemRepository;
import com.ssafy.prosn.repository.post.tag.PostTagRepository;
import com.ssafy.prosn.repository.profiile.note.WrongAnswerRepository;
import com.ssafy.prosn.repository.user.UserRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;

/**
 * created by seongmin on 2022/07/29
 * updated by seongmin on 2022/08/08
 */
@Slf4j
@RequiredArgsConstructor
@Transactional(readOnly = true)
@Service
public class WrongAnswerServiceImpl implements WrongAnswerService {

    private final WrongAnswerRepository wrongAnswerRepository;
    private final UserRepository userRepository;
    private final ProblemRepository problemRepository;
    private final PostTagRepository postTagRepository;


    // 틀린 문제 저장
    @Override
    @Transactional
    public WrongAnswer save(WrongAnswerRequestDto dto, Long uid) {
        User user = userRepository.findById(uid).orElseThrow(() -> new BadRequestException("유효하지 않은 사용자입니다."));
        Problem problem = problemRepository.findById(dto.getPid()).orElseThrow(() -> new BadRequestException("유효하지 않은 문제입니다."));
        // 문제집에서 풀었는데 삭제된 문제라면 어떻게?? -> 조회할 때 작성자와 날짜만 안보이게 하기.

        // 이미 오답문제에 있는 문제라면? 틀린답만 수정 or 수정x
        boolean check = wrongAnswerRepository.existsByUserAndProblem(user, problem);
        if (check) {
            WrongAnswer wrongAnswer = wrongAnswerRepository.findByUserAndProblem(user, problem).orElseThrow(() -> new BadRequestException("유효하지 않은 오답노트입니다."));
            wrongAnswer.writeWrongAnswer(dto.getWrongAnswer());
            return wrongAnswer;
        }

        WrongAnswer wrongAnswer = WrongAnswer.builder()
                .problem(problem)
                .user(user)
                .wrong_answer(dto.getWrongAnswer())
                .build();
        return wrongAnswerRepository.save(wrongAnswer);
    }

    // 오답 노트 수정
    @Override
    @Transactional
    public void write(WrongNoteRequestDto dto, Long uid) {
        WrongAnswer wrongAnswer = validWrongAnswer(dto.getId());
        User user = userRepository.findById(uid).orElseThrow(() -> new BadRequestException("유효하지 않은 사용자입니다."));


        if (!user.equals(wrongAnswer.getUser())) {
            throw new NotAccessUserException("권한이 없습니다."); // 403으로 리턴하도록하기.
        }


        wrongAnswer.writeMemo(dto.getMemo());
        wrongAnswer.writeReason(dto.getReason());
        wrongAnswer.writeStudyContent(dto.getStudyContent());
        wrongAnswer.write();
    }

    @Override
    @Transactional
    public void delete(Long id, Long uid) {
        WrongAnswer wrongAnswer = validWrongAnswer(id);
        User user = userRepository.findById(uid).orElseThrow(() -> new BadRequestException("유효하지 않은 사용자입니다."));

        if (!user.equals(wrongAnswer.getUser())) {
            throw new NotAccessUserException("권한이 없습니다."); // 403으로 리턴하도록하기.
        }

        wrongAnswerRepository.delete(wrongAnswer);
    }

    // 내 오답노트 전체(목록) 조회
    @Override
    public NoteResponseDto getNote(Long uid, Pageable pageable, boolean isWrite) {
        User user = userRepository.findById(uid).orElseThrow(() -> new BadRequestException("유효하지 않은 사용자입니다."));

        Page<WrongAnswer> wrongAnswers = wrongAnswerRepository.findByUserAndIsWrite(user, isWrite, pageable);
        List<WrongAnswer> content = wrongAnswers.getContent();
        List<NoteDto> notes = new ArrayList<>();
        for (WrongAnswer wrongAnswer : content) {
            notes.add(new NoteDto(wrongAnswer.getId(), wrongAnswer.getProblem().getTitle(), wrongAnswer.isWrite(), wrongAnswer.getProblem()));
        }
        NoteResponseDto result = new NoteResponseDto();
        result.addNote(notes, wrongAnswers.getTotalPages(), wrongAnswers.getTotalElements());
        return result;
    }

    // 오답 노트 태그로 조회
    @Override
    public NoteResponseDto getNoteByTag(Long uid, Pageable pageable, boolean isWrite, String tag) {
        User user = userRepository.findById(uid).orElseThrow(() -> new BadRequestException("유효하지 않은 사용자입니다."));

        Page<NoteDto> notes = wrongAnswerRepository.findWrongAnswer(user, isWrite, pageable, tag);
        NoteResponseDto result = new NoteResponseDto();
        result.addNote(notes.getContent(), notes.getTotalPages(), notes.getTotalElements());
        return result;
    }

    // 오답노트에서 특정 문제 디테일 조회
    @Override
    public WrongAnswerNoteDetailResponseDto getNoteDetail(Long id, Long uid) {
        User user = userRepository.findById(uid).orElseThrow(() -> new BadRequestException("유효하지 않은 사용자입니다."));
        WrongAnswer wrongAnswer = validWrongAnswer(id);
        if (!user.equals(wrongAnswer.getUser())) {
            throw new IllegalStateException("권한이 없습니다.");
        }
        List<PostTag> postTagByPost = postTagRepository.findPostTagByPost(wrongAnswer.getProblem());
        List<Tag> tags = new ArrayList<>();
        for (PostTag postTag : postTagByPost) {
            tags.add(postTag.getTag());
        }
        return WrongAnswerNoteDetailResponseDto.builder()
                .id(id)
                .pid(wrongAnswer.getProblem().getId())
                .pid(wrongAnswer.getProblem().getId())
                .title(wrongAnswer.getProblem().getTitle())
                .tags(tags)
                .mainText(wrongAnswer.getProblem().getMainText())
                .example1(wrongAnswer.getProblem().getExample1())
                .example2(wrongAnswer.getProblem().getExample2())
                .example3(wrongAnswer.getProblem().getExample3())
                .example4(wrongAnswer.getProblem().getExample4())
                .answer(wrongAnswer.getProblem().getAnswer())
                .isDeleted(wrongAnswer.getProblem().isDeleted())
                .wrongAnswer(wrongAnswer.getWrongAnswer())
                .reason(wrongAnswer.getReason())
                .studyContent(wrongAnswer.getStudyContent())
                .memo(wrongAnswer.getMemo())
                .isWrite(wrongAnswer.isWrite())
                .build();
    }

    private WrongAnswer validWrongAnswer(Long id) {
        return wrongAnswerRepository.findById(id).orElseThrow(() -> new BadRequestException("유효하지 않은 오답노트입니다."));
    }
}
