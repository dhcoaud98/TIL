<template>
  <v-list>
    <div v-for="(scrapDetail, idx) in scrapDetails" :key="idx">
      <scrap-modal-list-items :scrapDetail="scrapDetail" :idx="idx" :lid="lid"
       @re-direct="redirectFolder"
       @get-selected-prob="getSelectedProb"></scrap-modal-list-items>
    </div>
  </v-list>
</template>

<script>
import ScrapModalListItems from '@/components/Profile/ScrapModalListItems.vue'
import axios from 'axios'
import drf from '@/api/drf.js'


export default {
  name: 'ScrapModalList',
  data() {
    return {
      selectedProbIdList: []
    }
  },
  components: {
    ScrapModalListItems,
  },
  props :{
    scrapDetails: Array,
    lid: Number,
  },
  methods: {
    redirectFolder() {
      this.$emit('re-direct')
    },
    getSelectedProb(pid) {
      this.selectedProbIdList.push(pid)
      // console.log('선택한 문제 아이디들=', this.selectedProbIdList);
      
    }
  }

}
</script>

<style>

</style>