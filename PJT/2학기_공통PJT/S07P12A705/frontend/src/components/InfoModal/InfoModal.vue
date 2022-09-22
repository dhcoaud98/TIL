<template>
  <!-- 2022.07.26 정보 모달 (남성은) -->
  <!-- 2022.08.04 댓글보기 버튼 활성화 (남성은) -->
  <v-container class="modal" appear>
    <v-container class="modal modal-overlay" @click.self="$emit('close')">
      <v-container class="modal-window pa-0">
        <v-container class="rounded-lg modal-content pa-0">
          <v-row class="d-flex justify-center px-3 info-modal-white">
            <!-- 정보부분 (처음에 떠있음) -->
            <v-col id="modal-content-window" class="pa-0">            
              <v-card-text class="d-flex justify-space-between align-center px-0">
                <v-btn @click="event()" text class="font-weight-bold pr-0 pl-3" small>자세히 보기</v-btn>
                <v-btn @click="$emit('close')" icon class="pa-0"><v-icon>mdi-close</v-icon></v-btn>
              </v-card-text>

              <!-- 정보 제목 -->
              <v-card-title class="font-weight-bold black--text">
                <h2>{{ info.title }}</h2> 
              </v-card-title>

              <!-- 정보 본문 -->
              <v-card-text class="d-flex pb-0">
                <!-- 카테고리 라벨 -->
                <div class="mt-5" v-for="(tag, idx) in infodetail.tags" :key="idx">
                  <v-chip small color="#926DFF" class="white--text ms-3">{{tag}}</v-chip>
                </div>
              </v-card-text>

              <!-- 내용 -->
              <v-card-text class="font-weight-bold">
                <v-container class="px-0">
                  <v-row>
                    <v-card outlined class="mb-2 pa-3 overflow-y-auto" max-height="500px" width="100%">
                      <v-card-text>
                        <div>
                          {{ infodetail.mainText }}
                        </div>                
                      </v-card-text>
                    </v-card>
                  </v-row>
                  <!-- 저작권 / 버튼 -->
                  <v-row class="justify-space-between">
                    <!-- 출제자 정보 -->
                    <div class="pa-0" >
                      <span class="grey--text mr-2 mb-1">Created by.
                        <v-btn class="px-0 font-weight-bold" plain @click=profileEvent(infodetail.writer.id)>                        
                          {{infodetail.writer.name}} 
                        </v-btn>
                      </span>
                    </div>

                    <!-- 남이 작성한 정보일 경우 -->
                    <div v-if="currentUser != infodetail.writer.id" class="pa-0 justify-end d-flex align-center">
                      <!-- 좋아요 버튼 -->
                      <div class="d-flex align-center">
                        <v-btn class="ms-2" icon color="dark lighten-2" @click="changeLikeStatus" id="upIcon">
                          <v-icon>{{upText}}</v-icon>
                        </v-btn>
                        <span>{{infodetail.numOfLikes}}</span>
                      </div>
                      <!-- 싫어요 버튼 -->
                      <div class="d-flex align-center">
                        <v-btn class="ms-2" icon color="dark lighten-2" @click="changeHateStatus" id="downIcon">
                          <v-icon>{{downText}}</v-icon>
                        </v-btn>
                        <span>{{infodetail.numOfDislikes}}</span>
                      </div>

                      <!-- 스크랩 버튼 -->
                      <div v-if="isLoggedIn">
                        <v-btn class="ms-1" icon color="dark lighten-2" @click="openScrapModal" id="scrapIcon">
                          <v-icon>{{scrapText}}</v-icon>
                        </v-btn>                
                      </div>  
                        <!-- 스크랩 모달 -->
                      <div>
                        <scrap @close="closeScrapModal" v-if="scrapModal" :pid="infodetail.id"></scrap>
                      </div>
                    </div>

                    <!-- 내가 작성한 정보일 경우 -->
                    <div v-else class="pa-0 justify-end d-flex align-center">
                      <v-btn class="ms-1" icon color="dark lighten-2" @click="openScrapModal" id="scrapIcon">
                        <v-icon>{{scrapText}}</v-icon>
                      </v-btn>                                    
                      <!-- 스크랩 모달 -->
                      <scrap @close="closeScrapModal" v-if="scrapModal"></scrap>
                      <!-- 수정 버튼 -->
                      <v-btn class="ms-1font-weight-bold" rounded outlined small @click="editInfo">수정</v-btn>
                      <!-- 삭제 버튼 -->
                      <v-btn class="ms-1 font-weight-bold" rounded outlined small color="red" @click="deleteInfo">삭제</v-btn>
                    </div>
                  </v-row>
                </v-container>
                
                <v-divider></v-divider>

                <!-- 댓글보기 -->
                <v-btn @click="showReplies" class="font-weight-bold mt-2" text>댓글보기</v-btn>
              </v-card-text>
            </v-col>

            <v-col id="reply-window" class="d-none">
              <v-card-text class="pa-0">
                <div>
                  <info-modal-reply :cid="infodetail.id" :commentList="commentList"></info-modal-reply>

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
import { mapGetters } from "vuex"
import InfoModalReply from './InfoModalReply.vue'
import Scrap from '@/components/Scrap/Scrap.vue'

export default {
  name: "InfoModal",
  components: {
    InfoModalReply,
    Scrap,
  },
  props: {
    infodetail: Object,
    info: Object,
  },
  data () {
    return {
      scrapModal: false,
      upText: 'thumb_up_off_alt',
      downText: 'thumb_down_off_alt',
      scrapText: 'bookmark_border',
      commentList: [],
    }
  },
  methods: {
    changeLikeStatus() {
      if (this.isLoggedIn){
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
            this.probdetail.numOfLikes = res.data.numOfLikes
          })
          .catch(err => {
            console.error(err)
          })
          /* 싫어요가 눌려 있는 상태에서 좋아요를 누르면 싫어요가 취소되는 것도 추가 */
          if (this.upText === "thumb_up_off_alt") {
          // 좋아요를 눌러야 하는데 이미 싫어요가 눌려져 있는 상태
          if (this.downText === "thumb_down") {
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
            this.probdetail.numOfDislikes = res.data.numOfDislikes
          })
          .catch(err => {
            console.error(err)
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
    event () {
      this.$router.push({ path: `information/${this.info.id}` })
    },
    profileEvent(uid) {
      this.$router.push({ path: `profile/${uid}`})
    },    
    onScroll () {
        this.scrollInvoked++
      },
    // 0815 삭제 버튼
    deleteInfo () {
      const userDecision = confirm('정말로 삭제하시겠습니까?')
      if (userDecision) {
        axios({
          url: drf.api + 'post' + `/${this.infodetail.id}`,
          method: 'delete',
          headers: {
            Authorization: this.accessToken,
          },
        })
        .then(res => {
          this.$router.push('/')
        }) 
        .catch(err =>{
          console.error(err)
        })
        this.$router.go()
      }
    },
    // 0815 수정
    // editInfo () {
    //   console.log('수정')
    // },
    openScrapModal() {
      this.scrapModal = true
    },
    closeScrapModal() {
        this.scrapModal = false
    },
    getInfoDetail() {
      axios({
        url: drf.api + 'post' + `/${this.infodetail.id}`,
        methods: 'get',
        headers: {
          Authorization : this.accessToken,
        },      
      })
      .then(res => {
        console.log(res.data)
        if (res.data.comments){
          this.commentList = res.data.comments.reverse()
        }
      })
      .catch(err => {
        console.error(err)
      })
    }
  },
  computed: {
    ...mapGetters(['accessToken','currentUser', 'isLoggedIn']),
  },
  created() {
    this.getInfoDetail()   
  },
}
</script>

<style>
.info-modal-white {
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
    background: white;
    border-radius: 4px;
    overflow: hidden;
    width: auto;
    max-height:100%
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