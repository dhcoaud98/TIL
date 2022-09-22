package com.ssafy.prosn.security;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.ssafy.prosn.domain.user.LocalUser;
import lombok.Getter;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import java.util.Collection;

/**
 * created by seongmin on 2022/07/27
 */
@Getter
@Slf4j
public class UserDetailsImpl implements UserDetails {
    private Long id;
    private String userId;
    private String email;
    private String name;
    @JsonIgnore
    private String password;
    private Integer point;

    public UserDetailsImpl(Long id, String userId, String email, String name, String password, Integer point) {
        log.info("로그 UserDetailsImpl");
        this.id = id;
        this.userId = userId;
        this.email = email;
        this.name = name;
        this.password = password;
        this.point = point;
    }

    public static UserDetailsImpl build(LocalUser user) {
        log.info("로그 UserDetailsImpl build");
        return new UserDetailsImpl(
                user.getId(),
                user.getUserId(),
                user.getEmail(),
                user.getName(),
                user.getPassword(),
                user.getPoint()
        );
    }

    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        return null;
    }

    @Override
    public String getPassword() {
        return password;
    }

    @Override
    public String getUsername() {
        return userId;
    }

    @Override
    public boolean isAccountNonExpired() {
        return true;
    }

    @Override
    public boolean isAccountNonLocked() {
        return true;
    }

    @Override
    public boolean isCredentialsNonExpired() {
        return true;
    }

    @Override
    public boolean isEnabled() {
        return true;
    }
}
