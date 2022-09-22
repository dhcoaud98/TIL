<template>
  <v-row class="justify-space-between mx-0">
    <div class="pa-0">
      <input type="radio" name="folders" :id="scrapFolder.id"
      @change="emitFolderId(scrapFolder.id)">
      <label :for="scrapFolder.id"
        class="ml-2 font-weight-mid-l">{{ scrapFolder.title }}</label>
      <!-- <v-checkbox
        :label="scrapFolder.title"
        color="info"
        class="font-weight-bold pa-0 ma-0"
        :id="`scrap${scrapFolder.id}`"
        @change="emitFolderId(scrapFolder.id)"
        name="folders"
      ></v-checkbox> -->
    </div>
    <div class="mr-2 pa-0 justify-end">
      <v-btn plain small class="px-0" @click="openModal"><h3 class="purple--text">이동</h3></v-btn>
      <v-btn plain small class="px-0" @click="$emit('delete-folder', scrapFolder.id)"><h3 class="red--text">삭제</h3></v-btn>
    </div>
    <!-- <p>hi</p> -->
    <scrap-post-modal 
      @close="closeModal" v-if="modal" 
      :lid="scrapFolder.id" 
      :scrapFolder="scrapFolder"
      :getScrapFolders="getScrapFolders"></scrap-post-modal>

  </v-row>
</template>

<script>
import drf from '@/api/drf'
import axios from 'axios'
import { mapGetters } from 'vuex'
import ScrapPostModal from '@/components/Profile/ScrapPostModal.vue'


export default {
  name: 'ScrapListItems',
  data(){
    return {
      modal: false,
    }
  },
  components: {
    ScrapPostModal
  },
  props: {
    scrapFolder: Object,
    getScrapFolders: Function,
  },
  computed: {
    ...mapGetters(['accessToken'])
  },
  methods: {
    emitFolderId(lid) {
      this.$emit('checkedFolder', lid)
      // console.log(lid);
    },
    async openModal() {
      await this.$store.dispatch('reIssue');
        this.modal = true
        console.log('openModal')
    },
    closeModal() {
        this.modal = false
        console.log('closeModal')
    },
    
  },
}
</script>

<style>

</style>