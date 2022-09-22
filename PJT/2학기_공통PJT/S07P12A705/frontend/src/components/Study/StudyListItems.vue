<template>
  <v-card outlined elevation="3" class="rounded-xl purple-outlined-card mb-8">
    <!-- 카드 타이틀 (그라데이션 입혀진 부분) -->
    <!-- <p>{{study}}</p> -->
    <v-card-title class="pa-0 purple-gradation">
      <v-container class="pa-0">
        <!-- 스터디 제목 / 현재인원수와 총인원수 -->
        <v-row class="d-flex justify-space-between ma-3">
          <!-- 제목 -->
          <div class="ms-5 d-flex align-center font-weight-regular dark--text" style="font-size: 1.3em; color: #585757;">
            {{ study.title }}
          </div>
          <!-- 좋아요 싫어요 정보 -->
          <div class="d-flex me-3">
            <v-icon class="me-2">mdi-account-check-outline</v-icon>
            <div class="me-3 grey--text">{{ study.currentPerson }}</div><div>/ {{ study.maxPerson }}</div>
          </div>
        </v-row>
      </v-container>
    </v-card-title>

    <!-- 카드 본문 -->
    <v-card-text>
      <v-row class="ma-4 mb-2 d-flex justify-space-between">
        <!-- 출제자 -->
          <div class="me-4 d-flex align-center" style="font-size: 1.2em">Leader. {{ master }}</div>
        <!-- 모달 띄우기 버튼 -->
          <!-- 화면 사이즈 md 이상 -->
          <v-btn @click="openModal" text large rounded height="45px" class="d-none d-md-flex">
            <div class="show-up-btn font-weight-regular">SHOW UP</div>
          </v-btn>
          <!-- 화면 사이즈 md 이하 -->
          <v-btn @click="openModal" text large rounded height="45px" class="d-md-none mt-3" width="100%">
            <div class="show-up-btn font-weight-regular">SHOW UP</div>
          </v-btn>
      </v-row>
    </v-card-text>

    <!-- 모달 -->
    <study-modal @close="closeModal" v-if="this.modal" :study="study" :myStudydetail="myStudydetail"></study-modal>
  </v-card>
</template>

<script>
import StudyModal from "@/components/Study/StudyModal.vue"
import { mapGetters } from 'vuex'
import drf from '@/api/drf'
import axios from 'axios'

export default {
  name: 'StudyListItems',
  data() {
    return {
      modal: false,
      pageId: 0,
      myStudydetail: [],
      master: '',
    }
  },
  props: {
    study: Object,
  },
  components: {
    StudyModal,
  },
  computed: {
    ...mapGetters(['currentUser', 'accessToken'])
  },
  methods: {
    openModal() {
      this.modal = true
      console.log(openModal)
      console.log(this.study.id)
    },
    closeModal() {
      this.modal = false
      console.log('closeModal')
    },
    doSend() {
        alert("스터디 신청이 완료되었습니다.")
        this.message = ''
        this.closeModal()
    },
    async getStudyDetail(){
      await this.$store.dispatch('reIssue');
      
      // api/study/{studyid}에 해당하는 detail study 정보 가져오기
      axios({
        url: drf.study.study() + `${this.study.id}`,
        methods: 'get',
        headers: {
          Authorization : this.accessToken,
        },
      })
      .then(res => {
        // console.log("studydetail =" , res.data)
        this.myStudydetail = res.data
        this.master = res.data.masterName
        // console.log(this.master);
        // console.log("myStudydetail =",this.myStudydetail.masterName)
      })
    }
  },
  created(){
    // 나의 스터디마다 정보 조회
    // console.log("왜?")
    // console.log("확인 =", this.myStudy)
    this.getStudyDetail()
  }
}
</script>

<style>
.feed-width {
    width: auto;
}
.border-a-10 {
  border-radius: 5px;
}
.color-FAF0F3 {
  background-color: #FAF0F3;
}
.category-tag {
  border-radius: 20px;
  border: 1px solid #E7C0F4;
  background-color: #E7C0F4;
  font-size: 3px;
  color: white;
  font-weight: bold;
  height: 20px;
  margin: 1px;
}
.problem_detail {
  font-size: 2px;
  text-align: right;
}
.problem_title {
  font-size: 2px;
}
.study-content {
  width : 100%;
  height: 100%;
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
.info-divider {
  background-color:#A384FF;
}
.study-detail-info {
  background-color: #EDE7F6;
  height: 100%;
}
.purple-gradation{
  background: linear-gradient(to right, #F2E6F6, #E7C0F4);
}
</style>