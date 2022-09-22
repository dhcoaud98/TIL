package com.ssafy.prosn.service;

import com.ssafy.prosn.domain.post.Post;
import com.ssafy.prosn.domain.post.PostTag;
import com.ssafy.prosn.domain.post.Problem;
import com.ssafy.prosn.domain.post.Tag;
import com.ssafy.prosn.domain.profile.status.Solving;
import com.ssafy.prosn.domain.user.User;
import com.ssafy.prosn.dto.RateDto;
import com.ssafy.prosn.dto.SolvingRequestDto;
import com.ssafy.prosn.dto.SolvingResponseDto;
import com.ssafy.prosn.dto.WrongAnswerRequestDto;
import com.ssafy.prosn.exception.BadRequestException;
import com.ssafy.prosn.repository.post.ProblemRepository;
import com.ssafy.prosn.repository.post.tag.PostTagRepository;
import com.ssafy.prosn.repository.profiile.status.SolvingRepository;
import com.ssafy.prosn.repository.user.UserRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

/**
 * created by yura on 2022/08/01
 * updated by seongmin on 2022/08/11
 */
@Slf4j
@RequiredArgsConstructor
@Transactional(readOnly = true)
@Service
public class SolvingServiceImpl implements SolvingService {
    private final SolvingRepository solvingRepository;
    private final UserRepository userRepository;
    private final ProblemRepository problemRepository;
    private final WrongAnswerService wrongAnswerService;
    private final int POINT = 10;

    @Override
    public SolvingResponseDto showAllSolving(Long userId, Pageable pageable) {
        Page<Solving> solvings = solvingRepository.findSolvingByUserId(userId, pageable);
        SolvingResponseDto result = new SolvingResponseDto();
        result.addSolving(solvings.getContent(), solvings.getTotalPages(), solvings.getTotalElements());
        return result;
    }

    @Override
    @Transactional
    public void problemSolving(Long uid, SolvingRequestDto dto) {
        User user = userRepository.findById(uid).orElseThrow(() -> new BadRequestException("유효하지 않은 사용자입니다."));
        Problem problem = problemRepository.findById(dto.getPid()).orElseThrow(() -> new BadRequestException("유효하지 않은 문제입니다."));
        Optional<Solving> checkSolving = solvingRepository.findByUserAndProblem(user, problem);
        if (checkSolving.isPresent()) {
            if (!checkSolving.get().isRight() && dto.isRight()) { // 다시풀어서 맞음
                checkSolving.get().correctAnswer();
                user.earnPoints(POINT);
            }
        } else { // 처음 푼 문제
            Solving solving = Solving.builder()
                    .user(user)
                    .problem(problem)
                    .isRight(dto.isRight())
                    .firstIsRight(dto.isRight())
                    .build();
            solvingRepository.save(solving);
            if (dto.isRight()) {
                user.earnPoints(POINT);
            }
        }
        // 틀린 문제는 바로 오답노트로 넘어감
        if (!dto.isRight()) {
            wrongAnswerService.save(new WrongAnswerRequestDto(dto.getPid(), dto.getWrongAnswer()), uid);
        }
    }

    @Override
    public RateDto getRate(Long pid) {
        Problem problem = problemRepository.findById(pid).orElseThrow(() -> new BadRequestException("유효하지 않은 문제입니다."));
        List<Solving> solvingInfos = solvingRepository.findByProblem(problem);
        double submitCnt = solvingInfos.size();
        double correctCnt = (double) solvingInfos.stream().filter(Solving::isFirstIsRight).count();
        return new RateDto(Math.round((correctCnt / submitCnt) * 100) / 100.0 * 100, (int) submitCnt);
    }
}
