<template>
  <div>
    <!-- 2022.07.25. 소셜로그인 (남성은) -->
    <v-container class="px-0">
      <v-row>
        <v-col cols="12" class="d-flex justify-center" @click="KakaoLogin()">
          <v-btn elevation="2" class="pa-0 rounded-lg" height="60">
            <img id="kakao-login" src="@/assets/kakao_login.png" alt="...">
          </v-btn>
        </v-col>
        <!-- <v-col cols="12" class="d-flex justify-center" @click="GoogleLogin()">
          <v-btn id='google-login' color="white" class="justify-space-between rounded-lg">
            <img src="@/assets/google_logo.png" alt="google_logo" id="google-logo">
            <img src="@/assets/google_text.png" alt="google_text">
            <div></div>
          </v-btn>
        </v-col> -->
        <v-col cols="12" class="d-flex justify-center" @click="naverLogin()">
          <v-btn id='naver-login' color="#03C75A" class="justify-space-between ps-1 rounded-lg">
            <img src="@/assets/naver_logo.png" alt="naver_logo" id="naver-logo">
            <img src="@/assets/naver_text.png" alt="naver_text" id="naver-text" class="me-3">
            <div></div>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'SocialLogin',
    methods: {
      KakaoLogin() {
        console.log('카카오 로그인 시도')
        window.location.href = "https://kauth.kakao.com/oauth/authorize?client_id=6ed2b72fdabc00402337b642bd55e31c&redirect_uri=http://i7a705.p.ssafy.io:8081/login/oauth2/code/kakao&response_type=code"
      },
      GoogleLogin () {
        console.log('구글 로그인 시도')
        window.location.href = "https://accounts.google.com/o/oauth2/v2/auth?scope=https://www.googleapis.com/auth/drive.metadata.readonly&response_type=code&redirect_uri=http://i7a705.p.ssafy.io:8081/login/oauth2/code/google&client_id=295331690529-n55t5j7cu200lok9c151d25nrfr2vv6g.apps.googleusercontent.com"
      },
      naverLogin () {
        console.log('네이버 로그인 시도')
        window.location.href = "https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id=LwPwQBNyhqiw3dYPZ4Av&state=state&redirect_uri=http://i7a705.p.ssafy.io:8081/login/oauth2/code/naver"
      }
    }

}
</script>

<style>
#kakao-login {
  width: 400px;
}
#google-login {
  height: 60px;
  width: 400px;
}
#naver-login {
  height: 60px;
  width: 400px;
}
#google-logo {
  height: 27px;
  width: 27px;
}
#naver-logo {
  height: 50px;
  width: 50px;
}
#naver-text {
  height: 20px;
}
</style>
