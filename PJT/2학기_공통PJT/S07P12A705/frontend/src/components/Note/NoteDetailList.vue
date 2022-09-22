<template>
  <!-- 작성 완료된 문제 요소 하나하나 0807 임지민  -->
  <!-- 문제 하나하나 받아오기 -->
  <!-- 화면 크기가 xs 이하일 때는 문제와 노트 작성 칸이 세로로 배치되게 수정하기 0805 임지민 -->
  <v-row class="mt-3">
    <!-- <p>{{ shuffledNum }}</p>  ok-->
    <!-- col 1: 상위의 createnotelist에서 받아온 문제 출력 -->
    <v-col cols="12" md="6" class="px-10 pr-md-5">
      <!-- 문제 보러가기 버튼: 문제 번호 받아와서 연결 -->
      <v-row class="mt-3 mb-5">
        <!-- <p>{{noteDetail}}</p> -->
        <router-link :to="`/problem/${noteDetail.pid}`" class="text-decoration-none ">
          <v-chip small outlined color="#a384ff" class="hover-pointer">문제 다시 풀기</v-chip>
        </router-link>
      </v-row>

      <!-- 문제 제목 -->
      <v-row class="justify-space-between">
        <h2>{{noteDetail.title}}</h2>
      </v-row>

      <!-- 문제 지문 -->
      <v-row>
        <p class="font-parent-mid-l">{{noteDetail.mainText}}</p>
      </v-row>

      <!-- 문제보기: 이것도 랜덤으로 for문 돌리기/ 체크박스로 라디오 묶는거....ㅠ-->
      <v-row>
        <v-col>
          <div v-for="example in examples" :key="example.id" class="my-3">
            <input type="radio" :value="`보기${example.id}`" :id="`check${example.id}`" name="bogey">
            <label :for="`check${example.id}`" 
            class="ml-2 font-parent-mid-l">
            {{example.example}} </label>
          </div>
        </v-col>
      </v-row>
 
      
      <v-row>
        <!-- 클릭하면 선지에서 보이게 -->
        <div class="text-center">
          <!-- db에서 받아온 내가 고른 답 -->
          <v-btn
            small
            outlined
            color="#a384ff"
            @click="selectMyAnswer"
          >
            내가 고른 답
          </v-btn>
        </div>
        <div class="text-center ml-3">
          <v-btn
            small
            outlined
            color="#a384ff"
            @click="selectRealAnswer"
          >
            정답
          </v-btn>

      </div>
      </v-row>
    </v-col>

    <v-divider vertical class="d-none d-md-block"></v-divider>

    <!-- col 2: 오답노트 양식 -->
    <!-- v-textarea에 v-model이랑 value를 같이 쓰면 value가 적용이 안됨 -->
    <v-col cols="12" md="6" class="px-3 mt-10 mt-md-0">
      <v-form class="pl-3" @submit.prevent="editNote">
        <!-- 틀린 이유 -->
        <v-row class="mx-2 my-2">
          <p class="font-weight-bold font-parent-mid-l mb-0">틀린 이유</p>
          <v-col class="col-12 pa-0">
            <v-textarea 
            maxlength="150" 
            no-resize counter required dense 
            rows="3" 
            class="font-parent-mid"
            v-model="noteDetail.reason"
            ></v-textarea>
          </v-col>
        </v-row>
        <!-- 추가로 공부할 것 -->
        <v-row class="mx-2 my-2">
          <v-col class="col-12 pa-0 mb-2"><p class="font-weight-bold font-parent-mid-l mb-0">추가로 공부할 것</p></v-col>
          <v-col class="col-12 pa-0">
            <v-textarea maxlength="150" 
            no-resize counter required dense 
            rows="3" 
            class="font-parent-mid"
            v-model="noteDetail.studyContent"
            > </v-textarea>
          </v-col>
        </v-row>
        <!-- 메모 -->
        <v-row class="mx-2 my-2">
          <v-col class="col-12 pa-0 mb-2"><p class="font-weight-bold font-parent-mid-l mb-0">메모</p></v-col>
          <v-col class="col-12 pa-0">
            <v-textarea maxlength="150" 
            no-resize counter required dense 
            rows="3" 
            class="font-parent-mid"
            v-model="noteDetail.memo"
            ></v-textarea>
          </v-col>
        </v-row>
        <!-- 수정하기 -->
        <v-row class="justify-end mt-5">
          <v-btn type="submit" outlined rounded small class="mr-3">수정하기</v-btn>
          <v-btn outlined rounded small @click="deleteNote">삭제하기</v-btn>
        </v-row>
      </v-form>
    </v-col>
  </v-row>
</template>

<script>
import axios from 'axios'
import drf from '@/api/drf.js'
import { mapGetters } from 'vuex'

export default {
  data(){
    return {
      examples: [],

    }
  },
  props: {
    noteDetail: Object,
  },
  computed: {
    ...mapGetters(['accessToken'])
  },
  methods :{
    selectMyAnswer() {
      // 클릭하면 내 정답에 해당되는 걸 위에 선지에서 표시
      // script에 props로 값이 넘어오니까 this.어쩌구로 받아오기
      // v-model로 스크립트와 템플릿 연결하기
      const myAnswer = this.noteDetail.wrongAnswer
      const targetMyAnswer = document.querySelector(`#check${myAnswer}`)
      console.log('targetMyAnswer=', targetMyAnswer)
      targetMyAnswer.checked=true
      targetMyAnswer.setAttribute("style", "accent-color: red;")
    },
    selectRealAnswer() {
      const targetRealAnswer = document.querySelector('#check1')
      console.log('targetRealAnswer=', targetRealAnswer)
      targetRealAnswer.checked=true
      targetRealAnswer.setAttribute("style", "accent-color: green;")
    },
    async editNote() {
      await this.$store.dispatch('reIssue');
      axios({
          url: drf.wrongAnswer.wrongAnswer(),
          method: 'patch',
          data: {
            id: this.noteDetail.id,
            reason: this.noteDetail.reason,
            studyContent: this.noteDetail.studyContent,
            memo: this.noteDetail.memo,
          },
          headers: {
            Authorization: this.accessToken,
          },
      })
      .then(res => {
          console.log("res = ",res);
          this.$router.go()
          // data에 저장해서 띄우기
          // dispatch('saveToken', token)
          // dispatch('fetchCurrentUser')
      
      })
      .catch(err =>{
          console.log("에러")
          console.log(err)
        })
    },
    async deleteNote() {
      await this.$store.dispatch('reIssue');

      const userDecision = confirm('정말로 삭제하시겠습니까?')
      if (userDecision) {
        axios({
            url: drf.wrongAnswer.wrongAnswer() + this.noteDetail.id,
            method: 'delete',
            headers: {
              Authorization: this.accessToken,
            },
        })
        .then(res => {
            console.log("res.data = ",res.data);
            this.$router.push({ path: '/note' })
        })
        .catch(err =>{
            console.log("에러")
            console.log(err)
            })
      }
    },
    
  },
  created() {
    // 랜덤으로 띄워주기 위해 숫자 섞기
    // 근데 이렇게하면 어쩔때는 보기가 undefined가 뜸
    const nums  = [1,2,3,4]
    const shuffled = nums.sort(() => Math.random() - 0.5)
    // const noteDetail = this.noteDetail
    // this.shuffledNum = shuffled
    nums.forEach(num => {
      // console.log(ex)
      // console.log(dict);
      // const dict = {}
      // this.examples.push(`example${num}`)
      // console.log(dict)

      this.examples.push({'id': num, 'example': this.noteDetail[`example${num}`]})
      // console.log(this.noteDetail[`example${num}`])

      // const arr = []
      // arr.push(this.noteDetail[`example${num}`])
      // console.log(arr)
    })
    // console.log(this.shuffledNum)
  }
}
</script>

<style>
  .left-border-grey {
    border-left: 1px solid #d9d9d9;
  }

  /* 내가 고른 답, 정답이 나오는 드롭다운의 box shadow 없애기 */
  .v-menu__content {
    box-shadow: none;
  }
  .hover-pointer:hover{
    cursor: pointer;
  }

</style>