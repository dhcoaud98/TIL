package com.ssafy.prosn.repository.profiile.note;

import com.querydsl.core.types.Predicate;
import com.querydsl.core.types.Projections;
import com.querydsl.jpa.impl.JPAQueryFactory;
import com.ssafy.prosn.domain.user.User;
import com.ssafy.prosn.dto.NoteDto;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageImpl;
import org.springframework.data.domain.Pageable;

import javax.persistence.EntityManager;
import java.util.List;

import static com.ssafy.prosn.domain.post.QPostTag.*;
import static com.ssafy.prosn.domain.profile.note.QWrongAnswer.*;

/**
 * created by seongmin on 2022/08/07
 */
public class WrongAnswerRepositoryImpl implements WrongAnswerRepositoryCustom {

    private final JPAQueryFactory queryFactory;

    public WrongAnswerRepositoryImpl(EntityManager em) {
        this.queryFactory = new JPAQueryFactory(em);
    }

    //    @Override
//    public Page<NoteResponseDto> findWrongAnswer(User user, boolean isWrite, Pageable pageable, String tag) {
//        List<NoteResponseDto> result = queryFactory
//                .select(Projections.fields(NoteResponseDto.class,
//                        wrongAnswer1.id,
//                        wrongAnswer1.problem.title,
//                        wrongAnswer1.isWrite,
//                        wrongAnswer1.problem))
//                .from(wrongAnswer1)
//                .where(wrongAnswer1.user.eq(user), wrongAnswer1.isWrite.eq(isWrite))
//                .offset(pageable.getOffset())
//                .limit(pageable.getPageSize())
//                .fetch();
//        return new PageImpl<>(result, pageable, result.size());
//    }
    @Override
    public Page<NoteDto> findWrongAnswer(User user, boolean isWrite, Pageable pageable, String tag) {
        List<NoteDto> result = queryFactory
                .select(Projections.fields(NoteDto.class,
                        wrongAnswer1.id,
                        wrongAnswer1.problem.title,
                        wrongAnswer1.isWrite,
                        wrongAnswer1.problem
                ))
                .from(wrongAnswer1)
                .join(postTag).on(wrongAnswer1.problem.id.eq(postTag.post.id))
                .where(wrongAnswer1.user.eq(user), wrongAnswer1.isWrite.eq(isWrite), tagContains(tag))
                .offset(pageable.getOffset())
                .limit(pageable.getPageSize())
//                .orderBy(wrongAnswer1.updated.asc())
                .fetch();
        return new PageImpl<>(result, pageable, result.size());
    }

    private Predicate tagContains(String tag) {
        if (tag.equals("")) {
            tag = null;
        }
        return tag != null ? postTag.tag.code.contains(tag) : null;
    }
}
