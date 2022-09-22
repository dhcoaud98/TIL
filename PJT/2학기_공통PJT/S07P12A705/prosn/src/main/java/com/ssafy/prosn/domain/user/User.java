package com.ssafy.prosn.domain.user;

import com.ssafy.prosn.domain.BaseEntity;
import com.ssafy.prosn.domain.post.Post;
import com.ssafy.prosn.domain.profile.scrap.PostList;
import lombok.*;
import org.hibernate.annotations.ColumnDefault;
import org.hibernate.annotations.DynamicInsert;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

/**
 * created by seongmin on 2022/07/18
 * updated by seongmin on 2022/08/04
 */
@Entity
@Inheritance(strategy = InheritanceType.JOINED)
@DiscriminatorColumn
@DynamicInsert
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Getter
@Table(name = "users")
public abstract class User extends BaseEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
    private String email;

    @OneToMany(mappedBy = "user", fetch = FetchType.LAZY)
    private List<Post> posts = new ArrayList<>();

    @OneToMany(mappedBy = "user", fetch = FetchType.LAZY)
    private List<PostList> postLists = new ArrayList<>();

    @ColumnDefault("0")
    private Integer point;

    @Enumerated(EnumType.STRING)
    private Authority authority;
    public User(String name, String email) {
        this.name = name;
        this.email = email;
        this.point = 0;
        this.authority = Authority.ROLE_USER;
    }

    /**
     * 문제를 풀고 맞았을 경우 포인트를 얻는 메서드
     *
     * @param point : 획득한 포인트
     * @return : 갱신된 포인트
     */
    public int earnPoints(int point) {
        return this.point += point;
    }
}
