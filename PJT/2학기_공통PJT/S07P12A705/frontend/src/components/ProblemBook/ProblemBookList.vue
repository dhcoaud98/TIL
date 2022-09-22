<template>
<!-- 
  틀린 문제들 받아오기 
  - 문제 개수대로 탭 띄우기
  - 탭 모양: 동그라미 숫자  
-->
  <v-container>
    <v-row>
      <v-col>
        <!-- <p>hi {{bookDetails.problemInfos.length}}</p> -->
        <v-toolbar
          flat
        >
          <!-- <template v-slot:extension> -->
            <v-tabs
              v-model="tab"
              align-with-title
            >
              <v-tabs-slider color="red lighten-4"></v-tabs-slider>

              <!-- 여기에 오답노트 개수 세서 넣어놓기 -->
              <v-tab
                v-for="i in (0, endTabNum)"
                :key="i"
              >
                {{ i }}
              </v-tab>
            </v-tabs>
          <!-- </template> -->
        </v-toolbar>

        <!-- 여기는 위에처럼 오답노트 개수 세서 넣어놓기 -->
        <v-tabs-items v-model="tab">
          <v-tab-item
            v-for="probDetail in probDetails"
            :key="probDetail.id"
          >
            <!-- 여기다가 notelist로 받아서 v-for로 돌려주기 -->
            <v-card>
              <v-card-text>
                <!-- hello world: ok -->
                <!-- problem-book-list-items도 정상적으로 작동함 -->
                <!-- {{probDetail}} -->
                <problem-book-list-items :probDetail="probDetail"></problem-book-list-items>
              </v-card-text>
            </v-card>
          </v-tab-item>
        </v-tabs-items>
      </v-col>
    </v-row>
  </v-container>

</template>

<script>
import ProblemBookListItems from '@/components/ProblemBook/ProblemBookListItems.vue'
import axios from 'axios'
import drf from '@/api/drf.js'
import { mapGetters } from 'vuex'

export default {
  components: {
    ProblemBookListItems,
  },
  data() {
    return {
      tab: null,
      endTabNum: this.bookDetails.problemInfos.length,
      probInfos: this.bookDetails.problemInfos,
      probDetails: []
    }
  },
  props: {
    bookDetails: Object
  },
  computed: {
    ...mapGetters(['accessToken'])
  },
  created() {
    // 엑쇼스로 문제 정보 불러와서 미리 저장해놓고 하위 컴포넌트로 넘기기 0817 임지민
    // console.log(this.endTabNum);
    this.probInfos.forEach(prob => {
      let pid = prob.id
      axios({
      url: drf.api+'post/' + pid,
      method: 'get',
      headers: {
        Authorization: this.accessToken,
      },
    })
    .then(res => {
      // console.log(res) //ok
      this.probDetails.push(res.data)
      // console.log('문제집에서 문제 불러오기', this.probDetails);
    })
    .catch(err => {
      console.log(err);
    })
    });
  }
}
</script>

<style>

</style>