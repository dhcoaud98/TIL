package com.ssafy.prosn.config;

import com.ssafy.prosn.domain.post.Tag;
import com.ssafy.prosn.repository.post.tag.TagRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import java.util.ArrayList;
import java.util.List;

@Component
@RequiredArgsConstructor
public class DataInit {
    private final TagRepository tagRepository;

    @PostConstruct
    public void init() {
        List<Tag> all = tagRepository.findAll();
        if (all.size() == 0) {
            List<Tag> tags = new ArrayList<>();
            tags.add(new Tag("NW", "네트워크"));
            tags.add(new Tag("OS", "운영체제"));
            tags.add(new Tag("DS", "자료구조"));
            tags.add(new Tag("DB", "데이터베이스"));
            tags.add(new Tag("AL", "알고리즘"));
            tags.add(new Tag("OOP", "객체지향"));
            tags.add(new Tag("PL", "프로그래밍 언어"));
            tags.add(new Tag("CS", "컴퓨터 구조"));
            tags.add(new Tag("TC", "기술동향"));
            tags.add(new Tag("SC", "보안"));
            tags.add(new Tag("ETC", "기타"));
            tagRepository.saveAll(tags);
        }

    }
}
