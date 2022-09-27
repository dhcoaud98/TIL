# 05.18

## VUE응용

[TOC]

### 1. Vue router

#### 1. 404 page

1. Vue Router에 등록되지 않은 routes일 경우

   ex) no-shch-routes

   vue router는 routes 배열에서 순차적으로 URL을 검색

   등록되지 않은 모든(*) URL은 /404로 redirection

2. Vue Router에는 등록되어 있지만, 서버에서 해당 리소스를 찾을 수 없는경우

   ex) /articles/987654321

#### 2. Navigation Guard

Navigation Guard 설정

 (이전 페이지에서 있던 에러 메시지 삭제)

 로그인(Authentication)이 필요 없는 route 이름들 저장(/login, /signup)

0. router 에서 이동 감지

1. 현재 이동하고자 하는 페이지가 로그인이 필요한지 확인

2. 로그인이 필요한 페이지인데 로그인이 되어있지 않다면

  로그인 페이지(/login)로 이동

3. 로그인이 되어 있다면

  원래 이동할 곳으로 이동

4. 로그인이 되어있는데 /login, /signup 페이지로 이동한다면

  메인 페이지(/)로 이동

### 2. Vuex

#### 2. Vuex modules & namespace
