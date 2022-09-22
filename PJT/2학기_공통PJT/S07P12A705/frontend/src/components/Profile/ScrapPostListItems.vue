<template>
  <v-card outlined elevation="3" class="rounded-xl purple-outlined-card mb-5">
    <!-- 카드 타이틀 (그라데이션 입혀진 부분) -->
    <v-card-title class="pa-0 bg-scrap-gradation">
      <v-container class="pa-0">

        <!-- 리스트 제목  -->
        <v-row class="my-3 justify-space-between">
          <!-- 리스트 제목 -->
          <div class="ms-5 d-flex align-center font-weight-regular dark--text" style="font-size: 1.2em; color: #585757;">
            {{ scrapFolder.title }}
          </div>
          <v-icon large class="me-5" color="blue lighten-5">mdi-folder-open</v-icon>

        </v-row>
      </v-container>
    </v-card-title>

    <!-- 카드 본문 -->
    <v-card-text>
      <v-row class="mx-4 d-flex justify-space-between">
        <!-- 모달 띄우기 버튼 -->
        <v-btn @click="openModal" large rounded height="45px" class="mt-3" width="100%" elevation="0">
          <div class="show-up-btn font-weight-regular">SHOW UP</div>
        </v-btn>
      </v-row>
    </v-card-text>

    <!-- 모달 -->
    <scrap-post-modal @close="closeModal" v-if="modal" :lid="scrapFolder.id" :scrapFolder="scrapFolder"></scrap-post-modal>
  </v-card>
</template>

<script>
import ScrapPostModal from '@/components/Profile/ScrapPostModal.vue'

export default {
  data () {
    return {
      modal: false,
    }
  },
  components: {
    ScrapPostModal,
  },
  props: {
    scrapFolder: Object,
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
  },
  created(){
    // 스크랩 폴더 조회하기 
    
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
.bg-scrap-gradation {
  background: linear-gradient(to right, #dbeff9, #8094FF);
}
</style>