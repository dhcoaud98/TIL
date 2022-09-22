<template>
  <v-container class="modal" appear>
    <v-container class="modal modal-overlay" @click.self="$emit('close')">
      <v-container class="modal-window pa-0">
        <v-card class="modal-content rounded-lg pa-4">
          <!-- <slot/> -->
          <v-card-title class="pb-0">
            <v-container class="pa-0">
              <v-row class="d-flex justify-space-between">
                <h2 class="font-weight-medium grey--text text--darken-2 pt-1">STUDY</h2>
                <v-btn @click="$emit('close')" icon class="pa-0"><v-icon>mdi-close</v-icon></v-btn>
              </v-row>

              <v-row class="mt-6 ml-1" v-if="myStudydetail">
                <!-- <p>{{myStudydetail}}</p> -->
                <!-- <p style="font-size: 10px;">{{studydetail}}</p> -->
                <h2 class="purple--text text--darken-4 font-weight-medium">{{myStudydetail.title}}</h2>
              </v-row>
              <v-row class="mt-6 ml-1" v-else>
                <h2 class="purple--text text--darken-4 font-weight-medium">{{studydetail.title}}</h2>
              </v-row>

              <v-row>
                <!-- 내가 만든 스터디일 때 버튼 -->
                <v-col class="d-flex justify-end pe-0" v-if="createdByMe" cols="12">
                  <v-btn rounded class="ms-2 font-weight-bold" @click="editStudy(myStudydetail.id)">스터디 수정하기</v-btn>
                </v-col>

                <!-- 남이 만든 스터디일 때 버튼 -->
                <div v-else>
                  <v-col class="d-flex justify-end pe-0" cols="12" v-if="studydetail.secret">
                    <v-btn rounded class="ms-2 font-weight-bold" @click="doSend">스터디 신청하기</v-btn>
                  </v-col>
                </div>
              
              </v-row>
            </v-container>
          </v-card-title>

          <v-divider color="#A384FF" class="mx-2"></v-divider>

          <v-card-text class="py-2" v-if="myStudydetail">
            <div class="mx-2 my-1">
              <h3 class="ma-0 px-1 font-weight-bold grey--text text--darken-3">현재원 / 총원 : {{myStudydetail.currentPerson}} / {{myStudydetail.maxPerson}} </h3>
              <h3 class="ma-0 px-1 font-weight-bold grey--text text--darken-3">장소 : {{myStudydetail.place}}</h3>
              <!-- 내가 만든 스터디일 경우 마감일 필드가 안 넘어옴 -->
              <!-- <p class="ma-0 px-2">마감일 : {{myStudydetail.expiredDate}}</p> -->
            </div>
          </v-card-text>
          <v-card-text class="py-2" v-else>
            <div class="mx-2 my-1">
              <h3 class="ma-0 px-1 font-weight-bold grey--text text--darken-3">현재원 / 총원 : {{studydetail.currentPerson}} / {{studydetail.maxPerson}} </h3>
              <h3 class="ma-0 px-1 font-weight-bold grey--text text--darken-3">장소 : {{studydetail.place}}</h3>
              <h3 class="ma-0 px-2 font-weight-bold grey--text text--darken-3">마감일 : {{studydetail.expiredDate}}</h3>
            </div>
          </v-card-text>

          <v-divider color="#A384FF" class="mx-2"></v-divider>

          <v-card-text>
            <div class="d-flex" v-if="myStudydetail">
              <div class="pl-2" v-for="(tag, idx) in myStudydetail.tags" :key="idx">
                <v-chip small color="#A384FF" class="white--text font-wieght-bold">{{ tag.type }}</v-chip>
              </div>
            </div>
            <div class="d-flex" v-else>
              <div class="pl-2" v-for="(tag, idx) in studydetail.tags" :key="idx">
                <v-chip small color="#A384FF" class="white--text font-wieght-bold">{{ tag.type }}</v-chip>
              </div>
            </div>

            <v-container class="my-4 study-detail-info">
              <v-row>
                <v-col cols="12" v-if="myStudydetail">
                  <h3> 스터디장 : {{ myStudydetail.masterName }}</h3>
                </v-col>
                <v-col cols="12" v-else>
                  <h3> 스터디장 : {{ studydetail.masterName }}</h3>
                </v-col>
                
                <v-col cols="12" v-if="myStudydetail">
                  <div class="black-text font-weight-bold">[ 스터디 설명 ]</div>
                  {{ myStudydetail.mainText }}
                </v-col>

                <v-col cols="12" v-else>
                  <div class="black-text font-weight-bold">[ 스터디 설명 ]</div>
                  {{ studydetail.mainText }}
                </v-col>

                <v-col cols="12" v-if="myStudydetail">
                  <div class="red--text text--darken-1 font-weight-bold">[ 해당 내용은 스터디원에게만 공개되는 내용입니다. ]</div>
                  {{ myStudydetail.secretText }}
                </v-col>
              </v-row>
            </v-container>

            <v-container>
              <v-row v-if="!studydetail.secret">
                <v-col class="d-flex justify-end pe-0" cols="12">
                  <div v-if="createdByMe">
                    <v-btn rounded class="ms-2 font-weight-bold white--text" color="red lighten-1" @click="deletedoSend">스터디 삭제하기</v-btn>
                  </div>
                  <div v-else>
                    <v-btn rounded class="ms-2 font-weight-bold" @click="deleteStudy">스터디 탈퇴하기</v-btn>
                  </div>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-card>
      </v-container>
    </v-container>
  </v-container>
</template>  

<script>
import drf from '@/api/drf'
import axios from 'axios'
import { mapGetters } from "vuex"

export default {
  name: 'StudyModal',
  data() {
    return {
      modal: false,
      studyId: '',
      studydetail: [],
      createdByMe: null,
    }
  },
  props: {
    study: Object,
    myStudydetail: Object,
  },
  created() {
    // this.studyId = this.study.id
    // console.log("study id = ",this.studyId)
    // console.log(this.createdByMe)
    // console.log('현재 = ', this.currentUser);
    this.getStudyDetail()

    if(this.myStudydetail.masterId === this.currentUser){
      // console.log('trueeeee');
      this.createdByMe = true
    } else {
      // console.log('falseeee');
      this.createdByMe = false
    }
    // console.log('mmmmmmmmmmmmmmmm')
    // console.log(this.studydetail);
    // console.log(this.currentUSer)

  },
  methods: {
    openModal() {
      this.modal = true
      console.log(openModal)
    },
    closeModal() {
      this.modal = false
      console.log(closeModal)
    },
    
    // 스터디 신청하기 (0813 오채명) 신청 후 새로고침
    doSend() {
      axios({
        url: drf.study.study() + 'me/' + `${this.myStudydetail.id}`,
        method: 'post',
        headers: {
          Authorization: this.accessToken,
        },  
      })
      .then(res => {
        console.log("스터디 신청 =", res)
        this.$swal({
          icon: 'success',
          text: "스터디 신청이 완료되었습니다."
        })
        this.$router.go();
      })
      .catch(err =>{
        console.log("에러")
        console.log(err.response.status)
        if (err.response.status === 500) {
          this.$swal({
            icon: 'warning',
            text: '이미 가입된 스터디입니다.'
          })
        }
      })
    },

    // 스터디 삭제 (0812 오채명) 삭제 후 새로고침
    deletedoSend() { 
      this.$swal({
        icon: 'warning',
        text: '정말로 삭제하시겠습니까?',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: '아니요',
        cancelButtonText: '삭제'
      }) .then((result) => {
        if (result.isCancel) {
          this.$swal(
            '스터디가 삭제되었습니다.',              
            'success'
          )}
        axios({
          url: drf.api + 'study' + `/${this.studydetail.id}`,
          method: 'delete',
          headers: {
            Authorization: this.accessToken,
          },        
        })
        this.$router.go();
      })
    },

    // 나의 스터디 탈퇴 (0815 오채명) 삭제 후 새로고침
    deleteStudy () {
      this.$swal({
        icon: 'warning',
        text: '정말로 탈퇴하시겠습니까?',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: '아니요',
        cancelButtonText: '탈퇴'
      }) .then((result) => {
        if (result.isCancel) {
          this.$swal(
            '스터디 탈퇴되었습니다.',              
            'success'
          )}
        axios({
          url: drf.study.study() + 'me' + `/${this.myStudydetail.id}`,
          method: 'delete',
          headers: {
            Authorization : this.accessToken,
          },
        })
        this.$router.go();  
      })
    },

    // 스터디 수정하기
    editStudy (sid) {
      // console.log('sid=' , sid);
      this.$router.push({path: `editstudy/${sid}`})
    },

    //api/study/{studyid}에 해당하는 detail study 정보 가져오기
    async getStudyDetail() {
      await this.$store.dispatch('reIssue');
      axios({
        url: drf.study.study() + `${this.myStudydetail.id}`,
        methods: 'get',
        headers: {
          Authorization : this.accessToken,
        },
      })
      .then(res => {
        // console.log("studydetail =" , res.data)
        this.studydetail = res.data
        console.log("studydetail 모달 =",this.studydetail)
      })
    }



  },
  computed: {
    ...mapGetters(['accessToken', 'currentUser']),
  }
}

</script>

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
    background: #F3F1F5;
    border-radius: 4px;
    overflow: hidden;
    height: auto;
    width: 550px;
  }

  &-content {
    padding: 10px 20px;
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
.button {
  background-color:#A384FF;
  padding-right: 2%;
  padding-left: 2%;
  padding-top: 1%;
  padding-bottom: 1%;
  margin: 1%;
  color: white;
  border-radius: 5px;
}
.button_update {
  background-color:green;
  padding-right: 2%;
  padding-left: 2%;
  padding-top: 1%;
  padding-bottom: 1%;
  margin: 1%;
  color: white;
  border-radius: 5px;
}
.button_delete {
  background-color:red;
  padding-right: 2%;
  padding-left: 2%;
  padding-top: 1%;
  padding-bottom: 1%;
  margin: 1%;
  color: white;
  border-radius: 5px;
}
</style>