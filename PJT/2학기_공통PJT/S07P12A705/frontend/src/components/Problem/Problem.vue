<template>
  <v-container mt-5>
    <v-row class="justify-space-between mt-5">
      <div class="d-flex mt-5">
        <!-- <p>{{probDetail}}</p> -->
        <h2>{{ probDetail.title }}</h2>
        <div class="d-inline-block ms-3" v-if="showCorrectStatus">
          <v-btn v-if="myCorrectStatus" rounded small outlined color="green">정답</v-btn>
          <v-btn v-else rounded small outlined color="red">오답</v-btn>
        </div>
      </div>
      <v-btn @click="goBack()" text class="font-weight-bold mt-5">뒤로가기</v-btn>
    </v-row>
    <!-- <p>{{probDetail}}</p> -->
    <v-row>
      <div v-for="tag in probDetail.tags" :key="tag" class="ms-2 mb-3">
        <v-chip color="#926DFF" class="white--text ms-3">{{tag}}</v-chip>
      </div>
    </v-row>

    <v-row>
      <v-col cols="12">
        <p class="font-parent-lar black--text my-4">
          {{ probDetail.mainText }}
        </p>
          
      </v-col>
    </v-row>

    <v-row>
      <v-container>
        <!-- 문제보기: 이것도 랜덤으로 for문 돌리기 -->
        <v-form @submit.prevent="submitProblem">
          <v-row>
            <v-col>
              <div v-for="example in examples" :key="example.id" class="my-3">
                <input type="radio" :value="`보기${example.id}`" :id="example.id" name="bogey">
                <label :for="`check${example.id}`" 
                class="ml-2 font-parent-mid-l">
                {{example.example}} </label>
              </div>
            </v-col>
          </v-row>
          <!-- 저작권 / 버튼 -->

          <v-row class="d-flex justify-space-between">
            <!-- 출제자 정보 -->
            <v-col class="pa-0" >
              <span class="grey--text mr-2 mb-1">Created by.
                <v-btn class="px-0 mb-1 font-weight-bold" plain @click=profileEvent(probDetail.writer.id)>                        
                  {{probDetail.writer.name}} 
                </v-btn>
              </span>
            </v-col>

            <!-- 버튼: 남이 낸 문제 -->
            <v-col v-if="currentUser != probDetail.writer.id" cols="8" class="pa-0 justify-end d-flex align-center">
              <!-- 좋아요 버튼 -->
              <div>
                <v-btn class="ms-1" icon color="dark lighten-2" @click="changeLikeStatus" id="upIcon" large>
                  <v-icon>{{upText}}</v-icon>
                </v-btn>
                <span>{{probDetail.numOfLikes}}</span>
              </div>
              <!-- 싫어요 버튼 -->
              <div>
                <v-btn class="ms-1" icon color="dark lighten-2" @click="changeHateStatus" id="downIcon" large>
                  <v-icon>{{downText}}</v-icon>
                </v-btn>
                <span>{{probDetail.numOfDislikes}}</span>
              </div>
              <!-- 스크랩 버튼 -->
              <v-btn class="ms-2" icon color="dark lighten-2" @click="openScrapModal" id="scrapIcon" large>
                <v-icon>{{scrapText}}</v-icon>
              </v-btn>
              <scrap @close="closeScrapModal" v-if="scrapModal" :pid="probDetail.id"></scrap>                    
              <!-- 제출 버튼 -->
              <v-btn type="submit" rounded outlined class="ms-1" large>제출</v-btn>
            </v-col>

            <!-- 내가 낸 문제 -->
            <v-col v-else cols="8" class="pa-0 justify-end d-flex align-center">
              <!-- 스크랩 버튼 -->
              <v-btn class="ms-2" icon color="dark lighten-2" @click="openScrapModal" id="scrapIcon" large>
                <v-icon>{{scrapText}}</v-icon>
              </v-btn>
              <!-- 삭제 -->
              <v-btn type="submit" color="red" rounded outlined class="ms-1" large @click="deleteprob">삭제</v-btn>
            </v-col>

          </v-row>
        </v-form>
      </v-container>
    </v-row>

    <v-divider color="#A384FF" class="mt-3"></v-divider>
      
    <v-row>
      <!-- 댓글보기 -->
      <v-col cols="12" class="pa-0">
        <!-- <p>{{probDetail.id}}</p> -->
        <problem-reply :pid="probDetail.id" :commentList="commentList"></problem-reply>
      </v-col>           
    </v-row>  
  </v-container>
</template>

<script>
import ProblemReply from '@/components/ProblemModal/ProblemReply.vue'
import { mapGetters } from 'vuex'
import axios from 'axios'
import drf from '@/api/drf.js'
import Scrap from '@/components/Scrap/Scrap.vue'


export default {
  name: 'Problem',
  data(){
    return {
      scrapModal: false,
      upText: 'thumb_up_off_alt',
      downText: 'thumb_down_off_alt',
      scrapText: 'bookmark_border',
      probDetail: null,
      examples: [],
      credentials: {
        pid: '',
        right: '',
        wrongAnswer: '',
      },
      showCorrectStatus: false,
      myCorrectStatus: null,
      commentList: [],
    }
  },
  components: {
    ProblemReply,
    Scrap,
  },
  computed: {
    ...mapGetters(['accessToken', 'currentUser'])
  },
  methods: {
    // 2022.08.04. 라우터 경로 연결
    goBack () {
      this.$router.go(-1)
    },
    changeLikeStatus() {
        /* 
        버튼 클릭하면 색이 바뀌도록
        thumb up --> thumb up off alt
        thumb down --> thumb down off alt
        bookmark border --> bookmark
        */
       // 좋아요 엑쇼스 0815 임지민
        // axios 보내기
          axios({
            url: drf.postFeed.likeordis(),
            method: 'post',
            headers: {
              Authorization: this.accessToken,
            },
            data: {
              pid: this.probDetail.id,
              type: true
            }
          })
          .then(res => {
            console.log(res.data);
            this.probDetail.numOfLikes = res.data.numOfLikes
            if(res.data.numOfLikes === 1) {
              this.upText = 'thumb_up'
            } else {
              this.upText = 'thumb_up_off_alt'
            }

          })
          .catch(err => {
            // console.log(this.accessToken)
            // console.log(this.userId)
            console.log(err);
          })
            /* 싫어요가 눌려 있는 상태에서 좋아요를 누르면 싫어요가 취소되는 것도 추가 */
    
            if (this.upText === "thumb_up_off_alt") {
              // 좋아요를 눌러야 하는데 이미 싫어요가 눌려져 있는 상태
              if (this.downText === "thumb_down") {
                  // console.log(this.downText)
                  this.changeHateStatus()
                  this.downText = "thumb_down_off_alt"
              }
              this.upText = "thumb_up"
              } else {
                this.upText = "thumb_up_off_alt"
              }
    },
    changeHateStatus() {
       // 싫어요 엑쇼스 0815 임지민
        // axios 보내기
          axios({
            url: drf.postFeed.likeordis(),
            method: 'post',
            headers: {
              Authorization: this.accessToken,
            },
            data: {
              pid: this.probDetail.id,
              type: false
            }
          })
          .then(res => {
            console.log(res.data);
            this.probDetail.numOfDislikes = res.data.numOfDislikes
            
          })
          .catch(err => {
            // console.log(this.accessToken)
            // console.log(this.userId)
            console.log(err);
          })
          /* 좋아요가 눌려 있는 상태에서 싫어요를 누르면 좋아요가 취소되는 것도 추가 */
        if (this.downText === "thumb_down_off_alt") {
            this.downText = "thumb_down"
            // 싫어요를 눌렀는데 이미 좋아요가 눌러져 있는 상태
            if (this.upText === "thumb_up") {
                this.changeLikeStatus()
                this.upText = "thumb_up_off_alt"
            }
       } else {
            this.downText = "thumb_down_off_alt"
       }
    },
    changeScrapStatus() {
       if (this.scrapText === "bookmark_border") {
            this.scrapText = "bookmark"
       } else {
            this.scrapText = "bookmark_border"
       }
    },
    async openScrapModal() {
      await this.$store.dispatch('reIssue');
        this.scrapModal = true
        console.log('openModal')
    },
    closeScrapModal() {
        this.scrapModal = false
        console.log('closeModal')
    },
    profileEvent(uid) {
      this.$router.push({ path: `../profile/${uid}`})
    },
    // 문제 풀기; 문제 푼 후 결과 저장(0811 임지민)
    submitProblem() {
      // 문제 맞는 지 틀린 지 먼저 확인하고
      // 이게 null이면 답을 선택하라는 alert 창 띄우기
      const selectedAnswer = document.querySelector('input[name="bogey"]:checked').id
      // console.log(selectedAnswer)
      this.credentials.wrongAnswer = selectedAnswer
      if (selectedAnswer === "1") {
        this.credentials.right = true
        this.myCorrectStatus = true
        // alert('정답입니다.')
        this.$swal({
          icon: 'success',
          text: '정답입니다'
        })
      } else {
        this.credentials.right = false
        // alert('오답입니다.')
        this.$swal({
          icon: 'warning',
          text: '오답입니다.'
        })
        this.myCorrectStatus = false

      }
      this.showCorrectStatus = true

      // console.log(this.credentials)
      // axios 보내기
      axios({
        url: drf.solving.solving(),
        method: 'post',
        headers: {
          Authorization: this.accessToken,
        },
        data: this.credentials
      })
      .then(res => {
        // 받아온 데이터를 작성 전/후로 구분하는 작업 필요(0808 임지민)
        console.log(res)
      })
      .catch(err => {
        // console.log(this.accessToken)
        // console.log(this.userId)
        console.log(err);
      })
    },
    getProbDetail() {
      // console.log('problem ')
    const probId = this.$route.params.pid
    // console.log('probid=', probId)

    axios({
      url: drf.api + 'post/' + `${probId}`,
      method: 'get',
      headers: {
        Authorization: this.accessToken,
      },
    })
    .then(res => {
      console.log(res) //ok
      this.probDetail = res.data

      // 댓글이 있는 경우에만 0815 임지민
      if (res.data.comments){
        this.commentList = res.data.comments.reverse()
        this.commentLength = this.commentList.length
      } 

      // console.log(res.data.comments)
      if (this.examples.length===0) {
        const nums  = [1,2,3,4]
        const shuffled = nums.sort(() => Math.random() - 0.5)
        // const noteDetail = this.noteDetail
        // this.shuffledNum = shuffled
        nums.forEach(num => {
          // console.log(num);
          // console.log(this.probdetail[`example${num}`])
          this.examples.push({'id': num, 'example': this.probDetail[`example${num}`]})
          })
        }
      })
      .catch(err => {
        console.log(err);
      })
    },

    // 내가 낸 문제 삭제하기(0815 오채명)
    deleteprob() {
      const userDecision = confirm('정말로 삭제하시겠습니까?')
      if (userDecision) {
        axios({
          url: drf.api + 'post' + `/${this.probDetail.id}`,
          method: 'delete',
          headers: {
            Authorization: this.accessToken,
          },
        })
        .then(res => {
          console.log("res.data = ",res.data)
          // console.log("삭제 되었습니다. ", res)
          this.$router.push('/')
        })
        .catch(err =>{
          console.log("에러")
          console.log(err)
        })
        this.$router.go(); // 새로고침
      }
    },
  },
  created() {
    this.getProbDetail()
  },
}
</script>

<style>

</style>