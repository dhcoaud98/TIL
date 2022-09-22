<template>
  <!-- 2022.08.01. 문제 만들기 (남성은) -->
  <!-- 추후 백에서 데이터 받으면 바로 연결해서 axios 통신 가능 -->
  <v-container fluid class="mt-5 rounded-lg create-something" >
    <!-- 문제출제하기 -->
    <v-row>
      <v-col cols="12" class="ma-3">
        <h2 class="px-3 font-weight-regular">문제 출제하기</h2>
      </v-col>
    </v-row>

    <v-divider class="mx-5" color="#A384FF"></v-divider>

    <!-- 문제정보 작성란 -->
      <v-form ref="form" @submit.prevent="createProblem" class="px-5">
        <!-- 카테고리 -->
        <v-row class="mx-2 mt-5">
          <v-col class="col-12 pa-0 mb-2"><p class="mb-0 font-weight-bold">카테고리</p></v-col>
          <v-col class="col-12 pa-0">
            <v-autocomplete v-model="credentials.tags" :items="categories" item-text="toUser" item-value="toDB" label="주제를 선택하세요 (복수선택 가능)" required dense chips small-chips multiple></v-autocomplete>          
          </v-col>
        </v-row>

        <!-- 문제이름 -->
        <v-row class="mx-2 mt-2">
          <v-col class="col-12 pa-0 mb-2"><p class="font-weight-bold mb-0">문제이름</p></v-col>
          <v-col class="col-12 pa-0">
            <v-text-field v-model="credentials.title" label="문제 이름을 입력하세요 (최대 20자)" maxlength="20" counter required dense></v-text-field>
          </v-col>
        </v-row>

        <!-- 지문 -->
        <v-row class="mx-2 my-2">
          <v-col class="col-12 pa-0 mb-2"><p class="font-weight-bold mb-0">지문</p></v-col>
          <v-col class="col-12 pa-0">
            <v-textarea v-model="credentials.mainText" label="지문을 입력하세요 (최대 150자)" maxlength="150" no-resize counter required dense></v-textarea>
          </v-col>
        </v-row>

        <!-- 보기 -->
        <!-- 정답보기 -->
        <v-row class="mx-2 mt-4">
          <v-col class="col-12 col-md-3 col-lg-2 pa-0"><p class="font-weight-bold mb-0">보기1 (정답)</p></v-col>
          <v-col class="col-12 col-md-9 col-lg-10 pa-0">
            <v-text-field v-model="credentials.ex1" label="정답이 되는 첫 번째 보기를 입력하세요" required dense></v-text-field>
          </v-col>
        </v-row>
        <!-- 오답보기1 -->
        <v-row class="mx-2 mt-2">
          <v-col class="col-12 col-md-3 col-lg-2 pa-0"><p class="font-weight-bold mb-0">보기2</p></v-col>
          <v-col class="col-12 col-md-9 col-lg-10 pa-0">
            <v-text-field v-model="credentials.ex2" label="두 번째 보기를 입력하세요" required dense></v-text-field>
          </v-col>
        </v-row>
        <!-- 오답보기2 -->
        <v-row class="mx-2 mt-2">
          <v-col class="col-12 col-md-3 col-lg-2 pa-0"><p class="font-weight-bold mb-0">보기3</p></v-col>
          <v-col class="col-12 col-md-9 col-lg-10 pa-0">
            <v-text-field v-model="credentials.ex3" label="세 번째 보기를 입력하세요" required dense></v-text-field>
          </v-col>
        </v-row>
        <!-- 오답보기3 -->
        <v-row class="mx-2 mt-2 mb-5">
          <v-col class="col-12 col-md-3 col-lg-2 pa-0"><p class="font-weight-bold mb-0">보기4</p></v-col>
          <v-col class="col-12 col-md-9 col-lg-10 pa-0">
            <v-text-field v-model="credentials.ex4" label="네 번째 보기를 입력하세요" required dense></v-text-field>
          </v-col>
        </v-row>          
        
        <v-divider color="#A384FF"></v-divider>
        
        <!-- 출제버튼 -->
        <v-row class="my-2 ">
          <v-col cols="12" class="d-flex justify-end pa-0">
            <!-- router - 1  -->
            <v-btn large rounded color="#EA4C89" class="white--text font-weight-bold me-5 mt-2 py-5" @click="cancel()">취소하기</v-btn>
            <!-- submit -->
            <v-btn large rounded type="submit" color="#A384FF" class="white--text font-weight-bold me-3 mt-2 py-5">출제하기</v-btn>
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
      credentials: {
        title: '',
        tags: [],
        answer: '',
        mainText: '',
        ex1: '',        
        ex2: '',
        ex3: '',
        ex4: '',
      }
    }),
  methods: {
    cancel () {
      this.$router.push({ path: `../profile/${this.currentUser}` })
    },
    async createProblem() {
      await this.$store.dispatch('reIssue');
			// console.log('토큰 = ', this.accessToken);
			this.credentials.answer = this.credentials.ex1;
			axios({
				url: drf.postFeed.problem(),
				method: 'post',
				headers: {
					Authorization: this.accessToken,
				},
				data: this.credentials,
			})
				.then((res) => {
					console.log('res = ', res);
          this.$router.push({ path: `../profile/${this.currentUser}` })
				})
				.catch((err) => {
					console.log('에러');
					console.log(err);
				});
		},
  },
  computed: {
    ...mapGetters(['accessToken', 'currentUser']),
  },
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
