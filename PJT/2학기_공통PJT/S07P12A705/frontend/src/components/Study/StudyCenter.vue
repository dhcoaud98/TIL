<template>
  <v-container class="ma-0 pa-0">
    <v-row class="d-flex mt-5 ms-5">
      <v-icon large color="#926DFF">groups</v-icon>
      <h2 class="ms-3 dark--text font-weight-regular">S T U D Y</h2>
    </v-row>    

    <!-- 1. 프로필 상단 -->
    <v-row class="justify-center mt-10 mx-5 mb-0">
      <!-- 뱃지, 이름 -->
      <v-container class="pa-0 mx-0">
        <v-row>
          <div class="d-flex">
            <div><v-chip :color="`${this.badgeColor}`" class="white--text font-weight-bold mx-3">{{badge}}</v-chip></div>
            <div class="d-flex justify-center align-end"><h2 class="pa-0 ma-0">{{userName}}</h2><h3 class="grey--text">님의 스터디</h3></div>
          </div>

          <div class="d-flex">
          </div>
        </v-row>

        <v-row class="ps-10">
          <v-col cols="6" class="detail_text ma-0 pa-0">문제 풀이 {{userInfo.problemSolvingCount}} 문제</v-col>
          <v-col cols="6" class="detail_text ma-0 pa-0">정답률 {{ userInfo.correctRate }}%</v-col>
          <v-col cols="6" class="detail_text ma-0 pa-0">문제/정보 작성 {{ userInfo.writePostCount }}문제</v-col>
          <v-col cols="6" class="detail_text ma-0 pa-0">포인트 {{ userInfo.point }}점</v-col>
        </v-row>

        <v-row class="pa-0"> 
          <v-col class="pa-0 px-2">
            <v-btn text rounded class="pa-0 dark--text" @click="event()" color="#512DA8" width="100%">
              <v-icon color="#A384FF" class="me-2">group_add</v-icon><h3>MAKE STUDY +</h3>
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-row>

    <!-- 2. 프로필 하단 -->
    <v-row class="d-flex justify-center mt-5 mx-5 mb-0">
      <v-toolbar dark height="45px">
        <v-tabs v-model="tabs" background-color="#CCA5FE" grow> 
          <v-col class="px-0">
            <v-tab class="tab--text white--text pa-0" href="#one"><h3 class="font-weight-regular">STUDIES</h3></v-tab>
          </v-col>
          <v-col class="px-0">
            <v-tab class="tab--text white--text pa-0" href="#two"><h3 class="font-weight-regular">MY STUDY</h3></v-tab>
          </v-col>
        </v-tabs>
      </v-toolbar>
      
      <v-container class="ma-0 pa-0" v-if="activeFab.page === '1'">
        <study-list></study-list>
      </v-container>
      <v-container class="ma-0 pa-0" v-if="activeFab.page === '2'">
        <my-study-list></my-study-list>
      </v-container>
    </v-row>
  </v-container>
</template>

<script>
import StudyList from "./StudyList.vue"
import MyStudyList from "./MyStudyList.vue"
import router from "@/router"
import { mapGetters } from 'vuex'
import axios from 'axios'
import drf from '@/api/drf'


export default {
  name: 'ProfileCenter',
  components: {
    StudyList,
    MyStudyList,
  },
  data () {
    return {
      fab: false,
      hidden: false,
      tabs: null,
      pass: '',
      userInfo: {},
      badge: 'S E E D',
      badgeColor: 'rgb(0, 207, 87)',
    }
  },
  computed: {
    activeFab () {
      switch (this.tabs) {
        case 'one': return { page: '1' }
        case 'two': return { page: '2' }
        default: return {}
      }
    },
    ...mapGetters(['accessToken', 'userId', 'userName', 'currentUser'])
  },
  methods:{
    event () {
      router.push({ path: 'createstudy' })
    }
  },
  created() {
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
.rank_box{
  border-radius: 10px;
  border: 1px solid rgb(142, 68, 173);
  background-color: rgb(142, 68, 173);
  height: 25px;
  width: 80%;
}
.rank {
  font-size: 18px;
  color: white;
  font-weight: bold;
}
.v-application--wrap {
  max-width: none;
}
.category-tag {
  border-radius: 20px;
  border: 1px solid #A384FF;
  background-color: #A384FF;
  font-size: 5px;
  color: white;
  font-weight: bold;
  height: 25px;
  margin: 1px;
}
.detail{
  border-radius : 5px;
  border: 1px dashed #000000;
  height : 100px;
}
.detail_text {
  font-size: 16px;
  font-weight: 500;
}
.tab--text {
  color: #000000 !important;
}
</style>

