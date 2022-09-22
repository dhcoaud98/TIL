package com.ssafy.prosn.domain.post;

import com.ssafy.prosn.domain.user.User;
import lombok.*;
import org.hibernate.annotations.DynamicInsert;

import javax.persistence.Entity;

/**
 * created by seongmin on 2022/07/19
 * updated by seongmin on 2022/08/15
 */
@Entity
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@DynamicInsert
@Getter
public class Information extends Post {

//    private String mainText;

    @Builder
    public Information(String title, User user, String mainText) {
        super(title, mainText, user);
//        this.mainText = mainText;
    }
}
