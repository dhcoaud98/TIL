<template>
  <v-container class="mt-5 px-0 px-md-3">
    <v-row>
      <v-col class="text-center">
        <p v-if="!studys.length">아직 등록된 스터디가 없습니다</p>
      </v-col>
    </v-row>
    <study-list-items v-for="(study, idx) in studys" :key="idx" :study="study"></study-list-items>
    <br>  
    <v-pagination
      v-model="nowPage"
      :length="endPage + 1"
      color="#A384FF"
      circle
      @input="handlePage()"
    ></v-pagination>
  </v-container>
</template>

<script>
import axios from 'axios'
import drf from '@/api/drf'
import StudyListItems from "./StudyListItems.vue"
import { mapGetters } from 'vuex'

export default {
  name: 'StudyList',
  components: {
    StudyListItems,
  },
  data () {
    return {
      value: null,
      nowPage: 1,
      endPage: 0,
      studys: [],
      page: 0,
    }
  },
  computed: {
    ...mapGetters(['accessToken']),
  },
  created() {
    // 0811 오채명
    // 스터디 가장 기본 페이지인 첫 번째 엑시오스
    const params = {
      page: 0,
      size: 5, 
      sort: 'updated,DESC'
    } 
    axios({
      url: drf.study.study(),
      method: 'get',
      headers: {
        Authorization : this.accessToken,
      },
      params: params
      //page=0&size=3&sort=updated,desc
    })
    .then(res => {
      this.studys = res.data.content
      console.log("studys = ",this.studys)
      this.endPage = res.data.totalPages
      // console.log("totalPages =",res.data.totalPages)
      // console.log("totalElements =", res.data.totalElements)
    })
    .catch(err => {
      console.log("에러")
      console.log(err)
    })
  },
  methods: {
    // 페이지 네이션 엑시오스
    handlePage () {
      console.log("event = ", Number(event.target.ariaLabel.slice(-1)))
      this.page = Number(event.target.ariaLabel.slice(-1))

      const params ={
        page: this.page -1 ,
        size: 5,
        sort: 'updated,DESC'
      }
      axios({
        url: drf.study.study(),
        method: 'get',
        headers: {
          Authorization: this.accessToken
        },
        params: params        
      })
      .then(res => {
        console.log("넘어온 data = ", res.data.content)
        this.studys = res.data.content
      })
      .catch(err => {
        console.log("에러")
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>