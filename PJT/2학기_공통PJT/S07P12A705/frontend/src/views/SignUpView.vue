<template>
  <!-- 2022.07.22 로그인 화면 구성요소들 (남성은) -->
  <!-- 0805 임지민 
    - 로고, 서비스 설명 부분 grey lighten-4 처리   
    - 가운데 정렬보다 왼쪽 정렬이 깔끔한 것 같아서 바꿨는 데 제 소견일 뿐 화면 보고 이전이 나오면 바꿔도 됩니당
    - prosn 로고가 큰 것 같아 사이즈 조금 작게 수정함   
    - 로고에 홈화면 연결   
  -->
  <v-container class="d-flex align-center grey lighten-4 px-0" height="100%">
    <v-row class="d-flex justify-center px-0">
      <!-- 회원가입 -->
      <v-col class="col-12 col-sm-10 col-md-6 rounded-lg d-flex flex-column align-center justify-center white pa-0 mt-3">
        <v-row class="mt-4">
          <v-col class="text-center">
            <router-link to="/" class="d-inline-block">
              <v-img src="../assets/prosn_logo.png" max-width="200px" max-height="80px"></v-img>
            </router-link>
          </v-col>
        </v-row>

        <div class="mt-8">
          <p class="font-parent-lar display-1">S I G N U P</p>
        </div>

        <!-- 정보작성 -->
        <v-row class="px-0 ma-0 mb-10">
          <v-col class="mx-5 pa-0">
            <v-container class="mt-5 px-0" width="100%">
              <v-form ref="form" class="ma-0 pa-0" @submit.prevent="submitSignUp">
                
                <!-- 각 text field 내부 속성들은 추후에 수정하기 -->

                <!-- 아이디 필드 -->
                <v-row no-gutters>
                  <v-col cols="12" md="9" class="ma-0 pa-0">
                    <v-text-field v-model="credentials.userId" :rules="idRules" :counter="12" name="userId" label="아이디" required ></v-text-field>
                  </v-col>
                  <v-col cols="12" md="3" class="ma-0 pa-0">
                    <v-btn @click="idDoubleCheck" color="#d9d9d9" class="rounded-xl grey--text mt-3 id-double-check" width="100%">
                      <p class="ma-0 black--text">중복확인</p>
                    </v-btn>
                  </v-col>
                </v-row>

                <!-- 
                    비밀번호 필드
                    - 힌트: 최소 n자 이상(hint)
                    - 8자 이상 입력되지 않으면 빨간 텍스트가 뜸
                    - 눈 모양 아이콘 누르면 작성한 비번이 보였다 안보였다 함
                -->
                <v-row class="pa-0">
                  <v-col class="pa-0">
                    <v-text-field v-model="credentials.password" 
                        :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'" 
                        :rules="[rules.required, rules.min]" 
                        :type="show1 ? 'text' : 'password'" 
                        name="password1" label="비밀번호" hint="최소 8자 이상 입력하세요" 
                        counter 
                        @click:append="show1 = !show1"
                    ></v-text-field>
                  </v-col>
                </v-row>

                <!-- 비밀번호 확인 필드-->
                <v-row class="pa-0">
                  <v-col class="pa-0">
                    <v-text-field
                        v-model="credentials.passwordCheck"
                        :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                        :rules="[rules.required, checkPassword]"    
                        :type="show2 ? 'text' : 'password'"
                        name="password2"
                        label="비밀번호 확인"
                        counter
                        @click:append="show2 = !show2"
                    ></v-text-field>
                  </v-col>
                </v-row>

                <!-- 사용자 이름 필드 -->
                <v-row class="pa-0">
                  <v-col class="pa-0">
                    <v-text-field v-model="credentials.name" :rules="nameRules" :counter="8" label="사용자 이름" name="name" required></v-text-field>
                  </v-col>
                </v-row>

                <v-row class="mb-2 pa-0">
                  <v-col class="pa-0">
                    <v-text-field v-model="credentials.email" label="이메일" name="email" :rules="emailRules" required></v-text-field>
                  </v-col>
                </v-row>
                            
                <!-- 회원가입 버튼: 유효성 검사 + submit -->
                <v-row class="mt-5 mb-1 justify-center pa-0">
                  <!-- 아래에 submitSignup 메서드를 정의; axios로 db에 사용자 정보를 저장하기 -->
                  <v-col cols="12" class="pa-0">
                    <v-btn rounded :disabled="!valid" @click="validate();" type="submit" class="col-12 my-2 d-flex justify-space-between" height="45px">
                      <img src="@/assets/prosn_logo_sm.png" alt="..." class="signin-logo">
                      <p class="pa-0 ma-0 font-weight-medium signin-text purple--text text--lighten-2">JOIN US</p>
                      <div class="pa-2"></div>
                    </v-btn>
                  </v-col>
                </v-row>
              </v-form>
            </v-container>
          </v-col>
        </v-row>

        <!-- 이미 계정이 있으신가요?  -->
        <v-row class="mt-0 mb-4">
          <v-col cols="12" class=" d-flex justify-center pa-0">
            <p>이미 계정이 있으신가요?<router-link to="/login" class="purple--text text--lighten-2 text-decoration-none hover-login ml-3 font-weight-bold black--text">로그인</router-link></p>
        </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// import { mapActions } from 'vuex'
import axios from 'axios'
import drf from '@/api/drf'

export default {
    name: 'SignUpView',
    data: () => ({
        valid: true,
        credentials : {
            userId: '',
            name: '',
            password: '',
            email: '',
        },
        id: '',
        idRules: [
            v => !!v || '아이디는 필수 입력값입니다.',
            v => (v && v.length <= 12) || '아이디는 12자 이하로 입력하세요',
        ],
        email: '',
        emailRules: [
            v => !!v || '이메일은 필수 입력값입니다.',
            v => /.+@.+\..+/.test(v) || '이메일이 유효하지 않습니다.',
        ],
        name: '',
        nameRules: [
            v => !!v || '사용자 이름은 필수 입력값입니다.',
            v => (v && v.length <= 12) || '사용자 이름은 10자 이하로 입력하세요',
        ],
        show1: false,
        show2: false,
        password: '',
        passwordCheck: '',
        rules: {
          required: value => !!value || '필수 입력값입니다.',
          min: v => v.length >= 8 || '최소 8자 이상을 입력하세요',
        },
        idDuplicateFlag : false
    }),

    methods: {
        // ...mapActions(['accounts/signUp']),

        reset () {
            this.$refs.form.reset()
        },

        // 비밀번호 일치 여부
        checkPassword() {
            if (this.password === this.passwordCheck) {
                return true
            } else {
                return '비밀번호가 일치하지 않습니다.'
            }
        },

        // id 중복확인 (0815 오채명)
        idDoubleCheck () {
          // console.log(this.credentials.userId)
          axios({
            url: drf.api + 'user/' + 'id/' + 'check' ,
            method: 'post',
            data: {
              uid : this.credentials.userId
            }
          })
          .then(res =>{
            this.idDuplicateFlag = true;
            alert('사용가능한 아이디입니다.')
          })
          .catch(err =>{
            if (err.response.status === 409){
              alert('이미 사용중인 아이디 입니다.')
            }
          })
        },

        validate () {
            this.$refs.form.validate()
        },
        submitSignUp () {
            console.log('axios = ', axios)
            // console.log('submit') --- ok
            // submit했을 때 axios로 db에 사용자 정보를 저장해주면 된다.
            // console.log("클릭")
            // console.log("credentials = ", this.credentials)
            if(!this.idDuplicateFlag) {
              alert("아이디 중복 체크를 해주세요.")
            } else {
              axios({
                url: drf.accounts.join(),
                method: 'post',
                data: this.credentials
              })
              .then(res => {
                  console.log("res = ",res);
                  // 0810 오채명 : 회원가입은 grantType이 없기 때문에 axios할 때 넘겨주면 안됩니다.
                  // 회원가입이 완료되면 바로 로그인을 시켜주기 위함
                  this.$store.dispatch('saveToken', res.data.accessToken)
                  this.$store.dispatch('saveName', res.data.name)
                  
                  // 회원가입이 완료되면 메인 페이지로 이동
                  this.$router.push({ path: '/'})              
              })
              .catch(err =>{
                  console.error(err)
                  if (err.request.status === 400){
                    this.$swal({
                      icon: 'error',
                      text: '비밀번호 형식을 확인해주세요.',
                  })
                }
              })
            }            
        }
    },
  }
</script>

<style>
    .border-grey {
        border: 1px solid #d9d9d9;
        border-radius: 5%
    }
    .id-double-check:hover {
        background: #a384ff;
        color: white;
        font-weight: bold;
    }
    .hover-login:hover {
        color: #a384ff;
        text-decoration: underline;
    }

    /* router-link 기본 글자 색 검정색, 밑줄 없애기 0805 임지민 */
    .v-application a {
        color: black;
    }
    a:-webkit-any-link {
        text-decoration: none;
    }
    .signin-logo {
        height: 25px;
        width: 25px;
    }
    .signin-text {
        font-size: 1.2rem;
    }
</style>