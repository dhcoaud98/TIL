<template>
  <!-- 전체적인 틀 -->
  <v-container fluid class="white mt-10">
    <!-- 문제 정보 -->
    <v-row class="align-center mx-5 mt-5 border-a-10 px-4 rounded-xl yellow lighten-4">
      <v-col cols="1"><v-icon large color="orange darken-3">mdi-note-edit-outline</v-icon>
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
      <create-note-list :noteDetail="noteDetail"></create-note-list>
    </v-row>
  </v-container>
</template>

<script>
import CreateNoteList from '@/components/Note/CreateNoteList.vue'
import { mapGetters } from 'vuex'
import axios from 'axios'
import drf from '@/api/drf.js'

export default {
  data() {
    return {
      noteDetail: null,
    }
  },
  components: {
    CreateNoteList,
  },
  methods : {
    async createNote(){
      await this.$store.dispatch('reIssue');
      const noteId = this.$route.params.noteId
      // console.log('noteId=', noteId)
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
        // console.log(this.noteDetail)

      })
      .catch(err => {
        console.log(err);
      })
    }
  },
  computed: {
    ...mapGetters(['userName', 'accessToken'])
  },
  created() {
    this.createNote()
  }
}
</script>

<style>

</style>