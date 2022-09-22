package com.ssafy.prosn.domain.post;

import com.ssafy.prosn.domain.BaseEntity;
import lombok.*;

import javax.persistence.*;

/**
 * created by seongmin on 2022/07/19
 * updated by seongmin on 2022/07/19
 */
@Entity
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Getter
public class ProblemWorkbook extends BaseEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "problem_id")
    private Problem problem;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "workbook_id")
    private Workbook workbook;

    @Builder
    public ProblemWorkbook(Problem problem, Workbook workbook) {
        this.problem = problem;
        this.workbook = workbook;
    }
}
