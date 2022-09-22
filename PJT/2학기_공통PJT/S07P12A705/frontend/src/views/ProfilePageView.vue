<template>
  <v-container fluid class="pa-0 pt-0 pt-md-10 mt-0">
    <!-- row 1: 메인 피드와 sidebar 모두를 감싸는 줄 -->
    <v-row>

      <!-- col 1: 메인 피드 부분 -->
      <v-col class="mt-2 white rounded-lg">
        <profile-center></profile-center>  
      </v-col>


      <!-- col 2: 사이드 바 -->
      <v-col md="5" lg="4" class="d-md-flex d-none grey lighten-4">
        <side-bar></side-bar>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ProfileCenter from '../components/Profile/ProfileCenter.vue'
import SideBar from '@/components/SideBar.vue'


export default {
  name: 'ProfilePageView',
  components :{
    ProfileCenter,
    SideBar,
  }
}
</script>

<style>
  /* .v-application--wrap {
  max-width: none;
  }
  .container {
    max-width: none;
  }
  .w-100 {
    width: 100%;
  }  
  .tab-hover::before {
    color: #616161;
  } */
</style>