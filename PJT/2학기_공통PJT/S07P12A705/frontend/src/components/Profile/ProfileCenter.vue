<template>
  <v-container class="ma-0 pa-0">
    <v-row class="d-flex mt-5 ms-5">
      <v-icon large color="#926DFF">person</v-icon>
      <h2 class="ms-3 dark--text font-weight-regular">P R O F I L E</h2>
    </v-row>
    
    <!-- 1. 프로필 상단 -->
    <v-row class="justify-center mt-10 mx-5 mb-0">
      <!-- 뱃지, 이름 -->
      <v-container class="pa-0 mx-0">
        <v-row class="d-flex justify-space-between align-end">
         <div class="d-flex">
            <div><v-chip :color="`${this.badgeColor}`" class="white--text font-weight-bold mx-3">{{badge}}</v-chip></div>
            <div class="d-flex justify-center align-end"><h2 class="pa-0 ma-0">{{ userInfo.name }}</h2><h3 class="grey--text">님의 프로필</h3></div>
          </div>
          
          <!-- 팔로우 팔로워 정보 -->
          <div class="d-flex" v-if="userInfo.id == currentUser">
            <v-btn @click="openFollowerModal" plain x-large class="px-0"><h4 class="me-3">팔로워 {{ userInfo.followerCount }}명</h4></v-btn>
            <v-btn @click="openFollowingModal" plain x-large class="px-0"><h4>팔로잉 {{ userInfo.followingCount }}명</h4></v-btn>

            <my-follower-modal scrap @close="closeFollowerModal" v-if="myFollowerModal"></my-follower-modal>
            <my-following-modal scrap @close="closeFollowingModal" v-if="myFollowingModal"></my-following-modal>
          </div>

          <div class="d-flex" v-else>
            <h4 class="grey--text text--darken-2 me-3">팔로워 {{ userInfo.followerCount }}명</h4>
            <h4 class="grey--text text--darken-2">팔로잉 {{ userInfo.followingCount }}명</h4>
          </div>
        </v-row>

        <v-row class="ps-10">
          <v-col cols="6" class="detail_text ma-0 pa-0">문제 풀이 {{ userInfo.problemSolvingCount }} 문제</v-col>
          <v-col cols="6" class="detail_text ma-0 pa-0">정답률 {{ userInfo.correctRate }}%</v-col>
          <v-col cols="6" class="detail_text ma-0 pa-0">문제/정보 작성 {{ userInfo.writePostCount }}문제</v-col>
          <v-col cols="6" class="detail_text ma-0 pa-0">포인트 {{ userInfo.point }}점</v-col>
        </v-row>

        <!-- 만약 내 페이지라면 글작성 -->
        <v-row v-if="currentUser === userInfo.id" class="pa-0"> 
          <v-col class="pa-0 px-2">
            <v-btn text rounded class="pa-0 dark--text" @click="event1()" color="#512DA8" width="100%">
              <v-icon color="#A384FF" class="me-2">quiz</v-icon><h3>PROBLEM +</h3>
            </v-btn>
          </v-col>
          <v-col class="pa-0 px-2">
            <v-btn text rounded class="pa-0 font-weight-bold dark--text" @click="event2()" color="#512DA8" width="100%" >
              <v-icon color="#A384FF" class="me-2">info</v-icon><h3>INFORMATION +</h3>
            </v-btn>
          </v-col>
        </v-row>

        <!-- 내 페이지 아니면 팔로우/언팔로우 버튼 -->
        <v-row v-else class="pa-0"> 
          <v-col class="pa-0 px-2">
            <v-btn @click="followEvent" text rounded class="pa-0 dark--text" color="#512DA8" width="100%">            
              <h3 v-if="isFollow">팔로우 취소</h3>
              <h3 v-else>팔로우</h3>
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-row>

    <!-- 2. 프로필 하단 -->
    <!-- 내 프로필일 때 -->
    <v-row v-if="currentUser === userInfo.id" class="profile_tab d-flex justify-center mt-5 mx-5 mb-0">
      <v-toolbar dark height="45px">
        <v-tabs v-model="tabs" background-color="#CCA5FE" grow>
          <v-col class="px-0">
            <v-tab class="tab--text white--text pa-0" href="#one"><h3 class="font-weight-regular">SOLVING</h3></v-tab>
          </v-col>
          <v-col class="px-0">
            <v-tab class="tab--text white--text pa-0" href="#two"><h3 class="font-weight-regular">SCRAP</h3></v-tab>
          </v-col>
          <v-col class="px-0">
            <v-tab class="tab--text white--text pa-0" href="#three"><h3 class="font-weight-regular">My Post</h3></v-tab>
          </v-col>
        </v-tabs>
      </v-toolbar>
          
      <v-container class="ma-0 pa-0" v-if="activeFab.page === '1'">
        <solved-problem-list></solved-problem-list>
      </v-container>
      <v-container class="ma-0 pa-0" v-if="activeFab.page === '2'">
        <scrap-post-list></scrap-post-list>
      </v-container>
      <v-container class="ma-0 pa-0" v-if="activeFab.page === '3'">
        <my-post-list></my-post-list>
      </v-container>
    </v-row>

    <!-- 다른사람 프로필일 때 -->
    <v-row v-else class="profile_tab d-flex justify-center mt-5 mx-5 mb-0">
      <v-toolbar dark height="45px">
        <v-tabs v-model="tabs" background-color="#CCA5FE" grow>
          <v-col class="px-0">
            <v-tab class="tab--text white--text pa-0" href="#three"><h3 class="font-weight-regular">{{userInfo.name}}'s Post</h3></v-tab>
          </v-col>
        </v-tabs>
      </v-toolbar>

      <v-container class="ma-0 pa-0" v-if="activeFab.page === '3'">
        <my-post-list></my-post-list>
      </v-container>
    </v-row>
  </v-container>
</template>

<script>
import SolvedProblemList from "./SolvedProblemList.vue"
import ScrapPostList from "./ScrapPostList.vue"
import MyPostList from "./MyPostList.vue"
import MyFollowingModal from "./MyFollowingModal.vue"
import MyFollowerModal from "./MyFollowerModal.vue"
import { mapGetters } from 'vuex'
import axios from 'axios'
import drf from '@/api/drf'

export default {
  name: 'ProfileCenter',
  components: {
    SolvedProblemList,
    ScrapPostList,
    MyPostList,
    MyFollowingModal,
    MyFollowerModal,
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
      profileOwnerId: '',
      isFollow: false,
      myFollowerModal: false,
      myFollowingModal: false,
    }
  },
  computed: {
    activeFab () {
      switch (this.tabs) {
        case 'one': return { page: '1' }
        case 'two': return { page: '2' }
        case 'three': return { page : '3' }
        default: return {}
      }
    },
    ...mapGetters(['accessToken', 'userId', 'userName', 'currentUser'])
  },
  methods:{
    event1 () {
      this.$router.push({ path: '../createproblem' })
    },
    event2 () {
      this.$router.push({ path: '../createinfo' })
    },
    openFollowerModal () {
      this.myFollowerModal = true
    },
    openFollowingModal () {
      this.myFollowingModal = true
    },
    closeFollowerModal () {
      this.myFollowerModal = false
    },
    closeFollowingModal () {
      this.myFollowingModal = false
    },
    followEvent () {
      axios({
        url: drf.api + 'user/' + 'following/' + `${this.userInfo.id}`,
        method: 'get',
        headers: {
          Authorization : this.accessToken,
        }
      })
      .then(res => {
        console.log('팔로잉 성공')
        console.log(res.data)
        this.$router.go()
        // console.log("totalPages =",res.data.totalPages)
        // console.log("totalElements =", res.data.totalElements)
      })
      .catch(err => {
        console.log("에러")
        console.log(err)
      })    
    }
  },
  created() {
    // 유저정보 확인
    const profileOwnerId = this.$route.params.uid;
    console.log('프로필', profileOwnerId)
    axios({
      url: drf.api + 'user/' + 'info/' + `${profileOwnerId}`,
      method: 'get',
      headers: {
        Authorization : this.accessToken,
      },
    })
    .then(res => {
      // console.log('프로필 주인', res.data)
      // console.log('지금 프로필 보는사람', this.currentUser)
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

    axios({
      url: drf.api + 'user/following',
      method: 'get',
      headers: {
        Authorization : this.accessToken,
      },
    })
    .then(res => {
      const myFollowingList = res.data.content
      console.log(this.userInfo.id)
      myFollowingList.forEach((element) => {
        // console.log('element', element)
        // console.log('id', this.userInfo.id)
        if (element.id == this.userInfo.id) {
        this.isFollow = true
      }})
    })
    .catch(err => {
      console.log(err)
    })
  }
}
</script>


<style>
.rank_box{
  border-radius: 10px;
  border: 1px solid rgb(142, 68, 173);
  background-color: rgb(142, 68, 173);
  height: 25px;
  width: 20px;
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

