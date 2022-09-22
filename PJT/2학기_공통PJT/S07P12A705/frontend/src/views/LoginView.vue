<template>
  <!-- 2022.07.22 로그인 화면 구성요소들 (남성은) -->
  <!-- 0805 임지민 
    - 로고, 서비스 설명 부분 grey lighten-4 처리   
    - 가운데 정렬보다 왼쪽 정렬이 깔끔한 것 같아서 바꿨는 데 제 소견일 뿐 화면 보고 이전이 나오면 바꿔도 됩니당
    - prosn 로고가 큰 것 같아 사이즈 조금 작게 수정함   
    - 로고에 홈화면 연결   
  -->
  <v-container class="d-flex align-center grey lighten-4 px-0" height="100%">
    <v-row id="login-page" class="d-flex justify-center px-0">
      <!-- 로그인 -->
      <v-col class="col-12 col-sm-10 col-md-6 rounded-lg d-flex flex-column align-center justify-center white pa-0 mt-3">
        <v-row class="mt-4">
          <v-col class="text-center">
            <router-link to="/" class="d-inline-block">
              <v-img src="../assets/prosn_logo.png" max-width="200px" max-height="80px"></v-img>
            </router-link>
          </v-col>
        </v-row>

        <div class="mt-8">
          <p class="font-parent-lar display-1">L O G I N</p>
        </div>

        <!-- 로컬 로그인 -->
        <v-row class="px-5 ma-0 mb-10">
          <v-col class="mx-5">
            <local-login></local-login>

            <!-- 소셜 로그인 -->
            <social-login></social-login>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container></template>

<script>
import LocalLogin from '@/components/LocalLogin.vue'
import SocialLogin from '@/components/SocialLogin.vue'

export default {
  name: 'LoginView',
  data: () => ({
    //
  }),
  components : {
    LocalLogin,
    SocialLogin,
  }
};
</script>

<style>
html {
  background-color: #f9f9f9;
}
</style>
