# 05.13

## pjt

[TOC]

### 0. 배포

* 소프트 웨어 전개는 소프트웨어 시스템을 사용할 수 있도록 만드는 모든 활동
* 소프트웨어 배포는 최종 사용자에게 소프트웨어를 전달하는 과정이다.

1. 무엇을? 

   * Django : 서버 컴퓨터에서 요청과 응답을 처리할 프로그램

2. 언제?

   * 개발 : 분석, 계획, 설계, 개발, 테스트
   * 운영: 배포(배치), 운영

3. 누가, 어디에?

   * SW 제공자가 사용자 컴퓨터에
   * CD나 저장 버튼으로 설치
   * 서버에서 사용(Web App)

4. 어떻게?

   * git push -> remote repo -> git pull

   * git push -> remote repo -> CI server(test, Build, Deploy)

* SW를 개발하는 이유?

  : SW 배포

### 1. Server 배포

* Flow
  * Client - Web server - WSI - Application Server

### 2. Client 배포
