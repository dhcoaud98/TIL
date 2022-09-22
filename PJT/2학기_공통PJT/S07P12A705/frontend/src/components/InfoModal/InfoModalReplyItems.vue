<template>
  <!-- 2022.07.26 댓글창 (남성은) -->
  <!-- <v-card elevation="2" class="rounded ma-2 pa-4 mx-1"> -->
    <v-container class="mt-2 border-a-10 h-300 overflow-auto px-0">
      <div v-for="comment in commentList" :key="comment.id" >
        <div id="grey-reply" rounded class="mb-2">
          <v-row class="border-a-10">
            <!-- <p>{{commentList}}</p> -->
            <v-col>{{comment.mainText}}</v-col>
          </v-row>

          <v-row class="justify-space-between" v-if="userId===comment.user.id">
            <v-col class="pt-0 d-flex">
              <div cols="3" lg="3" class="align-end secondary--text text--lighten-3">{{comment.user.name}}</div>
              <div class="align-end secondary--text text--lighten-3 ms-4">{{comment.created}}</div>
            </v-col>
            <v-col class="d-flex col-4">
              <v-btn @click="deleteComment(comment.id)" text color="#a384ff">삭제</v-btn>
            </v-col>  
          </v-row>

          <v-row v-else>
            <v-col class="pt-0 d-flex">
              <div cols="3" lg="3" class="align-end secondary--text text--lighten-3">{{comment.user.name}}</div>
              <div cols="5" lg="3" class="align-end secondary--text text--lighten-3 ms-4">{{comment.created}}</div>
            </v-col>
          </v-row>
        </div>
      </div>
    </v-container>
  <!-- </v-card> -->
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios'
import drf from '@/api/drf.js'

export default {
  data() {
    return {

    }
  },
  props: {
    commentList: Array,
    cid: Number,
  },
  computed: {
    ...mapGetters(['userId', 'accessToken']),
  },
  methods: {
    deleteComment(commentId) {
      const check = confirm('정말 삭제하시겠습니까?')
      if (check) {
        axios({
          url: drf.api + 'comment/' + `${commentId}`,
          method: 'delete',
          headers: {
            Authorization: this.accessToken,
          },
        })
          .then((res) => {
            // console.log(this.credentials);
            console.log('res = ', res);
            console.log(this.pid)
            this.$router.go()
            // this.$router.push({path: `/problem/${this.pid}`})
          })
          .catch(err => {
            console.log('댓삭 에러= ', err)
          })
        }
      }
    },
}
</script>

<style>

</style>