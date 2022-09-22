package com.ssafy.prosn.service;

import com.ssafy.prosn.domain.post.Post;
import com.ssafy.prosn.domain.post.Problem;
import com.ssafy.prosn.domain.post.ProblemWorkbook;
import com.ssafy.prosn.domain.post.Workbook;
import com.ssafy.prosn.domain.profile.scrap.PostList;
import com.ssafy.prosn.domain.profile.scrap.Scrap;
import com.ssafy.prosn.domain.user.User;
import com.ssafy.prosn.dto.PostResponseDto;
import com.ssafy.prosn.exception.BadRequestException;
import com.ssafy.prosn.repository.post.ProblemWorkbookRepository;
import com.ssafy.prosn.repository.post.WorkbookRepository;
import com.ssafy.prosn.repository.profiile.scrap.PostListRepository;
import com.ssafy.prosn.repository.profiile.scrap.ScrapRepository;
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
 * created by seongmin on 2022/08/08
 */
@Slf4j
@RequiredArgsConstructor
@Transactional(readOnly = true)
@Service
public class WorkbookServiceImpl implements WorkbookService {

    private final UserRepository userRepository;
    private final ProblemWorkbookRepository problemWorkbookRepository;
    private final ScrapRepository scrapRepository;
    private final PostListRepository postListRepository;
    private final WorkbookRepository workbookRepository;

    @Override
    @Transactional
    public Workbook save(Long pid, Long uid, String title) {
        User user = userRepository.findById(uid).orElseThrow(() -> new BadRequestException("유효하지 않은 사용자입니다."));
        PostList postList = postListRepository.findById(pid).orElseThrow(() -> new BadRequestException("유효하지 않은 폴더입니다."));
        List<Scrap> scraps = scrapRepository.findByPostList(postList);
        Workbook workbook = Workbook.builder()
                .title(title)
                .user(user)
                .build();

        List<ProblemWorkbook> problemList = new ArrayList<>();
        for (Scrap scrap : scraps) {
            Post post = scrap.getPost();
            if (post instanceof Problem) {
                problemList.add(new ProblemWorkbook((Problem) scrap.getPost(), workbook));
            }
        }
        problemWorkbookRepository.saveAll(problemList);
        return workbook;
    }

    @Override
    public PostResponseDto showAllWorkbook(Pageable pageable) {
        Page<Workbook> workbooks = workbookRepository.findAll(pageable);
        PostResponseDto result = new PostResponseDto();
//        List<Workbook> content = workbooks.getContent();
//        List<ProblemWorkbook> problemWorkbooks = content.get(0).getProblemWorkbooks();
        result.addPost(workbooks.getContent(), workbooks.getTotalPages(), workbooks.getTotalElements());
        return result;
    }

    @Override
    @Transactional
    public Workbook update(Long uid, Long wid, String title) {
        User user = userRepository.findById(uid).orElseThrow(() -> new BadRequestException("유효하지 않은 사용자입니다."));
        Workbook workbook = workbookRepository.findById(wid).orElseThrow(() -> new BadRequestException("유효하지 않은 문제집입니다."));
        workbook.renameTitle(title);
        return workbook;
    }
}
