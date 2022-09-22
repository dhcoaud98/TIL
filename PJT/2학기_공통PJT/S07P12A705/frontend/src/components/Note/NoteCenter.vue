<template>
  <v-container class="ma-0 pa-0">
    <v-row class="d-flex mt-5 ms-5">
      <v-icon large color="#926DFF">sticky_note_2</v-icon>
      <h2 class="ms-3 dark--text font-weight-regular">N O T E</h2>
    </v-row>  

    <!-- row 1. 제목 -->
    <v-row class="mt-10 mx-5 mb-0">
      <div class="d-flex">
        <div><v-chip :color="`${this.badgeColor}`" class="white--text font-weight-bold mx-3">{{badge}}</v-chip></div>
        <div class="d-flex justify-center align-end"><h2 class="pa-0 ma-0">{{userName}}</h2><h3 class="grey--text">님의 오답노트</h3></div>
      </div>
    </v-row>

    <!-- 
      row 2. 카테고리들 
      - 클릭하면 내부 텍스트 값을 아래 열로 보내주기
      - 그리고 그 텍스트 값을 notelist로 내려줘야 함
    -->
    <v-row class="bottom-border-grey pb-5 mr-2 mx-5 mb-0">
      <v-chip-group column mandatory active-class="clicked-chip">
        <v-chip class="mr-2 my-2 border-grey" @click="selectCategory('whole','전체')" id="whole" small>#전체</v-chip>
        <div v-for="category in categories" :key="category.toDB">
          <v-chip class="mr-2 my-2 border-grey" :id="category.toDB" @click="selectCategory(category.toDB, category.toUser)" small>
            #{{category.toUser}}</v-chip>
        </div>
      </v-chip-group>
    </v-row>

    <!-- row 3: 선택한 카테고리 -->
    <v-row class="mt-2 mr-0 mx-5">
      <v-col class="bottom-border-grey">
        <p class="font-parent-lar font-weight-bold mb-1">#{{ selectedUser }}</p>
      </v-col>
    </v-row>

    <!-- row4. note list -->
    <v-row class="ml-2 mx-5">
      <p class="font-parent-mid-l font-weight-bold bottom-border-grey mt-3 mx-5">작성 전 문제</p>
      <!-- <p>hi</p> -->
      <!-- <p>{{ beforeProbs }} </p> -->
    </v-row>
    <v-row v-if="noBeforeProbs">
      <v-col class="text-center">
        <p>아직 작성 전 오답노트가 없습니다</p>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <note-list :selectedDB="selectedDB" :beforeProbs="beforeProbs"></note-list>
      </v-col>
    </v-row>
    <v-row class="text-center justfy-center">
      <v-col>
        <v-pagination
          v-model="page1"
          :length="beforeProbs.length/3 + 1"
          color="#A384FF"
          class="mt-3"
        ></v-pagination>
      </v-col>
  </v-row>
    <hr class="my-5 border-grey mx-5">
    <v-row class="ml-2">
      <p class="font-parent-mid-l font-weight-bold bottom-border-grey mx-5">이미 작성한 문제</p>
    </v-row>
    <v-row v-if="noAfterProbs">
      <v-col class="text-center">
        <p>아직 작성 후 오답노트가 없습니다</p>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <note-list :selectedDB="selectedDB" :afterProbs="afterProbs"></note-list>
      </v-col>
    </v-row>
    <v-row class="text-center justfy-center">
      <v-col>
        <v-pagination
          v-model="page2"
          :length="afterProbs.length/3 + 1"
          color="#A384FF"
          class="mt-3"
        ></v-pagination>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import NoteList from '@/components/Note/NoteList.vue'
import { mapGetters } from 'vuex'
import axios from 'axios'
import drf from '@/api/drf.js'

export default {
  components: {
    NoteList
  },
  data() {
    return {
      page1: 1,
      page2: 1,
      noBeforeProbs: false,
      noAfterProbs: false,
      selectedUser : '전체',
      selectedDB: 'whole',
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
      beforeProbs: [],
      afterProbs: [],
      badge: 'S E E D',
      badgeColor: 'rgb(0, 207, 87)',
    }
  },
   methods: {
    selectCategory(toDB, toUser) {
      this.selectedUser = toUser
      if (toDB == 'whole') {
        this.wholeNote()
      } else {
        this.tagNote(toDB)
      }
    }
  },
  computed: {
    ...mapGetters(['accessToken', 'userId', 'userName', 'currentUser'])
  },
  methods: {
    wholeNote () {
      const isWriteParams = ['true', 'false']
  
      isWriteParams.forEach(oneParam => {
        const params = {
            // pageable: 0,
            isWrite: oneParam,
            // sort: onUpdated, 'desc'
          } 
        axios({
          url: drf.api + 'wrongAnswer/' + 'all',
          method: 'get',
          headers: {
            Authorization: this.accessToken,
          },
          params: params,
        })
        .then(res => {
          // 받아온 데이터를 작성 전/후로 구분하는 작업 필요(0808 임지민)
          // console.log(res.data.content)
          if (oneParam === 'false'){
            this.beforeProbs = res.data.content
            console.log('before=', this.beforeProbs)
          
            if (!this.beforeProbs.length) {
              this.noBeforeProbs = true
            }
    
          } else {
            this.afterProbs = res.data.content
            console.log('after=',this.afterProbs)
            if (!this.afterProbs.length){
               this.noAfterProbs = true
              }
          }
          // console.log('in'); //ok
        })
        .catch(err => {
          // console.log(this.accessToken)
          // console.log(this.userId)
          console.log(err);
        })
      })
    },
    tagNote(toDB) {
    // console.log('toDB= ', toDB);
    const isWriteParams = ['true', 'false']
    isWriteParams.forEach(oneParam => {
      const params = {
        page: this.page,
        size: 3,
        tag: toDB,
        isWrite: oneParam
      }
      axios({
        url: drf.api + 'wrongAnswer/' + 'tag',
        method: 'get',
        headers: {
          Authorization: this.accessToken,
        },
        params: params,
      })
      .then(res => {
        // 받아온 데이터를 작성 전/후로 구분하는 작업 필요(0808 임지민)
        // console.log(res.data)
        if (oneParam === 'false'){
          this.beforeProbs = res.data.content
          // console.log('tagbefore');
          // console.log('tagbefore=', this.beforeProbs)
        } else {
          this.afterProbs = res.data.content
          // console.log('tagafter');
          // console.log('tagafter=',this.afterProbs)
        }
        // console.log('in'); //ok
       })
      .catch(err => {
        // console.log(this.accessToken)
        // console.log(this.userId)
        console.log(err);
      })
    })
    },
  },
  created() {
    this.wholeNote()

    
    // 유저 정보 확인
    axios({
      url: drf.api + 'user/' + 'info/' + `${this.currentUser}`,
      method: 'get',
      headers: {
        Authorization : this.accessToken,
      },
    })
    .then(res => {
      console.log(res.data)
      this.userInfo = res.data
      // 뱃지 컬러랑 문구 정하기
      if (this.userInfo.problemSolvingCount + this.userInfo.writePostCount >= 10 ) {
        this.badge = "G R E E N"
        this.badgeColor = "rgb(0, 128, 0)"
      } else if (this.userInfo.problemSolvingCount + this.userInfo.writePostCount >= 50) {
        this.badge = "B R O N Z E"
        this.badgeColor = "rgb(176, 141, 87)"
      } else if (this.userInfo.problemSolvingCount + this.userInfo.writePostCount >= 100) {
        this.badge = "S I L V E R"
        this.badgeColor = "rgb(192, 192, 192)"
      } else if (this.userInfo.problemSolvingCount + this.userInfo.writePostCount >= 200) {
        this.badge = "G O L D"
        this.badgeColor = "rgb(255, 215, 0)"
      } else if (this.userInfo.problemSolvingCount + this.userInfo.writePostCount >= 500) {
        this.badge = "M A S T E R"
        this.badgeColor = "rgb(231,76,60)"
      } else if (this.userInfo.problemSolvingCount + this.userInfo.writePostCount >= 1000) {
        this.badge = "P R O S N"
        this.badgeColor = "rgb(142,68,173)"
      } 
    })
  },
}
</script>

<style>
.clicked-chip {
  background-color: #a394ff !important;
  color: white !important;
  border: none;
}
.bottom-border-grey {
  border-bottom: 1px solid #d9d9d9;
}
.theme--light.v-chip:not(.v-chip--active) {
  background: white;
}
.row {
  margin: auto;
}
.font-parent-mid-l {
  font-size: 1em;
}
</style>