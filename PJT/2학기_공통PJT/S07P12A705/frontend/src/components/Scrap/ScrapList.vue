<template>
  <v-container class="overflow-y-auto" style="height: 200px;">
    <!-- <v-checkbox
      label="기본폴더"
      color="info"
      value=""
      hide-details
      class="mt-0 font-weight-bold"
    ></v-checkbox> -->
    <div v-for="scrapFolder in scrapFolders" :key="scrapFolder.id">
      <!-- <p>{{scrapFolder.title}}</p> -->
      <scrap-list-items 
      :scrapFolder="scrapFolder" 
      :getScrapFolders="getScrapFolders" 
      @checkedFolder="catchFolderId"
      @delete-folder="deleteFolder"></scrap-list-items>
    </div>
    <div>
      <!-- <p>hi</p> -->
      <!-- <p>{{lid}}</p> -->
    </div>
  </v-container>
</template>

<script>
import ScrapListItems from '@/components/Scrap/ScrapListItems.vue'
import axios from 'axios'
import drf from '@/api/drf.js'
import { mapGetters } from 'vuex'

export default {
  name: 'ScrapList',
  data() {
    return {
      lid: null,
    }
  },
  components: {
    ScrapListItems,
  },
  props: {
    scrapFolders: Array,
    getScrapFolders: Function,
  },
  computed: {
    ...mapGetters(['accessToken'])
  },
  methods: {
    catchFolderId(lid) {
      // console.log('hihi')
      this.lid = lid
      // console.log('캐치했다=', this.lid);
      this.$emit('emit-folder', lid)
    },
    async deleteFolder(lid) {
      await this.$store.dispatch('reIssue');
      // axios 보내기
      const check = confirm('정말 삭제하시겠습니까?')
      if (check) {
      axios({
        url: drf.scrap.folder() + lid,
        method: 'delete',
        headers: {
          Authorization: this.accessToken,
        },
        data: {
          id: lid
        }
      })
      .then(res => {
        // 받아온 데이터를 작성 전/후로 구분하는 작업 필요(0808 임지민)
        console.log('스크랩 폴더 삭제= ', res)
        this.getScrapFolders()
      })
      .catch(err => {
        // console.log(this.accessToken)
        // console.log(this.userId)
        console.log('스크랩 폴더 삭제 에러= ',err);
      })
    }
    },
    async getScrapFolders() {
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
        this.$router.go()
      })
      .catch(err => {
        console.log('스크랩 폴더 조회 에러', err);
        if (err.response.status === 400) {
          this.$swal({
            icon: 'warning',
            text: '유효하지 않은 폴더입니다'
          })
          this.$router.go()
        }
      })
    },
  }
}
</script>

<style>

</style>