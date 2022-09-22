package com.ssafy.prosn.repository.post;

import com.querydsl.core.types.Projections;
import com.querydsl.jpa.impl.JPAQueryFactory;
import com.ssafy.prosn.dto.PopularityProblemDto;

import javax.persistence.EntityManager;
import java.util.List;

import static com.ssafy.prosn.domain.post.QProblem.*;
import static com.ssafy.prosn.domain.profile.status.QSolving.*;

/**
 * created by seongmin on 2022/08/10
 */
public class ProblemRepositoryImpl implements ProblemRepositoryCustom {
    private final JPAQueryFactory queryFactory;

    public ProblemRepositoryImpl(EntityManager em) {
        this.queryFactory = new JPAQueryFactory(em);
    }

    @Override
    public List<PopularityProblemDto> popularProblem() {
        return queryFactory
                .select(Projections.fields(PopularityProblemDto.class,
                        problem.id,
                        problem.title,
                        problem.numOfLikes,
                        problem.views,
                        problem.count().as("submissionNum")
                ))
                .from(problem).join(problem.solvingList, solving)
                .groupBy(problem.id)
                .orderBy(((problem.views.divide(2)).add((problem.numOfDislikes).multiply(5)).add(problem.id.count()).multiply(3)).desc())
                .limit(3)
                .fetch();
    }
}
