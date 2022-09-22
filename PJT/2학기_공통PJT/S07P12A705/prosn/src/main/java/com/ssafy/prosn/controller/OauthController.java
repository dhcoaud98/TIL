package com.ssafy.prosn.controller;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.nimbusds.jose.shaded.json.JSONObject;
import com.ssafy.prosn.domain.user.SocialUser;
import com.ssafy.prosn.dto.SocialLoginResponseDto;
import com.ssafy.prosn.oauth.*;
import com.ssafy.prosn.repository.user.SocialUserRepository;
import com.ssafy.prosn.repository.user.UserRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.*;
import org.springframework.http.client.ClientHttpResponse;
import org.springframework.http.client.HttpComponentsClientHttpRequestFactory;
import org.springframework.http.converter.json.MappingJackson2HttpMessageConverter;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.DefaultResponseErrorHandler;
import org.springframework.web.client.RestTemplate;

import java.io.IOException;
import java.util.HashMap;

import static org.hibernate.cfg.AvailableSettings.URL;

@RestController
@Slf4j
@RequiredArgsConstructor
@RequestMapping("/login/oauth2/code")
public class OauthController {
    private final UserRepository userRepository;
    private final SocialUserRepository socialUserRepository;

    //    private final OauthService oauthService;
//    private final SocialOauth socialOauth;
//
//    /**
//     * 플랫폼 타입
//     * */
//    @GetMapping("/{platform}")
//    public void platform (@PathVariable(name = "platform") Platform platform) {
//        log.info("controller social login platform: " + platform);
//        oauthService.request(platform);
//    }
//
//    /**
//     * code = 인가 코드
//     * */
//    @GetMapping("/{platform}/callback")
//    public SocialLoginResponseDto callback(@PathVariable(name = "platform") Platform platform, @RequestParam(name = "code") String code) {
//        log.info("controller social login code: " + code);
//        String access_Token = oauthService.requestAccessToken(platform, code);
//        SocialLoginResponseDto socialLoginResponseDto = socialOauth.getUserInfo(access_Token);
//        return socialLoginResponseDto;
//    }
    @GetMapping(value = "/kakao")
    public SocialLoginResponseDto kakaoOauthRedirect(@RequestParam("code") String code,
                                                     @Value("${spring.security.oauth2.client.registration.kakao.client-id}") String client_id,
//                                 @Value("${spring.security.oauth2.client.registration.kakao.client-secret}") String client_secret,
                                                     @Value("${spring.security.oauth2.client.registration.kakao.authorization-grant-type}") String authorization_grant_type,
                                                     @Value("${spring.security.oauth2.client.registration.kakao.redirect-uri}") String redirect_uri) {
        System.out.println("code=" + code);
        RestTemplate rt = new RestTemplate();
        rt.setRequestFactory(new HttpComponentsClientHttpRequestFactory());
        rt.setErrorHandler(new DefaultResponseErrorHandler() {
            @Override
            public boolean hasError(ClientHttpResponse response) throws IOException {
                HttpStatus statusCode = response.getStatusCode();
                return statusCode.series() == HttpStatus.Series.SERVER_ERROR;
            }
        });
        HttpHeaders headers = new HttpHeaders();
        headers.add("Content-type", "application/x-www-form-urlencoded;charset=utf-8");

        MultiValueMap<String, String> params = new LinkedMultiValueMap<>();
        params.add("grant_type", authorization_grant_type);
        params.add("client_id", client_id);
//    params.add("client_secret", client_secret);
        params.add("redirect_uri", redirect_uri);
        params.add("code", code);

        HttpEntity<MultiValueMap<String, String>> kakaoRequest = new HttpEntity<>(params, headers);

        ResponseEntity<String> response = rt.exchange(
                "https://kauth.kakao.com/oauth/token",
                HttpMethod.POST,
                kakaoRequest,
                String.class
        );

        ObjectMapper objectMapper = new ObjectMapper();
        KakaoOauthParams kakaoOauthParams = null;
        try {
            kakaoOauthParams = objectMapper.readValue(response.getBody(), KakaoOauthParams.class);
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }

        HttpHeaders headers1 = new HttpHeaders();
        headers1.add("Authorization", "Bearer " + kakaoOauthParams.getAccess_token());
        headers1.add("Content-type", "application/x-www-form-urlencoded;charset=utf-8");

        HttpEntity<HttpHeaders> kakaoRequest1 = new HttpEntity<>(headers1);

        ResponseEntity<String> profileResponse = rt.exchange(
                "https://kapi.kakao.com/v2/user/me",
                HttpMethod.POST,
                kakaoRequest1,
                String.class
        );
        log.info("profileResponse.toString() ={}", profileResponse.toString());

        KakaoProfile kakaoProfile = null;
        try {
            kakaoProfile = objectMapper.readValue(profileResponse.getBody(), KakaoProfile.class);
            System.out.println("oauth controller kakaoProfile: " + kakaoProfile);
        } catch (JsonProcessingException e) {
            log.info("캐치 : {}", e.getMessage());
            e.printStackTrace();
        }
        Long id = kakaoProfile.getId();
        log.info("id: " + id);
        SocialLoginResponseDto socialLoginResponseDto = SocialLoginResponseDto.builder()
                .oauthId(String.valueOf(kakaoProfile.getId()))
                .platform(Platform.KAKAO)
                .email(kakaoProfile.getKakao_account().getEmail())
                .name(kakaoProfile.getKakao_account().getProfile().getNickname())
                .accessToken(kakaoOauthParams.getAccess_token())
                .refreshToken(kakaoOauthParams.getRefresh_token())
                .build();
        log.info("kakao 유저 인포" + socialLoginResponseDto);


        if (socialUserRepository.findByOauthId(socialLoginResponseDto.getOauthId()).isPresent()) {
            return socialLoginResponseDto;
        } else {
            SocialUser user = userRepository.save(SocialUser.builder()
                    .oauthId(socialLoginResponseDto.getOauthId())
                    .platform(socialLoginResponseDto.getPlatform())
                    .email(socialLoginResponseDto.getEmail())
                    .name(socialLoginResponseDto.getName())
                    .build());
        }


        return socialLoginResponseDto;
    }

    @GetMapping("/google")
    public SocialLoginResponseDto googleOAuthRedirect(@RequestParam String code,
                                                      @Value("${spring.security.oauth2.client.registration.google.client-id") String client_id,
                                                      @Value("${spring.security.oauth2.client.registration.google.client-secret}") String client_secret,
                                                      @Value("${spring.security.oauth2.client.registration.google.authorization_code}") String authorization_grant_type,
                                                      @Value("${spring.security.oauth2.client.registration.google.redirect_uri}") String redirect_uri) {

        RestTemplate rt = new RestTemplate();
        rt.setRequestFactory(new HttpComponentsClientHttpRequestFactory());
        rt.setErrorHandler(new DefaultResponseErrorHandler() {
            public boolean hasError(ClientHttpResponse response) throws IOException {
                HttpStatus statusCode = response.getStatusCode();
                return statusCode.series() == HttpStatus.Series.SERVER_ERROR;
            }
        });
        HttpHeaders headers = new HttpHeaders();
        headers.add("Content-Type", "application/x-www-form-urlencoded");

        MultiValueMap<String, String> params = new LinkedMultiValueMap<>();
        params.add("client_id", client_id);
        params.add("client_secret", client_secret);
        params.add("code", code);
        params.add("grant_type", authorization_grant_type);
        params.add("redirect_uri", redirect_uri);

        HttpEntity<MultiValueMap<String, String>> accessTokenRequest = new HttpEntity<>(params, headers);

        ResponseEntity<String> accessTokenResponse = rt.exchange(
                "https://oauth2.googleapis.com/token",
                HttpMethod.POST,
                accessTokenRequest,
                String.class
        );
        log.info("oauth controller google token: " + accessTokenResponse);
        ObjectMapper objectMapper = new ObjectMapper();
        GoogleOauthParams googleOauthParams = null;
        try {
            googleOauthParams = objectMapper.readValue(accessTokenResponse.getBody(), GoogleOauthParams.class);
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
        log.info("oauth controller google oauth params: " + googleOauthParams);
        HttpHeaders headers1 = new HttpHeaders();
        headers1.add("Authorization", "Bearer " + googleOauthParams.getAccess_token());

        HttpEntity profileRequest = new HttpEntity(headers1);

        ResponseEntity<String> profileResponse = rt.exchange(
                "https://oauth2.googleapis.com/tokeninfo?access_token=" + googleOauthParams.getId_token(),
                HttpMethod.GET,
                profileRequest,
                String.class
        );

        log.info("oauth controller google profile: " + profileResponse);
        HashMap<String, String> profileParams = null;
        try {
            profileParams = objectMapper.readValue(profileResponse.getBody(), HashMap.class);
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }

        //google refresh token 안 넘어옴
        SocialLoginResponseDto socialLoginResponseDto = SocialLoginResponseDto.builder()
                .oauthId(profileParams.get("id"))
                .platform(Platform.GOOGLE)
                .email(profileParams.get("email"))
                .name(profileParams.get("name"))
                .accessToken(googleOauthParams.getAccess_token())
                .build();
        log.info("google 유저 인포" + socialLoginResponseDto);

        if (socialUserRepository.findByOauthId(socialLoginResponseDto.getOauthId()).isPresent()) {
            return socialLoginResponseDto;
        } else {
            SocialUser user = userRepository.save(SocialUser.builder()
                    .oauthId(socialLoginResponseDto.getOauthId())
                    .platform(socialLoginResponseDto.getPlatform())
                    .email(socialLoginResponseDto.getEmail())
                    .name(socialLoginResponseDto.getName())
                    .build());
        }

        return socialLoginResponseDto;
    }

    @GetMapping("/naver")
    public SocialLoginResponseDto naverOAuthRedirect(@RequestParam String code, @RequestParam String state,
                                                     @Value("${spring.security.oauth2.client.registration.naver.client-id}") String client_id,
                                                     @Value("${spring.security.oauth2.client.registration.naver.client-secret}") String client_secret,
                                                     @Value("${spring.security.oauth2.client.registration.naver.authorization-grant-type}") String authorization_grant_type) {

        RestTemplate rt = new RestTemplate();

        HttpHeaders accessTokenHeaders = new HttpHeaders();
        accessTokenHeaders.add("Content-type", "application/x-www-form-urlencoded");

        MultiValueMap<String, String> accessTokenParams = new LinkedMultiValueMap<>();
        accessTokenParams.add("grant_type", authorization_grant_type);
        accessTokenParams.add("client_id", client_id);
        accessTokenParams.add("client_secret", client_secret);
        accessTokenParams.add("code", code);
        accessTokenParams.add("state", state);

        HttpEntity<MultiValueMap<String, String>> accessTokenRequest = new HttpEntity<>(accessTokenParams, accessTokenHeaders);

        ResponseEntity<String> accessTokenResponse = rt.exchange(
                "https://nid.naver.com/oauth2.0/token",
                HttpMethod.POST,
                accessTokenRequest,
                String.class
        );

        ObjectMapper objectMapper = new ObjectMapper();
        NaverOauthParams naverOauthParams = null;
        try {
            naverOauthParams = objectMapper.readValue(accessTokenResponse.getBody(), NaverOauthParams.class);
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }

        HttpHeaders profileRequestHeader = new HttpHeaders();
        profileRequestHeader.add("Authorization", "Bearer " + naverOauthParams.getAccess_token());

        HttpEntity<HttpHeaders> profileHttpEntity = new HttpEntity<>(profileRequestHeader);

        ResponseEntity<String> profileResponse = rt.exchange(
                "https://openapi.naver.com/v1/nid/me",
                HttpMethod.POST,
                profileHttpEntity,
                String.class
        );

        NaverProfile naverProfile = null;
        try {
            naverProfile = objectMapper.readValue(profileResponse.getBody(), NaverProfile.class);
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }

        SocialLoginResponseDto socialLoginResponseDto = SocialLoginResponseDto.builder()
                .oauthId(naverProfile.getResponse().getId())
                .platform(Platform.NAVER)
                .email(naverProfile.getResponse().getEmail())
                .name(naverProfile.getResponse().getName())
                .accessToken(naverOauthParams.getAccess_token())
                .refreshToken(naverOauthParams.getRefresh_token())
                .build();
        log.info("naver 유저 인포" + socialLoginResponseDto);

        if (socialUserRepository.findByOauthId(socialLoginResponseDto.getOauthId()).isPresent()) {
            return socialLoginResponseDto;
        } else {
            SocialUser user = userRepository.save(SocialUser.builder()
                    .oauthId(socialLoginResponseDto.getOauthId())
                    .platform(socialLoginResponseDto.getPlatform())
                    .email(socialLoginResponseDto.getEmail())
                    .name(socialLoginResponseDto.getName())
                    .build());
        }

        return socialLoginResponseDto;
    }
}
