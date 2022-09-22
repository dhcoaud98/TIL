<template>
  <v-card outlined elevation="3" class="rounded-xl purple-outlined-card mb-8">
    <!-- 카드 타이틀 (그라데이션 입혀진 부분) -->
    <v-card-title class="pa-0 bg-gradation">
      <v-container class="pa-0">

        <!-- dType에 따라 바뀌는 뱃지 -->
        <v-row class="mt-3 ms-5">
          <div v-if="userPost.ptype === `Information`" class="d-flex align-center font-weight-regular grey--text" style="font-size: 0.8em">
            <v-icon color="#F355F6" class="me-2">mdi-circle</v-icon>
            <p class="mb-0">I N F O</p>
          </div>
          <div v-if="userPost.ptype === `Problem`" class="d-flex align-center font-weight-regular grey--text" style="font-size: 0.8em">
            <v-icon color="#8094FF" class="me-2">mdi-circle</v-icon>
            <p class="mb-0">P R O B L E M</p>
          </div>
          <div v-if="userPost.ptype === `Workbook`" class="d-flex align-center font-weight-regular grey--text" style="font-size: 0.8em">
            <v-icon color="#DF6969" class="me-2">mdi-circle</v-icon>
            <p class="mb-0">B O O K</p>
          </div>
        </v-row>

        <!-- 게시글 제목 / 좋아요와 싫어요 개수 -->
        <v-row class="d-flex justify-space-between my-1">
          <!-- 제목 -->
          <div class="ms-5 d-flex align-center font-weight-regular dark--text" style="font-size: 1em; color: #585757;">
           {{ userPost.title }}
          </div>
          <!-- 좋아요 싫어요 정보 -->
          <div class="d-flex me-3">
            <v-icon class="me-2">thumb_up_off_alt</v-icon>
            <!-- <div class="me-3">{{ probdetail.numOfLikes }}</div> -->
            <div class="me-3">{{ userPost.numOfLikes }}</div>
            <v-icon class="me-2">thumb_down_off_alt</v-icon>
            <div class="me-3">{{ userPost.numOfDislikes }}</div>
            <!-- <div class="me-3">{{ probdetail.numOfDislikes }}</div> -->
          </div>
        </v-row>
      </v-container>
    </v-card-title>

    <!-- 카드 본문 -->
    <v-card-text>
      <v-row>
        <!-- v-for문 사용해서 태그 띄우기 -->
        <div class="mt-5" v-for="tag in userPost.tags" :key="tag">
          <v-chip small color="#926DFF" class="white--text ms-3">{{ tag }}</v-chip>
        </div>
      </v-row>

      <v-row class="mx-4 d-flex justify-space-between">
        <!-- 문제 또는 정보 버튼 -->
        <v-btn v-if="userPost.ptype === `Information`" @click='showUpInfo()' large rounded height="45px" class="mt-3" width="100%" elevation="0">
          <div class="show-up-btn font-weight-regular">SHOW UP</div>
        </v-btn>
        <v-btn v-if="userPost.ptype === `Problem`" @click='showUpProb()' large rounded height="45px" class="mt-3" width="100%" elevation="0">
          <div class="show-up-btn font-weight-regular">SHOW UP</div>
        </v-btn>
        <v-btn v-if="userPost.ptype === `Workbook`" @click='showUpBook()' large rounded height="45px" class="mt-3" width="100%" elevation="0">
          <div class="show-up-btn font-weight-regular">SHOW UP</div>
        </v-btn>

      </v-row>
    </v-card-text>
  </v-card>
  <!-- created: (...)
        id: (...)
        numOfDislikes: (...)
        numOfLikes: (...)
        ptype: "Information"
        tags: (...)
        title: (...)
        updated: (...)
        views: (...)
        writer: (...) -->

<!-- created: (...)
      id: (...)
      numOfDislikes: (...)
      numOfLikes: (...)
      ptype: "Problem"
      tags: (...)
      title: (...)
      updated: (...)
      writerId: (...)
      writerName: (...) -->
</template>

<script>
import ProblemModal from '@/components/ProblemModal/ProblemModal.vue'
import InfoModal from '@/components/InfoModal/InfoModal.vue'

export default {
  data () {
    return {
      page1: 1,
      page2: 2,
      modal: false,
    }
  },
  components: {
    ProblemModal,
    InfoModal,
  },
  props: {
    userPost: Object,
  },
  methods: {
    openModal() {
      this.modal = true
      console.log('openModal')
    },
    closeModal() {
      this.modal = false
      console.log('closeModal')
    },
    showUpInfo () {
      this.$router.push({ path: `../information/${this.userPost.id}` })
    },
    showUpProb () {
      this.$router.push({ path: `../problem/${this.userPost.id}` })
    },
    showUpBook () {
      this.$router.push({ path: `../problembook/${this.userPost.id}` })
    },
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
  border-radius: 10px;
  border: 1px solid #E7C0F4;
  background-color: #E7C0F4;
  font-size: 1px;
  color: white;
  font-weight: bold;
  height: 10px;
  margin: 1px;
}
.problem_detail {
  font-size: 0.5px;
  text-align: right;
}
.problem_title {
  font-size: 2px;
  font-weight: bold;
}
.my_it {
  font-size: 2px;
  font-weight: bold;
}
.card-title {
  font-size: 2em;
  font-weight: medium;
}
.text-purple {
  color: #774BFA;
}
.show-up-btn {
  color: #774BFA;
  font-size: 1.7em;
}
.bg-gradation {
  background: linear-gradient(to right, #dbeff9, #e9dbf2);
}
</style>

<!-- 덮어씌우기 -->

<!-- <style scoped>
.purple-outlined-card {
  border: thin solid #8A96FD;
}
</style> -->
<!-- 덮어씌우기 -->

<!-- <style scoped>
.purple-outlined-card {
  border: thin solid #8A96FD;
}
</style> -->