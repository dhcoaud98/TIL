package com.ssafy.prosn.domain.post;

import com.ssafy.prosn.domain.user.User;
import lombok.*;
import org.hibernate.annotations.DynamicInsert;

import javax.persistence.Entity;

/**
 * created by seongmin on 2022/07/19
 * updated by seongmin on 2022/07/27
 */
@Entity
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@DynamicInsert
@Getter
public class Problem extends Post {

    private String example1;
    private String example2;
    private String example3;
    private String example4;

    private String answer;

    private String mainText;

    @Builder
    public Problem(String title, User user, String example1, String example2, String example3, String example4, String answer, String mainText) {
        super(title, user);
        this.example1 = example1;
        this.example2 = example2;
        this.example3 = example3;
        this.example4 = example4;
        this.answer = answer;
        this.mainText = mainText;
    }
}
