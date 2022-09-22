<template>
  <div>
    <!-- 작성 전 문제 0808 임지민 -->
    <div v-for="beforeProb in beforeProbs" :key="beforeProb.id" class="mb-2">
      <v-card outlined elevation="3" class="rounded-xl purple-outlined-card mb-8 ">
        <!-- 카드 타이틀 (그라데이션 입혀진 부분) -->
        <v-card-title class="pa-0 yellow-bg-gradation">
          <v-container class="pa-0">
            <!-- 제목 -->
            <v-row class="d-flex justify-space-between ma-3 mt-4">
              <div class="ms-5 d-flex align-center font-weight-regular dark--text" style="font-size: 1.3em; color: #585757;">
                {{beforeProb.title}}
              </div>
            </v-row>
          </v-container>
        </v-card-title>
    
        <!-- 카드 본문 -->
        <v-card-text class="pb-0">
          <v-row>
            <!-- v-for문 사용해서 태그 띄우기 -->
            <div class="mt-5" v-for="tag in beforeProb.tags" :key="tag">
              <v-chip small color="orange" class="white--text ms-3 lighten-2">{{tag}}</v-chip>
            </div>
          </v-row>
    
          <router-link :to="`/note/pre/${beforeProb.id}`" width="100%">  
            <v-row class="ma-2 mb-2 d-flex justify-space-between">
              <!-- 노트로 이동하기 버튼 -->
              <!-- 화면 사이즈 md 이상 -->
              <v-btn text large rounded height="45px" class="d-none d-md-flex" width="100%">
                <div class="note-btn font-weight-regular">NOTE</div>
              </v-btn>
              <!-- 화면 사이즈 md 이하 -->
              <v-btn text large rounded height="45px" class="d-md-none mt-3" width="100%">
                <div class="note-btn font-weight-regular">NOTE</div>
              </v-btn>
            </v-row>
          </router-link>
        </v-card-text>
      </v-card>
    </div> 

    <!-- 작성 후 문제 0808 임지민 -->
    <div v-for="afterProb in afterProbs" :key="afterProb.id" class="mb-2">
      <v-card outlined elevation="3" class="rounded-xl purple-outlined-card mb-8 me-3">
        <!-- 카드 타이틀 (그라데이션 입혀진 부분) -->
        <v-card-title class="pa-0 yellow-bg-gradation">
          <v-container class="pa-0">
            <!-- 제목 -->
            <v-row class="d-flex justify-space-between ma-3 mt-4">
              <div class="ms-5 d-flex align-center font-weight-regular dark--text" style="font-size: 1.3em; color: #585757;">
                {{afterProb.title}}
              </div>
            </v-row>
          </v-container>
        </v-card-title>
    
        <!-- 카드 본문 -->
        <v-card-text class="pb-0">
          <v-row>
            <!-- v-for문 사용해서 태그 띄우기 -->
            <div class="mt-5" v-for="tag in afterProb.tags" :key="tag">
              <v-chip small color="orange" class="white--text ms-3 lighten-2">{{tag}}</v-chip>
            </div>
          </v-row>
    
          <router-link :to="`/note/post/${afterProb.id}`" width="100%">  
            <v-row class="ma-2 mb-2 d-flex justify-space-between">
              <!-- 노트로 이동하기 버튼 -->
              <!-- 화면 사이즈 md 이상 -->
              <v-btn text large rounded height="45px" class="d-none d-md-flex" width="100%">
                <div class="note-btn font-weight-regular">NOTE</div>
              </v-btn>
              <!-- 화면 사이즈 md 이하 -->
              <v-btn text large rounded height="45px" class="d-md-none mt-3" width="100%">
                <div class="note-btn font-weight-regular">NOTE</div>
              </v-btn>
            </v-row>
          </router-link>
        </v-card-text>
      </v-card>
    </div>

  </div>
</template>

<script>
export default {
  data() {
    return {
      page: 1,
    }
  },
  props: {
    beforeProbs: Array,
    afterProbs: Array,
  },

}
</script>

<style>
.font-parent-xsml {
  font-size: 0.1em;
}
.yellow-bg-gradation {
  background: linear-gradient(to right, rgb(253, 235, 177), rgb(255, 205, 68));
}
.note-btn {
  color: orange;
  font-size: 1.7em;
}
</style>