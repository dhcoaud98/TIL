<template>
  <v-card-text class="px-1 py-3">
    <!-- 댓글 입력란 -->
    <v-container class="rounded-lg replies my-3">
      <!-- {{credentials}} -->
      <v-form @submit.prevent="submitComment" v-if="isLoggedIn">
        <v-row>
          <v-textarea 
          background-color="#f5f5f5" 
          rows="1" 
          placeholder="댓글을 작성해주세요" 
          no-resize dense
          v-model="credentials.mainText"
          class="mr-5"
          id="commentArea"></v-textarea>
          <v-btn type="submit" color="#A384FF" outlined rounded>
            댓글달기
          </v-btn>
        </v-row>
      </v-form>

    </v-container>
    <!-- 2022.08.03.댓글창 -->
    <v-container class="rounded-lg replies">
      <!-- 댓글창제목 -->
      <v-row class="ma-1">
        <v-col cols="12">
          <h2>댓글({{commentLength}})</h2>
        </v-col>
      </v-row>

      <v-divider color="#A384FF"></v-divider>

      <!-- 2022.08.03. 댓글 목록 -->
      <!-- 추후에 더미 데이터 넣고 버추얼스크롤 넣어서 확인하기-->
      <!-- 여기서 for문 돌려서 ProblemReplyItems 하나씩 띄우기 -->
      <v-row>
        <v-col class="pa-0">
          <!-- <p>hi</p> -->
          <info-modal-reply-items :commentList="commentList" :cid="credentials.cid"></info-modal-reply-items>
        </v-col>
      </v-row>
    </v-container>

  </v-card-text>
</template>

<script>
import InfoModalReplyItems from '@/components/InfoModal/InfoModalReplyItems.vue'
import { mapGetters } from 'vuex';
import axios from 'axios'
import drf from '@/api/drf.js'

export default {
  name: 'InfoModalReply',
  data() {
    return {
      credentials: {
        pid: this.cid,
        mainText: ''
      },
      commentLength: 0,
    }
  },
  props: {
    cid: Number,
    commentList: Array,
  },
  components: {
    InfoModalReplyItems
  },
  computed: {
    ...mapGetters(['accessToken', 'isLoggedIn'])
  },
  methods: {
    submitComment() {
      console.log(this.credentials);
      axios({
				url: drf.api + 'comment/',
				method: 'post',
				headers: {
					Authorization: this.accessToken,
				},
				data: this.credentials,
			})
				.then((res) => {
          // console.log(this.credentials);
					console.log('res = ', res.data);
          // this.commentList.push(this.credentials)
          // this.$router.push({ path: 'profile' })

          // 댓글을 조회하기 위한 axios 0814 임지민
           axios({
            url: drf.api + 'post' + `/${this.cid}`,
            methods: 'get',
            headers: {
              Authorization : this.accessToken,
            },      
          })
          .then(res => { 
            // console.log('댓글 가져오기')
            this.commentList = res.data.comments.reverse()
            this.commentLength = this.commentList.length
            // console.log(this.commentList)

            // 작성 완료되면 댓글 입력란 비우기 0814 임지민
            const commentArea = document.querySelector('#commentArea')
            commentArea.value = ''
          })
				})
				.catch((err) => {
					console.log('에러');
					console.log(err);
          console.log(this.cid)
				});
    }
  },
  created() {
    console.log(this.commentList);
    if (this.commentList) {
      this.commentLength = this.commentList.length
    } 
  }
}
</script>

<style>
  .replies {
    background-color: #f5f5f5;
  }
  .h-300 {
    height: 300px;
  }
</style>