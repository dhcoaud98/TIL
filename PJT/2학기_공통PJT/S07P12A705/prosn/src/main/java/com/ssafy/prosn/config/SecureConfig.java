package com.ssafy.prosn.config;

import com.ssafy.prosn.repository.user.LocalUserRepository;
import com.ssafy.prosn.security.*;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.authentication.configuration.AuthenticationConfiguration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;
import org.springframework.stereotype.Component;

/**
 * created by seongmin on 2022/07/20
 * created by seongmin on 2022/07/27
 */
@RequiredArgsConstructor
@Configuration
@EnableWebSecurity
@Component
public class SecureConfig {

    private final JwtUtils jwtUtils;
//    private final AuthEntryPointJwt authEntryPointJwt;
    private final AuthAccessDenieHandler authAccessDenieHandler;
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }


    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
                .httpBasic().disable()
                .cors().and().csrf().disable()
                .formLogin().disable()
                .sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS)

                .and()
                .exceptionHandling()
//                .authenticationEntryPoint(authEntryPointJwt)
                .accessDeniedHandler(authAccessDenieHandler)

                .and()
                .authorizeRequests()
                .antMatchers("/api/**","/v2/api-docs", "/configuration/**", "/swagger*/**", "/webjars/**", "/swagger-ui.html", "/swagger-resources/**", "/login/**").permitAll()
                .anyRequest().authenticated()

                .and()
                .apply(new JwtSecurityConfig(jwtUtils));

        return http.build();
    }
}
