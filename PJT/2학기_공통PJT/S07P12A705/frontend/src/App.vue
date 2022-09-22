<template>
  <!-- <v-app :class="bgColor" @resize="selectBgColor"> -->
  <v-app :class="bgColor">
    <v-container class="px-0 px-md-3">
      <!-- sm 이하일 때 로고 나오도록 -->
      <v-row id="sm-logo" class= "d-flex d-md-none pb-0 mt-3 justify-space-between px-5">
        <div>
          <router-link to="/">
            <v-img src="./assets/prosn_logo.png" max-width="150px" max-height="50px"></v-img>
          </router-link>
        </div>
        <div class="d-flex">
          <v-col class="justify-center pa-0">
            <li style="list-style: none;" v-if="!isLoggedIn">
              <router-link to="/signup"><v-btn class="pa-0" x-large rounded-sm color="#a384ff" width="100%" text>signup</v-btn></router-link>
            </li>
            <li style="list-style: none;" v-if="isLoggedIn">
              <router-link to="/profile"><v-btn class="pa-0" x-large rounded-sm color="#a384ff" width="100%" text>{{ userName }}</v-btn></router-link>
            </li>
          </v-col>
      
          <v-col class="justify-center pa-0">
            <li style="list-style: none;" v-if="!isLoggedIn">
              <router-link to="/login"><v-btn class="pa-0" x-large rounded-sm color="#a384ff" width="100%" text>login</v-btn></router-link>
            </li>
            <li style="list-style: none;" v-if="isLoggedIn">
              <v-btn class="pa-0" x-large rounded-sm color="#a384ff" width="100%" text @click="logout">logout</v-btn>
            </li>
          </v-col>
        </div>
      </v-row>

      <v-row class="mt-0">
        <v-col cols="2" :class="`${navDisplayCol}`">
          <nav-bar id="navBarTag" :class="navDisplay"></nav-bar>
        </v-col>

        <v-col class="pt-0 px-0 px-md-3">
          <!-- url이 변경됨에 따라 계속 바뀌는 위치(0729 임지민) -->
          <!-- router/index.js에서 정의한 components의 컴포넌트를 띄워줌(0801 임지민) -->
          <router-view></router-view>

        <!-- sm 이하 일때: 아래 쪽에 네비게이션 바 -->
          <bottom-nav-bar class="d-flex d-md-none"></bottom-nav-bar>
        </v-col>
      </v-row>
    </v-container>
    <!-- <div class="nav">
      <nav-bar></nav-bar>
    </div>
    <div class="side">
      <side-bar></side-bar>
    </div> -->

    <!-- BottomNavBar md 이하일 때 남는 공간 만들기 위함 -->
    <v-container class="d-flex d-md-none mb-14" style="bottom: 0px">
    </v-container>  </v-app>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import BottomNavBar from '@/components/BottomNavBar.vue'
import SideBar from '@/components/SideBar.vue'
import MainPageView from '@/views/MainPageView.vue'
import { mapGetters } from 'vuex'


export default {
  name: 'App',
  data () {
    return{
      bgColor: 'bg-grey',
      navDisplay: 'd-flex',
      navDisplayCol: 'd-md-flex d-none',
      currentUrl: window.location.href
    }
  },
  components : {
    NavBar,
    BottomNavBar,
    SideBar,
    MainPageView,
  },
  computed: {
    ...mapGetters(['userName','isLoggedIn',]),
  },
  watch: {
    // currentUrl () {
    //   console.log('url changed-----------------------');
    // },
    /* 0805 임지민
      login, signup일 때는 navbar 안띄움
      아래 created까지 써줘야 새로 고침하면 navbar가 생기는 현상이 사라짐
    */
    $route(to, from) {
      console.log(to) // 도착지 login
      console.log(from) // 출발지 signUp
      // .v-application .d-sm-flex
      // const hiddenClass = document.querySelector('.v-application')
      if(to.name === 'login' || to.name === 'signUp') {
        // console.log('url changed-----------------------');
        this.navDisplay = 'd-none'
        this.navDisplayCol = 'd-none'
        const smLogo = document.querySelector('#sm-logo')
        smLogo.setAttribute('class', 'd-none')

      } else {
        this.navDisplay = 'd-flex'
        this.navDisplayCol = 'd-md-flex d-none'
      }
      
      // 로그인이 되어있지 않을 때, note, study를 url로 접근하려하면 막기
      // if (!this.isLoggedIn) {
      // const onlyAllowLoggedIn = [
      //   'study', 'note', 'noteDetail', 'createNote', 'createstudy', 'createproblem', 'createinfo', 'editstudy'
      // ]
      // onlyAllowLoggedIn.forEach(urlName => {
      //   console.log('로그인 해야 들어갈 수 있는 페이지');
      //   if (to.name === urlName || from.name === urlName) {
      //     this.$swal({
      //       icon: 'warning',
      //       text: '로그인 후 이용해주세요'
      //     })
      //     this.$router.push({path: '/login'})
      //     }
      //   })
      // }
      },
    },
    methods: {
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
      /*selectBgColor(){      
        // sm 이하에서는 배경색 흰색으로 바꾸기
        if (screen.innerWidth < 960){
          console.log('sml')
          this.bgColor = "white"
        } else {
          this.bgColor = "bg-grey"
        } 
      }, */
    },
    created() {
      // console.log('current url', location.href);
      // if($vuetify.breakpoint.sm) {console.log(true)}
      let currentUrl = location.href
      if (currentUrl.endsWith('login') || currentUrl.endsWith('signup')) {
        this.navDisplay = 'd-none'
        this.navDisplayCol = 'd-none'
        // 여기 진짜 무슨일이냐 매번
        const smLogo = document.querySelector('#sm-logo')
        smLogo.setAttribute('class', 'd-none')
      } else {
        this.navDisplay = 'd-flex'
        this.navDisplayCol = 'd-none d-md-flex'
      }
      // 로그인이 안되어 있을 때 url로 입력해서 접근하는 것 막기
      // console.log('현재 url type', currentUrl, typeof(currentUrl));
       const onlyAllowLoggedIn = [
        'study', 'note', 'createproblem', 'createinfo', 'editstudy'
      ]
      onlyAllowLoggedIn.forEach(urlName => {
        if (currentUrl.includes(urlName)){
          if (!this.isLoggedIn) {
            this.$swal({
              icon: 'warning',
              text: '로그인 후 이용해주세요'
            })
            this.$router.push({path: '/login'})
          }
        }
      })
    },  
  } 
</script>

<style scoped>
.app{
  height: 700px;
}
/* .nav{
  position: sticky; 
  float: left;
}
.side{
  float: right;
} */
/* .container에 최대 최소길이가 묶여있어서 마진이 많이 생겨서 조절해줌 */
.container {
  max-width: 1300px;
  min-width: none;
  /* border: 1px solid black; */
}
.bg-grey {
  background-color: #f5f5f5;
}
</style>