<template>
  <!-- 2022.07.26 문제 모달 (남성은) -->
  <!-- 2022.08.03 댓글보기 버튼 활성화 (남성은) -->
  <v-container class="modal" appear>
    <v-container class="modal modal-overlay" @click.self="$emit('close')">
      <v-container class="modal-window pa-0">
        <v-container class="rounded-lg modal-content pa-0">
          <v-row class="d-flex justify-center px-3 problem-modal-white">
            <!-- 문제부분 (처음에 떠있음) -->
            <v-col id="modal-content-window" class="pa-0">
              <!-- <slot name="btns">
              </slot>               -->
              <v-card-text class="d-flex justify-space-between align-center px-0">
                <v-btn @click="event(probdetail.id)" text class="font-weight-bold pr-0 pl-3" small>자세히</v-btn>
                <v-btn @click="$emit('close')" icon class="pa-0"><v-icon>mdi-close</v-icon></v-btn>
              </v-card-text>    

              <!-- 문제 제목 -->
              <!-- {{ problem.pk }}. {{ problem.MAIN_TEXT}} -->
              <v-card-title class="font-weight-bold">
                <p class="font-parent-lar mb-0">{{probdetail.title}}</p> 
                <div class="ms-3" id="correctStatus" v-if="showCorrectStatus">
                  <v-chip v-if="myCorrectStatus" rounded small outlined color="green" class="px-1"><v-icon color="green" small>mdi-circle</v-icon>정답</v-chip>
                  <v-chip v-else rounded small outlined color="red" class="px-1"><v-icon color="red" small>mdi-circle</v-icon>오답</v-chip>
                </div>
              </v-card-title>

              <!-- 문제 본문 -->
              <v-card-text class="d-flex">
                <!-- 카테고리 라벨 -->
                <!-- {{probdetail}} -->
                <!-- {{probdetail.id}} -->
                <div class="mt-5" v-for="(tag, idx) in probdetail.tags" :key="idx">
                  <v-chip small color="#926DFF" class="white--text ms-3">{{tag}}</v-chip>
                </div>  
              </v-card-text>

              <!-- 문제 -->
              <v-card-text class="font-weight-bold">
                <!-- <h2 class="black--text">
                다음 설명에 맞는 장치로 적절한 것은 무엇인가요?
                </h2>
                문제지문
                <h3 class="black--text my-4">
                  컴퓨터에는 (       )라고 불리는 굉장히 많은 스위치가 있고,<br>
                  on/off 상태를 통해 0과 1을 표현합니다.
                </h3> -->
                <!--  문제가 길어지면 모달이 화면 전체만큼 커져서 크기를 450px로 고정함 0811 임지민 -->
                <div>
                  <!-- <p>{{probdetail}}</p> -->
                  <h3>{{probdetail.mainText}}</h3>
                </div>

                <div>
                  <v-container>
                    <!-- 문제보기: 이것도 랜덤으로 for문 돌리기/ 체크박스로 라디오 묶는거....ㅠ-->
                    <v-form @submit.prevent="submitProblem">
                      <v-row>
                        <v-col>
                          <div v-for="example in examples" :key="example.id" class="my-3">
                            <div class="d-flex">
                              <input type="radio" :value="`보기${example.id}`" :id="example.id" name="bogey">
                              <label :for="`check${example.id}`" 
                              class="ml-2 font-parent-mid-l">
                              <h3>{{example.example}}</h3></label>
                            </div>                        
                          </div>
                        </v-col>
                      </v-row>
                      <!-- 저작권 / 버튼 -->
                      <v-row class="justify-space-between">
                        <!-- 출제자 정보 -->
                        <div class="pa-0" >
                          <span class="grey--text mr-2 mb-1">Created by.
                            <v-btn class="px-0 font-weight-bold" plain @click="profileEvent(probdetail.writer.id)">                        
                              {{probdetail.writer.name}} 
                            </v-btn>
                          </span>
                        </div>

                        <!-- 내가 낸 문제가 아닐 경우 -->
                      
                        <div v-if="currentUser != probdetail.writer.id" class="pa-0 justify-end d-flex align-center">
                          <!-- 좋아요 버튼 -->
                          <div>
                            <v-btn class="ms-1" icon color="dark lighten-2" @click="changeLikeStatus" id="upIcon">
                              <v-icon>{{upText}}</v-icon>
                            </v-btn>
                            <span>{{probdetail.numOfLikes}}</span>
                          </div>
                          <!-- 싫어요 버튼 -->
                          <div>
                            <v-btn class="ms-1" icon color="dark lighten-2" @click="changeHateStatus" id="downIcon">
                              <v-icon>{{downText}}</v-icon>
                            </v-btn>
                            <span>{{probdetail.numOfDislikes}}</span>
                          </div>
                          <!-- 스크랩 버튼 -->
                          <div v-if="isLoggedIn">                   
                              <v-btn class="ms-1" icon color="dark lighten-2" @click="openScrapModal"  id="scrapIcon">
                              <v-icon>{{scrapText}}</v-icon>
                              </v-btn>   
                          </div>
                          
                            <!-- 스크랩 모달 -->
                          <div>  
                            <scrap @close="closeScrapModal" v-if="scrapModal" :pid="probdetail.id"></scrap>
                            <!-- 제출 버튼 -->
                            <v-btn type="submit" rounded outlined class="ms-1" small>제출</v-btn>
                          </div>
                        </div>
                        
                        <!-- 내가 낸 문제 일 경우 -->
                        <div v-else class="pa-0 justify-end d-flex align-center">
                          <!-- 스크랩 버튼 -->
                          <div v-if="isLoggedIn">
                            <v-btn class="ms-1" icon color="dark lighten-2" @click="openScrapModal" id="scrapIcon">
                              <v-icon>{{scrapText}}</v-icon>
                            </v-btn>
                            
                            <scrap @close="closeScrapModal" v-if="scrapModal" :pid="probdetail.id"></scrap>
                            <!-- 수정 -->
                            <!-- <v-btn type="submit" rounded outlined class="ms-1" small @click="updateprob">수정</v-btn> -->
                            <!-- 삭제 -->
                            <v-btn type="submit" color="red" rounded outlined class="ms-1" small @click="deleteprob">삭제</v-btn>
                          </div>
                        </div>
                      </v-row>
                    </v-form>
                  </v-container>

                  <v-divider></v-divider>

                  <!-- 댓글보기 / 본문보기 -->
                  <v-btn @click="showReplies" class="font-weight-bold mt-2" text>댓글보기</v-btn>
                </div>            
              </v-card-text>
            </v-col>   

            <!-- 댓글부분 (댓글보기 누를시 바뀜 떠있음) -->
            <v-col id="reply-window" class="d-none">
              <v-card-text class="pa-0">
                <div>
                  <problem-reply :pid="probdetail.id" :commentList="commentList"></problem-reply>

                  <v-divider class="mx-1"></v-divider>

                  <!-- 댓글보기 / 본문보기 -->
                  <v-btn @click="noShowReplies" class="font-weight-bold mt-2 mb-4" text>본문보기</v-btn>
                </div>            
              </v-card-text>
            </v-col>
                        
          </v-row>
        </v-container>
      </v-container>
    </v-container>
  </v-container>
</template>

<script>
import drf from '@/api/drf'
import axios from 'axios'
import ProblemReply from './ProblemReply.vue'
import Scrap from '@/components/Scrap/Scrap.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'ProblemModal',
  components: {
    ProblemReply,
    Scrap,
  },
  data () {
    return {
      scrapModal: false,
      upText: 'thumb_up_off_alt',
      downText: 'thumb_down_off_alt',
      scrapText: 'bookmark_border',
      probId: 0,
      // probdetail: [],
      examples: [],
      credentials: {
        pid: '',
        right: '',
        wrongAnswer: '',
      },
      showCorrectStatus: false,
      myCorrectStatus: null,
      commentList: null,
      probdetail: []
    }
  },
  props: {
    mainProb: Object,
    // probdetail: Object,
  },
  computed: {
    ...mapGetters(['accessToken', 'currentUser', 'isLoggedIn'])
  },
  methods: {
    changeLikeStatus() {
      if (this.isLoggedIn){
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
              pid: this.probdetail.id,
              type: true
            }
          })
          .then(res => {
            // 받아온 데이터를 작성 전/후로 구분하는 작업 필요(0808 임지민)
            console.log(res)
            this.probdetail.numOfLikes = res.data.numOfLikes

          })
          .catch(err => {
            // console.log(this.accessToken)
            // console.log(this.userId)
            console.log(err);
          })
          /* 싫어요가 눌려 있는 상태에서 좋아요를 누르면 싫어요가 취소되는 것도 추가 */
        // console.log(document.querySelector('#correctStatus'));
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
      }
    },
    changeHateStatus() {
      if (this.isLoggedIn){
  
       // 싫어요 엑쇼스 0815 임지민
        // axios 보내기
          axios({
            url: drf.postFeed.likeordis(),
            method: 'post',
            headers: {
              Authorization: this.accessToken,
            },
            data: {
              pid: this.probdetail.id,
              type: false
            }
          })
          .then(res => {
            // 받아온 데이터를 작성 전/후로 구분하는 작업 필요(0808 임지민)
            console.log(res)
            this.probdetail.numOfDislikes = res.data.numOfDislikes

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
        if (this.isLoggedIn){
        this.scrapModal = true
        console.log('openModal')
        }
    },
    closeScrapModal() {
        this.scrapModal = false
        console.log('closeModal')
    },

    // 2022.08.03. 댓글보기 버튼 누를 때
    showReplies: function (event) {
      const modalContentWindow = document.querySelector("#modal-content-window")
      const replyWindow = document.querySelector("#reply-window")
      modalContentWindow.setAttribute('class', 'd-none')
      replyWindow.setAttribute('class', 'pa-0 col')
    },
    // 2022.08.03. 댓글접기 버튼 누를 때
    noShowReplies: function (event) {
      const modalContentWindow = document.querySelector("#modal-content-window")
      const replyWindow = document.querySelector("#reply-window")
      modalContentWindow.setAttribute('class', 'pa-0 col')
      replyWindow.setAttribute('class', 'd-none')    
    },
    // 2022.08.04. 라우터 경로 연결
    event(pid) {
      // console.log('pid=', pid)
      this.$router.push({ path: `problem/${pid}`})
    },
    profileEvent(uid) {
      this.$router.push({ path: `profile/${uid}`})
    },
    // 문제 풀기; 문제 푼 후 결과 저장(0811 임지민)
    submitProblem() {
      // 문제 맞는 지 틀린 지 먼저 확인하고
      // 이게 null이면 답을 선택하라는 alert 창 띄우기
      // const correctStatus = document.querySelector('#correctStatus')
      const selectedAnswer = document.querySelector('input[name="bogey"]:checked').id
      // console.log(selectedAnswer)
      this.credentials.wrongAnswer = selectedAnswer
      if (selectedAnswer === "1") {
        this.credentials.right = true
        this.$swal({
          icon: 'success',
          text: '정답입니다'
        })
        this.myCorrectStatus = true
        // alert('정답입니다.')
      } else {
        this.credentials.right = false
        // alert('오답입니다.')
        this.$swal({
          icon: 'error',
          text: '오답입니다'
        })
        this.myCorrectStatus = false

        // this.$router
      }
      this.showCorrectStatus = true

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
    
    // 내가 낸 문제 삭제하기(0812 오채명)
    deleteprob() {
      const userDecision = confirm('정말로 삭제하시겠습니까?')
      if (userDecision) {
        axios({
          url: drf.api + 'post' + `/${this.probId}`,
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

    // 내가 낸 문제 수정하기(0812 오채명)
    // updateprob() {
    //   axios({
    //     url: drf.api + 'post'
    //   })
    // }
    getProbDetail() {
      // console.log("problem id를 확인해볼까 = ", this.mainProb.id)
      this.probId = this.mainProb.id
      this.credentials.pid = this.mainProb.id
    
      axios({
        url: drf.api + 'post' + `/${this.probId}`,
        methods: 'get',
        headers: {
          Authorization : this.accessToken,
        },      
      })
      .then(res => {
        // console.log(res.data)
        this.probdetail = res.data
        if (res.data.comments){
          this.commentList = res.data.comments.reverse()
        }
        console.log(this.examples.length);
        if (this.examples.length===0){
          const nums  = [1,2,3,4]
          const shuffled = nums.sort(() => Math.random() - 0.5)
          // const noteDetail = this.noteDetail
          // this.shuffledNum = shuffled
          nums.forEach(num => {
            // console.log(num);
            // console.log(this.probdetail[`example${num}`])
            this.examples.push({'id': num, 'example': this.probdetail[`example${num}`]})
          })
        }
      })
      .catch(err => {
        console.log("에러")
        console.log(err)
      })
    }
  },
  created() {
    this.getProbDetail()
    
  },

  
}
</script>

<style>
.problem-modal-white {
  background-color: #EDE7F6;
}
#modal-content-window {
  min-width: 450px;
}
#reply-window{
  min-width: 450px;
}
</style>

<style lang="stylus" scoped>
.modal {
  &.modal-overlay {
    display: flex;
    align-items: center;
    justify-content: center;
    position: fixed;
    z-index: 30;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
  }

  &-window {
    background: whitesmoke;
    border-radius: 4px;
    overflow: hidden;
    width: auto;
  }

  &-content {
    padding: 10px;
    width: 100%;
    height: 100%
  }
}

// 오버레이 트랜지션
.modal-enter-active, .modal-leave-active {
  transition: opacity 0.4s;

  // 오버레이에 포함되어 있는 모달 윈도의 트랜지션
  .modal-window {
    transition: opacity 0.4s, transform 0.4s;
  }
}

// 딜레이가 적용된 모달 윈도가 제거된 후에 오버레이가 사라짐
.modal-leave-active {
  transition: opacity 0.6s ease 0.4s;
}

.modal-enter, .modal-leave-to {
  opacity: 0;

  .modal-window {
    opacity: 0;
    transform: translateY(-20px);
  }
}
</style>