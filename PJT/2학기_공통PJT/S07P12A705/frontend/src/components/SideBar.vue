<template>
  <!-- 채명왈 : lg 사이즈 이하에서는 사이드바가 보이지 않음! -->
  <!-- sidebar가 작은 화면에서 사라지는 문제: v-navigation-drawer 태그를 안쓰니까 해결됨 (0808 임지민) -->
  <v-container fluid class="bg-grey pa-0 mt-1 ml-3">
    <v-row>
      <!-- 채명왈 : login이랑 logout 나중에 router로 연결하면 됨 -->
      <v-col cols="6" class="justify-center pa-0">
        <li style="list-style: none;" v-if="!isLoggedIn">
          <router-link to="/signup" class="text-decoration-none black--text"><v-btn class="pa-0" rounded-sm color="#a384ff" width="100%" text>signup</v-btn></router-link>
        </li>
        <!-- 08.07 오채명 : 후에 유저 이름을 클릭하면 유저의 프로필로 넘어갈 수 있도록 함. -->
        <li style="list-style: none;" v-if="isLoggedIn">
          <router-link to="/profile" class="text-decoration-none black--text"><v-btn class="pa-0" rounded-sm color="#a384ff" width="100%" text>{{ userName }}</v-btn></router-link>
        </li>
      </v-col>
      
      <v-col cols="6" class="justify-center pa-0">
        <li style="list-style: none;" v-if="!isLoggedIn">
          <router-link to="/login" class="text-decoration-none black--text"><v-btn class="pa-0" rounded-sm color="#a384ff" width="100%" text>login</v-btn></router-link>
        </li>
        <li style="list-style: none;" v-if="isLoggedIn">
          <v-btn class="pa-0" rounded-sm color="#a384ff" width="100%" text @click="logout">logout</v-btn>
        </li>
      </v-col>
    </v-row>


    <!-- 1. 오늘의 인기 문제 -->
    <!-- icon 찾기 -->
    <v-card class="mx-auto mt-5 mb-5 pink-gradation rounded-xl" height ="auto">
      <v-card-text class="pa-5">
        <v-container>
        
          <!-- 전체제목 -->
          <v-row class="mt-2">
            <v-col class="pa-0">
              <p class="d-flex justify-center mb-0 color-magenta font-weight-bold">🎨 인기 문제</p>
            </v-col>
          </v-row>

          <!-- 상위 3개문제 -->
          <v-row>
            <v-container class="px-5">
              <!-- v-for문 돌릴것들 -->
              <!-- 각 추천문제 -->
              <!-- 인기문제; 제출률: 제출 수/조회 수*100 0813 임지민 -->
              <div v-for="(popularProb, idx) in popularProbs" :key="idx" class="mb-3">
                <v-row class="ps-2">
                  <v-btn plain @click="problemEvent(popularProb.popularityProblem.id)"><p class="title-font-size font-weight-bold mb-0 text-truncate">{{idx + 1}}. {{popularProb.popularityProblem.title.slice(0,10)}}</p></v-btn>
                </v-row>    
                <v-row class="d-flex justify-space-between font-weight-bold mt-1">
                  <div class="circle-background pa-0 d-flex justify-center align-center text-center">
                    추천<br>{{popularProb.popularityProblem.numOfLikes}}
                  </div>
                  <div class="circle-background pa-0 d-flex justify-center align-center text-center">
                    참여자<br>{{popularProb.popularityProblem.submissionNum}}명
                  </div>
                  <div class="circle-background pa-0 d-flex justify-center align-center text-center">
                    제출률<br>{{Math.ceil((popularProb.popularityProblem.submissionNum/popularProb.popularityProblem.views)*100)}}%
                  </div>
                </v-row>
                <!-- 여기까지를 v-for문 돌리면 됨 -->

              </div>
            </v-container>
          </v-row>

          <!-- 실시간 시간 표시 -->
          <v-row class="d-flex justify-end">
            <p class="text-right ma-0">{{nowDate}} {{nowTime}} 실시간</p>
          </v-row>
        </v-container>
      </v-card-text>
    </v-card>

    <!-- 2. 오늘의 유저 -->
    <v-card class="mx-auto mb-5 purple-back-gradation rounded-xl" height ="auto">
      <v-card-text class="py-5 px-3">
        <v-container>
        
          <!-- 전체제목 -->
          <v-row class="mt-2">
            <v-col class="pa-0">
              <p class="d-flex justify-center mb-0 color-purple font-weight-bold">🎈 유저 랭킹</p>
            </v-col>
          </v-row>

          <!-- 랭커 -->
          <v-row class="mt-7">
            <v-container class="pa-0 mb-2">
              <!-- v-for문 돌릴것들 -->
              <!-- 각 유저 -->
              <v-row>
                <v-container class="pa-0 mb-2">
                  <!-- 설명 -->
                  <v-row class="mb-2">
                    <!-- 등수 -->
                    <v-col cols="3" class="pa-0 black--text font-weight-bold text-center">등수</v-col>
                    <!-- 유저이름 -->
                    <v-col cols="6" class="pa-0 black--text font-weight-bold text-center">유저이름</v-col>
                    <!-- 포인트 -->
                    <v-col cols="3" class="pa-0 black--text font-weight-bold text-center">포인트</v-col>
                    <!-- 문제풀이개수 -->
                    <!-- <v-col cols="2" class="pa-0 black--text font-weight-bold text-center">풀이수</v-col>      -->
                  </v-row>    

                  <!-- v-for문 돌릴것들 -->
                  <!-- 각 유저 -->
                  <!-- 인기 유저  0813 임지민-->
                  <div v-for="(popularUser, idx) in popularUsers" :key="idx" class="mb-2">
                    <v-row>
                      <!-- 등수 -->
                      <v-col cols="3" class="align-self-center pa-0 dark--text text-center font-weight-bold">{{idx+1}}</v-col>
                      <!-- 유저이름 -->
                      <v-col cols="6" class="pa-0 dark--text text-center" @click=profileEvent(popularUser.id)><v-btn plain top class="pa-0">{{popularUser.name}}</v-btn></v-col>
                      <!-- 포인트 -->
                      <v-col cols="3" class="align-self-center pa-0 dark--text text-center">{{popularUser.point}}</v-col>
                      <!-- 문제풀이개수 -->
                      <!-- <v-col cols="2" class="pa-0 dark--text text-center">21</v-col>      -->
                    </v-row>    
                  </div>
                </v-container>
              </v-row>
              <!-- 여기까지를 v-for문 돌리면 됨 -->
            </v-container>
          </v-row>

          <!-- 실시간 시간 표시 -->
          <v-row class="d-flex justify-end">
            <p class="text-right ma-0">{{nowDate}} {{nowTime}} 실시간</p>
          </v-row>
        </v-container>
      </v-card-text>
    </v-card>
  </v-container>
</template>



<script>
import { mapGetters } from 'vuex';
import axios from 'axios'
import drf from '@/api/drf.js'

export default {
  name: "SideBar",
  components : {
  }, 
  data () {
    return {
      timer: null,
      nowDate: '',
      nowTime: '',
      // inputData: null,
      items: [
      ],
      popularProbs: null,
      popularUsers: null,

    }
  },
  computed: {
    ...mapGetters(['userName','isLoggedIn',]),
    isSearched() {
      return this.$store.getters['problem/isSearched']
    }
  },
  mounted () {
    this.timer = setInterval(() => {
      //console.log("이름 = ", this.userName);
      //console.log("로그인 확인 : ", this.isLoggedIn)
    this.setNowTimes()
    },1000)

  },
  methods: {
    profileEvent(uid) {
      this.$router.push({ path: `../profile/${uid}`})
      this.$router.go()
    },
    problemEvent(pid) {
      this.$router.push({ path: `../problem/${pid}`})
      this.$router.go()
    },
    setNowTimes() {
      let myDate = new Date()
      let mm = myDate.getMonth() + 1
      let dd = String(myDate.getDate() < 10 ? '0' + myDate.getDate() : myDate.getDate())
      let hou = String(myDate.getHours() < 10 ? '0' + myDate.getHours() : myDate.getHours())  
      let min = String(myDate.getMinutes() < 10 ? '0' + myDate.getMinutes() : myDate.getMinutes())  
      let sec = String(myDate.getSeconds() < 10 ? '0' + myDate.getSeconds() : myDate.getSeconds()) 
      this.nowDate = mm + '월 ' + dd + '일'
      this.nowTime = hou + ':' + min + ':' + sec 
    },
    logout () {
      console.log("logout click");
      this.$store.dispatch('removeToken', "")
      this.$store.dispatch('removeName', "")
      sessionStorage.setItem('accessToken', "")
      sessionStorage.setItem('currentUser', "")

      axios({
          url: drf.accounts.logout(),
          method: 'delete',
          headers: {
            Authorization: this.accessToken,
          },
      })
      .catch(err =>{
          console.log("에러")
          console.log(err.response.status)
      })
    },
    // 유저 정보 모두 가져와서 문제 많이 푼 횟수로 3개 가져오기
    // sidebarPopularUser() {
    //     axios({
    //             url: drf.accounts.login(),
    //             method: 'post',
    //             data: this.credentials
    //         })
    //         .then(res => {
    //             console.log("res = ",res);
    //             console.log("accessToken = ",res.data.accessToken);
    //             let grantType = res.data.grantType.replace(res.data.grantType.charAt(0), res.data.grantType.charAt(0).toUpperCase());
    //             console.log("grantType:", grantType);
    //             this.$store.dispatch('saveToken', grantType+" "+res.data.accessToken)
    //             this.$store.dispatch('saveName', res.data.name)
    //             this.$router.push({ path: '/'})
    //         })
    //         .catch(err =>{
    //             console.log("에러")
    //             console.log(err)
    //         })
    //   },
  },
  created() {
    // 인기 문제 0813 임지민
    console.log("사이드바 현재 유저 : ", this.isLoggedIn)
    axios({
      url: drf.postFeed.problem() + 'ranking/',
      method: 'get',
      headers: {
        Authorization: this.accessToken,
      },
    })
      .then((res) => {
        console.log('res sidebar= ', res);
        this.popularProbs = res.data
        // console.log(this.popularProbs)
        // this.$router.push({ path: 'profile' })
      })
      .catch((err) => {
        console.log('에러');
        console.log(err);
      });

    // 인기 유저 0813 임지민
    axios({
      url: drf.accounts.ranking(),
      method: 'get',
      headers: {
        Authorization: this.accessToken,
      },
    })
      .then((res) => {
        // console.log('res sidebar user= ', res);
        this.popularUsers = res.data
        // console.log(this.popularUsers)
        // this.$router.push({ path: 'profile' })
      })
      .catch((err) => {
        console.log('에러');
        console.log(err);
      });
  }
}
</script>

<style>
.btn {
  color: aqua;
}
.color-purple {
  color: #512DA8;
  font-size: 1.5em;
}
.color-magenta {
  color: #C2185B;
  font-size: 1.5em;
}
.pink-gradation {
  background: linear-gradient(#E7C0F4, #F0BBCF);
}
.purple-back-gradation {
  background: linear-gradient(#D4B4FF, #D9DFFF);
}
.title-font-size {
  font-size: 1.1em;
}
.circle-background {
  background: #FFF4F8;
  height: 65px;
  width: 65px;
  border-radius: 50%;
}
</style>