<template>
   <div>
      <!-- 2022.07.25. 회원 로그인정보 입력란 (남성은) -->
      <!-- 0805 임지민
      - 아직 계정이 없으신가요? 와 아이디/비번 찾기 사이에 간격 늘리기
      - 회원가입 hover시 보라색 text와 보라색 underline 뜨도록 수정
      - 회원가입 글자 bold로 바꿈
     -->
    
    <v-container class="mt-5">
      <v-form ref="form" v-model="valid" lazy-validation @submit.prevent="login" class="ma-0 pa-0">
        <v-row no-gutters>
          <v-col cols="12" md="9" class="ma-0 px-1">
            <!-- 네임룰 추후 설정 필요 -->
            <!-- ID 입력란 -->
            <v-text-field v-model="credentials.userId" :rules="idRules" :counter="12" name="userId" label="아이디" required></v-text-field>
            <!-- PASSWORD 입력란 -->
            <v-text-field
            v-model="credentials.password"
            :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="show ? 'text' : 'password'"
            name="input-10-2"
            label="비밀번호"
            hint="At least 8 characters"
            value=""
            class="input-group--focused"
            @click:append="show = !show"
            ></v-text-field>
          </v-col>

          <!-- 로그인 버튼 -->
          <v-col cols="12" md="3" class="ma-0 px-1">
            <v-btn :disabled="!valid" type="submit" color="#CCA5FE" class="rounded-xl white--text my-0 py-3 mt-3" height="80%" width="100%"><h3>로그인</h3></v-btn>
          </v-col>
        </v-row>
        <v-row class="mt-0 py-0 px-1">
          <p class="font-parent-mid red--text font-weight-bold">{{warningText}}</p>
        </v-row>
      </v-form>

      <!-- 회원가입/아이디찾기/비밀번호찾기 --> 
      <v-row class="mt-5">
        <v-col cols="12" class=" d-flex justify-center pa-0">
          <p>아직 계정이 없으신가요?<router-link to="/signup" class="purple--text text--lighten-2 text-decoration-none hover-login ml-3 font-weight-bold black--text">회원가입</router-link></p>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" class="d-flex justify-space-around pa-0">
          <a href="" class="black--text">아이디 찾기</a>
          <p>|</p>
          <a href="" class="black--text">비밀번호 찾기</a>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
//   export default {
//     // 2022.07.25. 아이디 (남성은)
//     data: () => ({
//       valid: true,
//       id: '',
//       // nameRules: [
//       //   v => !!v || 'Name is required',
//       //   v => (v && v.length <= 10) || 'Name must be less than 10 characters',
//       // ],
//     }),

//     // 2022.07.25. 비밀번호 (남성은)
//     data () {
//       return {
//         show: false,
//         password: '',
//         rules: {
//           required: value => !!value || 'Required.',
//           min: v => v.length >= 8 || 'Min 8 characters',
//         },
//       }
//     },

//     // 2022.07.25. 로그인 버튼 (남성은)
//     methods: {
//       validate () {
//         this.$refs.form.validate()
//       },
//     },
//   }

import axios from 'axios';
import drf from '@/api/drf';
import { mapState, mapActions } from 'vuex';
const accountStore = 'accountStore';

  export default {
    // 2022.07.25. 아이디 (남성은)
    data: () => ({
      valid: true,
      credentials : {
        userId: '',
        password: ''
      },
      show: false,
      rules: {
        required: value => !!value || 'Required.',
        min: v => v.length >= 8 || 'Min 8 characters',
      },
      id: '',
      idRules: [
          v => !!v || '아이디는 필수 입력값입니다.',
          v => (v && v.length <= 12) || '아이디는 12자 이하로 입력하세요',
      ],
      warningText: null,
    }),

   // 2022.07.25. 로그인 버튼 (남성은)
   methods: {
      validate() {
         this.$refs.form.validate();
      },
      // ...mapActions(['login'])
      login() {
         // axios.post(drf.accounts.login())
         // .then(({res}) => {
         //   console.log(res)
         // })
         axios({
            url: drf.accounts.login(),
            method: 'post',
            data: this.credentials,
         })
            .then((res) => {
               console.log('res = ', res.data);
              //  console.log('accessToken = ', res.data.accessToken);
              //  console.log('refreshToken = ', res.data.refreshToken);
              //  console.log('expire : ', res.data.tokenExpiresIn);
               let grantType = res.data.grantType.replace(
                  res.data.grantType.charAt(0),
                  res.data.grantType.charAt(0).toUpperCase()
               );
               console.log('grantType:', grantType);
               this.$store.dispatch(
                  'saveToken',
                  grantType + ' ' + res.data.accessToken
               );
               this.$store.dispatch('saveRefreshToken', res.data.refreshToken);
               this.$store.dispatch('saveExpiresIn', res.data.tokenExpiresIn);

               this.$store.dispatch('saveName', res.data.name);
               this.$store.dispatch('saveId', res.data.id);
               this.$router.push({ path: '/' });
               // const token = res.data.key
               // dispatch('saveToken', token)
               // dispaxtch('fetchCurrentUser')
            })
            .catch((err) => {
              //  console.log('에러');
              console.log(err);
              // 아이디, 비번을 잘못 입력하면 로그인창 하단에 경고메시지 띄우기 0814 임지민
               if (err.request.status === 403){
                this.warningText = '아이디 혹은 비밀번호를 확인해주세요'
                // console.log(this.warningText)
               };
              //  if (err.)
               // 401뜨면 alert창 띄워주기 0814 임지민
               
            });
      },
      // event () {
      //   this.$router.push({ path: '/' })
      // }
   },
};
</script>

<style></style>