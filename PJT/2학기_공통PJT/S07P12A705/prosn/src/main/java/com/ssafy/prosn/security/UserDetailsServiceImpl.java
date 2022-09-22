package com.ssafy.prosn.security;

import com.ssafy.prosn.domain.user.LocalUser;
import com.ssafy.prosn.repository.user.LocalUserRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import java.util.Collections;

/**
 * created by seongmin on 2022/07/27
 * updated by seongmin on 2022/07/28
 */
@Service
@Slf4j
@RequiredArgsConstructor
public class UserDetailsServiceImpl implements UserDetailsService {


    private final LocalUserRepository localUserRepository;

    @Override
    public UserDetails loadUserByUsername(String userId) throws UsernameNotFoundException {
        log.info("로그 UserDetailServiceImpl 시작");

        return localUserRepository.findByUserId(userId)
                .map(this::createUserDetails)
                .orElseThrow(() -> new UsernameNotFoundException(userId + " 을 DB에서 찾을 수 없습니다"));
//        LocalUser user = localUserRepository.findByUserId(userId)
//                .orElseThrow(() -> new UsernameNotFoundException("찾을 수 없는 아이디 : " + userId));
//        log.info("로그 UserDetailServiceImpl 끝");
//        return UserDetailsImpl.build(user);
    }

    private UserDetails createUserDetails(LocalUser user) {
        GrantedAuthority grantedAuthority = new SimpleGrantedAuthority(user.getAuthority().toString());

        return new User(
                String.valueOf(user.getId()),
                user.getPassword(),
                Collections.singleton(grantedAuthority)
        );
    }

}
