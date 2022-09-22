package com.ssafy.prosn.service;

import com.ssafy.prosn.domain.post.Tag;
import com.ssafy.prosn.domain.study.StudyGroup;
import com.ssafy.prosn.domain.study.StudyTag;
import com.ssafy.prosn.domain.study.UserStudy;
import com.ssafy.prosn.domain.user.User;
import com.ssafy.prosn.dto.*;
import com.ssafy.prosn.repository.post.tag.TagRepository;
import com.ssafy.prosn.repository.study.StudyGroupRepository;
import com.ssafy.prosn.repository.study.StudyTagRepository;
import com.ssafy.prosn.repository.study.UserStudyRepository;
import com.ssafy.prosn.repository.user.UserRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import javax.persistence.EntityManager;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

/**
 * created by yeomyeong on 2022/07/26
 * updated by seongmin on 2022/08/11
 */
@Service
@Slf4j
@Transactional(readOnly = true)
@RequiredArgsConstructor
public class StudyServiceImpl implements StudyService {

    private final StudyGroupRepository studyGroupRepository;
    private final UserStudyRepository userStudyRepository;
    private final UserRepository userRepository;
    //    private final EntityManager em;
    private final StudyTagRepository studyTagRepository;
    private final TagRepository tagRepository;

    /**
     * 스터디 생성
     */
    @Transactional
    public StudyGroup create(StudyGroupRequestDto studyGroupDto, Long uid) {
        User user = userRepository.findById(uid).orElseThrow(() -> new IllegalStateException("유효하지 않은 사용자입니다."));
        StudyGroup studyGroup = StudyGroup.builder()
                .title(studyGroupDto.getTitle())
                .mainText(studyGroupDto.getMainText())
                .maxPerson(studyGroupDto.getMaxPerson())
                .secretText(studyGroupDto.getSecretText())
                .expiredDate(studyGroupDto.getExpiredDate())
                .place(studyGroupDto.getPlace())
                .user(user)
                .build();

        StudyGroup save = studyGroupRepository.save(studyGroup);
        UserStudy userStudy = new UserStudy(user, studyGroup);
        userStudyRepository.save(userStudy);
        saveTag(studyGroupDto.getTags(), save);
        return save;
    }

    /**
     * 스터디 상세 내용 수정
     */
    @Transactional
    public StudyGroup update(Long studyGroupId, StudyGroupRequestDto newData) {
        StudyGroup oldData = studyGroupRepository.findById(studyGroupId).get();
        StudyGroup updated = oldData.update(newData);
        saveTag(newData.getTags(), updated);
        return updated;
    }

    /**
     * 스터디 삭제
     */
    public void deleteStudy(StudyGroup studyGroup) {
        List<UserStudy> userStudyList = userStudyRepository.findByStudyGroup(studyGroup);
        List<StudyTag> postTagByStudy = studyTagRepository.findPostTagByStudy(studyGroup);
        userStudyRepository.deleteAll(userStudyList);
        studyTagRepository.deleteAll(postTagByStudy);
        studyGroupRepository.delete(studyGroup);
    }

    /**
     * 스터디 가입
     */
    @Transactional
    public Long joinStudy(Long userId, StudyGroup studyGroup) {
        validateDuplicate(userId, studyGroup.getId());
        User user = userRepository.findById(userId).orElseThrow(() -> new IllegalStateException("유효하지 않은 사용자입니다"));

        UserStudy userStudy = new UserStudy(user, studyGroup);
        studyGroup.addCurrentPerson();
        userStudyRepository.save(userStudy);

        return userStudy.getId();
    }

    /**
     * 스터디 탈퇴
     */
    @Transactional
    public void removeStudy(Long userId, StudyGroup studyGroup) {
        if (!userStudyRepository.existsByUserIdAndStudyGroupId(userId, studyGroup.getId()))
            throw new IllegalStateException("가입되지 않은 스터디입니다.");

        UserStudy userStudy = userStudyRepository.findByUserIdAndStudyGroup(userId, studyGroup);
        studyGroup.removeCurrentPerson();
        userStudyRepository.deleteById(userStudy.getId());
    }

    /**
     * 스터디 상세 내용 조회
     */
    public StudyResponseDto showStudyGroup(Long userId, Long studyGroupId) {
        StudyGroup findGroup = studyGroupRepository.findById(studyGroupId)
                .orElseThrow(() -> new IllegalStateException("유효하지 않은 스터디그룹입니다."));
        // 로그인 유저가 스터디 그룹에 가입돼 있으면
        if (userStudyRepository.existsByUserIdAndStudyGroupId(userId, studyGroupId)) {
            UserStudyResponseDto res = UserStudyResponseDto.builder()
                    .id(findGroup.getId())
                    .title(findGroup.getTitle())
                    .currentPerson(findGroup.getCurrentPerson())
                    .maxPerson(findGroup.getMaxPerson())
                    .place(findGroup.getPlace())
                    .mainText(findGroup.getMainText())
                    .secretText(findGroup.getSecretText())
                    .tags(getTags(findGroup))
                    .mId(findGroup.getUser().getId())
                    .mName(findGroup.getUser().getName())
                    .secret(false)
                    .build();
            List<UserStudy> userStudyList = userStudyRepository.findByStudyGroup(findGroup);
            for (UserStudy userStudy : userStudyList) {
                res.addMember(userStudy.getUser().getId(), userStudy.getUser().getName());
            }
            return res;
        } else {
            return StudyGroupResponseDto.builder()
                    .id(findGroup.getId())
                    .expiredDate(findGroup.getExpiredDate())
                    .mainText(findGroup.getMainText())
                    .maxPerson(findGroup.getMaxPerson())
                    .title(findGroup.getTitle())
                    .currentPerson(findGroup.getCurrentPerson())
                    .place(findGroup.getPlace())
                    .tags(getTags(findGroup))
                    .mId(findGroup.getUser().getId())
                    .mName(findGroup.getUser().getName())
                    .secret(true)
                    .build();
        }

    }

    private void validateDuplicate(Long userId, Long sgId) {
        if (userStudyRepository.existsByUserIdAndStudyGroupId(userId, sgId)) {
            throw new IllegalStateException("이미 가입된 스터디입니다.");
        }
    }

    private void saveTag(List<String> studyTags, StudyGroup study) {
        List<StudyTag> postTagByStudy = studyTagRepository.findPostTagByStudy(study);
        if (postTagByStudy.size() != 0) {
            studyTagRepository.deleteByStudyId(study.getId());
        }
        studyTags.forEach(code -> {
            Optional<Tag> tag = tagRepository.findByCode(code);
            tag.orElseThrow(() -> new IllegalArgumentException("유효하지 않은 태그입니다."));
            studyTagRepository.save(new StudyTag(study, tag.get()));
        });
    }

    private List<Tag> getTags(StudyGroup study) {
        List<StudyTag> postTagByStudy = studyTagRepository.findPostTagByStudy(study);
        List<Tag> tags = new ArrayList<>();
        postTagByStudy.forEach(postTag -> {
            tags.add(postTag.getTag());
        });
        return tags;
    }
}
