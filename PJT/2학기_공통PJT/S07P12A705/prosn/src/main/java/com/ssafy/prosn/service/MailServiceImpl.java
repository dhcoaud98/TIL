package com.ssafy.prosn.service;

import lombok.RequiredArgsConstructor;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.Random;

/**
 * created by yeomyeong on 2022/08/04
 * updated by yeomyeong on 2022/08/07
 */
@Service
@RequiredArgsConstructor
public class MailServiceImpl implements MailService {
    private final JavaMailSender javaMailSender;
    private final PasswordEncoder passwordEncoder;

    @Override
    public String sendMail(String emailTo) {

        // SimpleMailMessage (단순 텍스트 구성 메일 메시지 생성할 때 이용)
        SimpleMailMessage simpleMessage = new SimpleMailMessage();

        // 수신자 설정
        simpleMessage.setTo(emailTo);
        simpleMessage.setFrom("prosnteam@naver.com");

        // 메일 제목
        simpleMessage.setSubject("[PROSN] 임시 비밀번호 발급");

        // 메일 내용
        String randPassword = randPassword();
        simpleMessage.setText("임시비밀번호: " + randPassword);

        // 메일 발송
        javaMailSender.send(simpleMessage);

        //DB 반영할 str
        return passwordEncoder.encode(randPassword);
    }

    private String randPassword() {
        int leftLimit = 48; // 숫자 '0'
        int rightLimit = 122; // 'z'
        int targetStringLength = 6; //6자리
        Random random = new Random();

        return random.ints(leftLimit,rightLimit + 1)
                .filter(i -> (i <= 57 || i >= 65) && (i <= 90 || i >= 97))
                .limit(targetStringLength)
                .collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append)
                .toString();
    }
}