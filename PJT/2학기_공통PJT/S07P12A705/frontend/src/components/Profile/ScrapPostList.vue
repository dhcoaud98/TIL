<template>
  <v-container class="mt-5 px-0 px-md-3">
    <!-- v-for 사용하기 -->
    <!-- {{ scrapFolders}} {{ scrapFolders.length}} -->
    <v-row>
      <v-col class="text-center">
        <p v-if="!scrapFolders.length">스크랩한 폴더가 없습니다</p>
      </v-col>
    </v-row>
    <div v-for="scrapFolder in scrapFolders" :key="scrapFolder.id">
      <scrap-post-list-items :scrapFolder="scrapFolder"></scrap-post-list-items>
    </div>
    <br>  
    <v-container class="text-center ">
      <v-pagination
        v-model="page"
        :length="scrapFolders.length/5 + 1"
        color="#A384FF"
      ></v-pagination>
    </v-container>
  </v-container>
</template>

<script>
import ScrapPostListItems from './ScrapPostListItems.vue'
import drf from '@/api/drf'
import axios from 'axios'
import { mapGetters } from 'vuex'


export default {
  name: 'ScrapPostList',
  components: {
    ScrapPostListItems,
  },
  data () {
    return {
      page: 1,
      scrapFolders: [],
    }
  },
  computed: {
    ...mapGetters(['accessToken'])
  },
  methods: {
    async getMyFolderList(){
      await this.$store.dispatch('reIssue');
     // 내 폴더 목록 조회 0815 임지민
    axios({
      url: drf.scrap.folder(),
      method: 'get',
      headers: {
        Authorization: this.accessToken,
      },
      })
      .then(res => {
        console.log('스크랩 폴더 조회=', res.data);
        this.scrapFolders = res.data
      })
      .catch(err => {
        console.log('스크랩 폴더 조회 에러', err);
      })
    }
  },
  created() {
    this.getMyFolderList()
  }
}
</script>

<style>

</style>