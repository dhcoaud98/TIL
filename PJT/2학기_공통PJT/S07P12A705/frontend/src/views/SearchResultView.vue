<template>
    <v-row>
      <!-- col 1: 메인 피드 부분 -->
      <v-col cols="12" md="8" class="mt-2 white">
        
        <!-- row 1-1: 검색 결과에 대해 데이터를 받아옴.(채명) -->
        <v-row>
          <search-bar>
          </search-bar>
          <h1 class="result ml-5" style="color:#A384FF" >
            {{ inputChange }}
          </h1> 
          <v-col>
            <span class="pt-5">에 대한 결과 입니다.</span>
          </v-col>
        </v-row>

        <v-divider></v-divider>

        <!-- row 1-2: 검색 결과에 대한 상단 탭; 문제/문제집, 정보 -->
        <v-toolbar dark class="mt-10 mx-4" height="45px">
          <v-tabs background-color="#CCA5FE" grow>
            <v-col class="px-0">
              <v-tab class="pa-0" @click="changeToProblemFeed">
                <p class="font-weight-regular text-center mb-0" style="font-size: 1.2rem">PROBLEM</p>
              </v-tab>            
            </v-col>
            <v-col class="px-0">
              <v-tab class="pa-0" @click="changeToBookFeed">
                <p class="font-weight-regular text-center mb-0" style="font-size: 1.2rem">BOOK</p>
              </v-tab>         
            </v-col>
            <v-col class="px-0">
              <v-tab class="pa-0" @click="changeToInfoFeed">
                <p class="font-weight-regular text-center mb-0" style="font-size: 1.2rem">INFORMATION</p>
              </v-tab> 
            </v-col>       
          </v-tabs>
        </v-toolbar>

        <!-- row 1-3: 피드 컨텐츠 부분 -->
        <v-row>
          <v-col>
            <!-- 메인 피드 1. -- 문제/문제집 -->
            <recent-problem id="problemFeed" :class="`${problemFeedClass}`"></recent-problem>
            <!-- 메인 피드 2. -- 문제집 -->
            <main-book id="BookFeed" :class="`${bookFeedClass}`" :mainBooks="mainBooks"></main-book>            
            <!-- 메인 피드 2. -- 정보 -->
            <info id="infoFeed" :class="`${infoFeedClass}`"></info>
          </v-col>
        </v-row>
      </v-col>

      <!-- col 2: 사이드 바 -->
      <v-col md="4" class="d-md-flex d-md-none grey lighten-4">
        <side-bar></side-bar>
      </v-col>
    </v-row>
</template>

<script>
import SideBar from '@/components/SideBar.vue'
import RecentProblem from '@/components/MainPage/RecentProblem.vue'
import Info from '@/components/MainPage/info.vue'
// import { mapGetters } from 'vuex';

export default {
  name: 'SearchResultView',
  components: {
    SideBar,
    RecentProblem,
    Info,
  },
  data() {
    return {
      fab: false,
      hidden: false,
      tabs: null,
      input: '',
      feedFlag: 0,
      problemFeedClass: 'd-flex',
      bookFeedClass: 'd-none',
      infoFeedClass: 'd-none',
      searchInput: null,
    }
  }, 
  created() {
    this.searchInput = this.inputChange
    console.log("서치 =",this.searchInput)
    // 0812 채명 : 검색 문제 엑시오스
    // axios({
    //   url: drf.api + 'post' + `/${this.probId}`,
    //   methods: 'get',
    //   headers: {
    //     Authorization : this.accessToken,
    //   },      
    // })
    // .then(res => {
    //   console.log(this.res)
    //   this.probdetail = res
    // })
    // .catch(err => {
    //   console.log("에러")
    //   console.log(err)
    // })
    // 0812 채명 : 검색 문제 엑시오스
  },  
  computed: {
    isSearched() {
      return this.$store.getters['problem/isSearched']
    },
    inputChange() {
      return this.$store.getters['problem/inputChange']
    },
    
  },
  methods: {
    changeToProblemFeed() {
      this.feedFlag = 0
      // console.log(this.feedFlag)
      this.problemFeedClass ='d-flex'
      this.bookFeedClass = 'd-none'
      this.infoFeedClass = 'd-none'
    },
    changeToBookFeed() {
      this.feedFlag = 1
      // console.log(this.feedFlag)
      this.problemFeedClass ='d-none'
      this.bookFeedClass = 'd-flex'
      this.infoFeedClass = 'd-none'
    },    
    changeToInfoFeed() {
      this.feedFlag = 2
      this.problemFeedClass ='d-none'
      this.bookFeedClass = 'd-none'
      this.infoFeedClass = 'd-flex'
    },
    // onInputChange: function(inputData) {
    //   // console.log(inputData)
    //   this.input = inputData
    // },
  //   changeToProblemFeed() {
  //     this.feedFlag = 0
  //     // console.log(this.feedFlag)
  //      // 2. 해당 탭에 불 들어오게
  //       const problemTab = document.querySelector('#problemTab')
  //       const infoTab = document.querySelector('#infoTab')
  //       problemTab.classList.add("clicked-main-tab")
  //       // console.log(problemTab.classList)
  //       if(infoTab.classList.length > 6){
  //         infoTab.classList.remove("clicked-main-tab")
  //       }
  //       this.problemFeedClass ='d-flex'
  //       this.infoFeedClass = 'd-none'
  //   },
  //   changeToInfoFeed() {
  //     this.feedFlag = 1
  //     // console.log(this.feedFlag)

  //     const problemTab = document.querySelector('#problemTab')
  //     const infoTab = document.querySelector('#infoTab')
  //     infoTab.classList.add("clicked-main-tab")
  //       // console.log(infoTab.classList)
  //       if(problemTab.classList.length > 6){
  //         // console.log('hi')
  //         problemTab.classList.remove("clicked-main-tab")
  //       }
  //       this.problemFeedClass ='d-none'
  //       this.infoFeedClass = 'd-flex'
  //   },
  }
}
</script>

<style>
  .bottom-line {
    border-bottom: #a384ff 3px solid;
  }
  .v-application--wrap {
  max-width: none;
  }
  
  /* before로 색을 지정해주니까 hover 했을 때 색이 흰색으로 정상적으로 바뀜 */
  .tab-hover::before {
    color: #616161;
  }
  :hover.tab-hover,
  .clicked-main-tab
   {
    background: #a384ff;
    color: white;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    cursor: pointer;
  }
  .container {
    max-width: none;
  }
  .w-100 {
    width: 100%;
  }
  

</style>