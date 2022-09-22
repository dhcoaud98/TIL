<template>
  <!-- 2022.08.02. 스터디 만들기 (남성은) -->
  <!-- 추후 백에서 데이터 받으면 바로 연결해서 axios 통신 가능 -->
  <v-container fluid class="mt-5 rounded-lg create-something" >
    <!-- 문제출제하기 -->
    <v-row>
      <v-col cols="12" class="ma-3">
        <h2 class="px-3 font-weight-regular">스터디 만들기</h2>
      </v-col>
    </v-row>

    <v-divider class="mx-5" color="#A384FF"></v-divider>

    <!-- 문제정보 작성란 -->
      <v-form class="px-5" ref="form" @submit.prevent="submitStudy">
        <!-- 스터디이름 -->
        <v-row class="mx-2 mt-2">
          <v-col class="col-12 pa-0 mb-2">
            <p class="font-weight-bold mb-0">스터디 이름</p>
          </v-col>
          <v-col class="col-12 pa-0">
            <v-text-field
              maxlength="20" 
              counter required dense
              v-model="myStudydetail.title"></v-text-field>
          </v-col>
        </v-row>

        <!-- 카테고리 -->
        <v-row class="mx-2 mt-5">
          <v-col class="col-12 pa-0 mb-2"><p class="mb-0 font-weight-bold">카테고리</p></v-col>
          <v-col class="col-12 pa-0">
            <v-autocomplete 
            :items="categories"
            label="카테고리를 다시 선택해주세요" 
            item-text="toUser" 
            item-value="toDB" 
            required dense chips small-chips multiple
            v-model="myStudydetail.tags"></v-autocomplete>          
          </v-col>
        </v-row>

        <v-row class="mx-2 mt-5">
          <v-col class="col-12 col-md-6 ma-0 pa-0">
            <!-- 스터디 최대인원 -->
            <v-container class="ps-0 pe-0 pe-md-3">
              <v-row>
                <v-col class="col-12 pa-0 mb-2"><p class="mb-0 font-weight-bold">최대인원</p></v-col>
                <v-col class="col-12 pa-0">
                  <v-select 
                  :items="numberofpeople" 
                  dense 
                  class="pe-md-2"
                  v-model="myStudydetail.maxPerson"></v-select>
                </v-col>
              </v-row>
            </v-container>
          </v-col>

          <v-col class="col-12 col-md-6 ma-0 pa-0">
            <!-- 스터디 모집 마감일 -->
            <v-container class="ps-0 pe-0">
              <v-row>
                <v-col class="col-12 pa-0 mb-2"><p class="mb-0 font-weight-bold">모집 마감일</p></v-col>
                <!-- <p>{{ myStudydetail }}</p> -->
                <!-- <p>{{credentials}}</p> -->
                <v-col class="col-12 pa-0">
                  <v-menu
                    ref="menu"
                    v-model="menu"
                    :close-on-content-click="false"
                    :return-value.sync="date"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field v-model="myStudydetail.expiredDate" label="마감일을 다시 선택해주세요" readonly v-bind="attrs" v-on="on" dense class="ps-md-2"></v-text-field>
                    </template>
                    <v-date-picker v-model="myStudydetail.expiredDate" color="#A384FF" no-title scrollable :allowed-dates="allowedDates">
                      <v-spacer></v-spacer>
                      <v-btn text color="#A384FF" @click="menu = false">Cancel</v-btn>
                      <v-btn text color="#A384FF" @click="$refs.menu.save(date)">OK</v-btn>
                    </v-date-picker>
                  </v-menu>
                </v-col>
              </v-row>
            </v-container>
          </v-col>
        </v-row>

        <!-- 스터디 장소 -->
        <v-row class="mx-2 mt-5">
          <v-col class="col-12 pa-0 mb-2"><p class="mb-0 font-weight-bold">장소</p></v-col>
          <v-col class="col-12 pa-0">
            <v-text-field 
            required dense
            v-model="myStudydetail.place"></v-text-field>
          </v-col>
        </v-row>


        <!-- 설명 -->
        <v-row class="mx-2 mt -5">
          <v-col class="col-12 pa-0 mb-2"><p class="font-weight-bold mb-0">스터디 소개</p></v-col>
          <v-col class="col-12 pa-0">
            <v-textarea 
            maxlength="250" 
            rows="4" 
            no-resize counter required dense
            v-model="myStudydetail.mainText"></v-textarea>
          </v-col>
        </v-row>

        <!-- 상세정보 -->
        <v-row class="mx-2 mt-5 mb-2">
          <v-col class="col-12 pa-0 mb-2"><p class="font-weight-bold mb-0">상세정보</p></v-col>
          <v-col class="col-12 pa-0">
            <v-textarea 
            maxlength="250" rows="4" 
            no-resize counter required dense
            v-model="myStudydetail.secretText"></v-textarea>
          </v-col>
        </v-row>

        <v-divider color="#A384FF"></v-divider>
        
        <!-- 출제버튼 -->
        <v-row class="my-2 ">
          <v-col cols="12" class="d-flex justify-end pa-0">
            <!-- router - 1  -->
            <v-btn large rounded color="#EA4C89" class="white--text font-weight-bold me-5 mt-2 py-5" @click="cancel()">취소하기</v-btn>
            <!-- submit -->
            <v-btn large rounded type="submit" color="#A384FF" class="white--text font-weight-bold me-3 mt-2 py-5">수정하기</v-btn>
          </v-col>
        </v-row>

      </v-form>
  </v-container> 
</template>

<script>
import axios from 'axios';
import drf from '@/api/drf';
import { mapGetters } from 'vuex';


export default {
  name: 'CreateProblem',
  data: () => ({
      // 카테고리 데이터
      categories: [
        {toDB:"NW", toUser: "네트워크"},
        {toDB:"OS", toUser: "운영체제"},
        {toDB:"DS", toUser: "자료구조"},
        {toDB:"DB", toUser: "데이터베이스"},
        {toDB:"AL", toUser: "알고리즘"},
        {toDB:"OOP", toUser: "객체지향"},
        {toDB:"PL", toUser: "프로그래밍 언어"},
        {toDB:"CS", toUser: "컴퓨터 구조"},
        {toDB:"TC", toUser: "기술동향"},
        {toDB:"SC", toUser: "보안"},
        {toDB:"ETC", toUser: "기타"},
      ],

      // 스터디원 선택범주
      numberofpeople: [2,3,4,5,6,7,8,9,10],

      // 스터디 마감일
      date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substring(0, 10),
      menu: false,
      modal: false,
      menu2: false,

      // DB에 추가할 때 사용
      credentials: {
        title: '',
        maxPerson: 0,
        expiredDate: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substring(0, 10),
        place: '',
        mainText: '',
        secretText: '',
        tags: [],
      },
      myStudydetail: []

    }),
  methods: {
      // 스터디 마감일 선택시에 당일 기준 전날은 선택 못하도록 하는 메서드
    allowedDates(val) {
      return val >= new Date().toISOString().substring(0,10)
      },
    cancel () {
      this.$router.push({ path: 'study' })
    },
    async submitStudy () {
      await this.$store.dispatch('reIssue');

      axios({
          url: drf.study.study(),
          method: 'put',
          headers: {
            Authorization: this.accessToken,
          },
          data: this.myStudydetail
      })
      .then(res => {
          console.log("스터디 수정res = ",res);
          // const token = res.data.key
          // dispatch('saveToken', token)
          // dispatch('fetchCurrentUser')
          this.$swal({
            icon: 'success',
            text: '스터디 수정이 완료되었습니다'
          })
          this.$router.push({name: 'study'})
      
      })
      .catch(err =>{
          console.log("에러")
          console.log(err)
          console.log(err.response.status)
          console.log("refreshToken=",this.refreshToken)
          if (err.response.status === 401) {
            Token.reissue(this.accessToken, this.refreshToken)
          }
        })
    }
  },
  computed: {
    ...mapGetters(['accessToken', 'refreshToken']),
  },
  created(){
    // api/study/{studyid}에 해당하는 detail study 정보 가져오기
    const sid = this.$route.params.sid
    // console.log('created sid=', sid);
    axios({
      url: drf.study.study() + `${sid}`,
      methods: 'get',
      headers: {
        Authorization : this.accessToken,
      },
    })
    .then(res => {
      // console.log("studydetail =" , res.data)
      this.myStudydetail = res.data
      this.myStudydetail.tags = []
      // this.master = res.data.masterName
      console.log(this.myStudydetail);
      // console.log("myStudydetail =",this.myStudydetail.masterName)
    })
  }
}
</script>

<style>
  .v-application--wrap {
  max-width: none;
  }
  .container {
    max-width: none;
  }
  .w-100 {
    width: 100%;
  }
  .create-something {
    background-color: #EDE7F6;
  }
</style>
}
</script>