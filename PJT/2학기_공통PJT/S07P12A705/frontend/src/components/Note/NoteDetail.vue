<template>
  <!-- 전체적인 틀 -->
  <v-container fluid class="white mt-10">
    <!-- 문제 정보 -->
    <v-row class="align-center mx-5 mt-5 border-a-10 px-4 rounded-xl yellow lighten-4">
      <v-col cols="1"><v-icon large color="orange darken-3">mdi-note-edit</v-icon>
      </v-col>
      <v-col>
        <v-row>
          <v-col class="align-center py-1">
            <v-col class="pa-0">
              <h2 class="font-weight-bold mr-3">{{noteDetail.title}}</h2>
            </v-col>
          </v-col>
        </v-row>
        <v-row class="ma-0">
          <v-col cols="3" class="pa-0 d-flex">
            <div v-for="tag in noteDetail.tags" :key="tag.id">
              <v-chip small color="orange" class="white--text ms-3">{{tag.type}}</v-chip>
            </div>
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <!-- 문제 부분 -->
    <v-row class="mt-0">
      <v-col>
        <note-detail-list :noteDetail="noteDetail"></note-detail-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import NoteDetailList from '@/components/Note/NoteDetailList.vue'
import axios from 'axios'
import drf from '@/api/drf.js'
import { mapGetters } from 'vuex'

export default {
  data() {
    return {
      noteDetail: null,
    }
  },
  components: {
    NoteDetailList,
  },
  props: {
    
  },
  computed: {
    ...mapGetters(['accessToken'])
  },
  methods : {
    async getNoteDetail() {
      await this.$store.dispatch('reIssue');
      const noteId = this.$route.params.noteId
      // console.log(noteId)
  
      axios({
        url: drf.wrongAnswer.wrongAnswer() + noteId,
        method: 'get',
        headers: {
          Authorization: this.accessToken,
        },
      })
      .then(res => {
        // console.log(res) //ok
        this.noteDetail = res.data
  
      })
      .catch(err => {
        console.log(err);
      })

    }
  },
  created() {
    this.getNoteDetail()
  },
}
</script>

<style>

</style>