<template>
  <!-- 2022.07.26 문제 모달 (남성은) -->
  <v-container class="modal" appear>
    <v-container class="modal modal-overlay" @click.self="$emit('close')">
      <v-container class="modal-window pa-0">
        <v-card class="rounded-lg modal-content pa-4">
          <!-- <p>{{scrapDetails}}</p> -->
          <!-- <p>{{ scrapFolder}}</p> -->
          <!-- 카드 타이틀 -->
          <v-card-title class="pb-0">
            <v-container class="pa-0">
              <!-- 각 개별 리스트의 이름 -->
              <v-row class="d-flex justify-space-between">
                <h2>{{ scrapFolder.title }} </h2>
                <v-btn @click="$emit('close')" icon class="pa-0"><v-icon>mdi-close</v-icon></v-btn>
              </v-row>

              <!-- 문제집 이름을 제출하기 위한 폼 0816 임지민 -->
                <v-row class="mt-5 justify-end" v-if="toggleBookInput">
                  <v-col class="px-0 ml-2" cols="2">
                    <v-btn 
                    small outlined rounded 
                    class="font-weight-bold"
                    @click="showBookInput">문제집 만들기</v-btn>
                  </v-col>
                </v-row>
              <v-form v-else @submit.prevent="createBook(scrapFolder.id)">
                <v-row class="justify-end align-center">
                  <v-col cols="4">
                    <!-- <p>{{scrapFolder.title}}</p> -->
                    <!-- <p>{{ credentials.title }}</p> -->
                    <v-text-field label="문제집 이름을 입력해주세요"
                        v-model="credentials.title"
                        id="bookName"></v-text-field>
                  </v-col>
                  <v-col cols="2" class="pa-0 text-end">
                    <v-btn
                      small outlined rounded
                      class="font-weight-bold"
                      type="submit">만들기</v-btn>
                  </v-col>
                </v-row>
              </v-form>
            </v-container>
          </v-card-title>

          <v-divider color="#A384FF" class="mx-3"></v-divider>

          <v-card-text class="py-0">
            <v-container class="pa-0">
                <!-- {{ scrapDetails }} -->
              <scrap-modal-list :scrapDetails="scrapDetails.content" :lid="lid"
              @re-direct="getFolderDetail"></scrap-modal-list>
            </v-container>
          </v-card-text>

          <v-divider color="#A384FF" class="mx-3"></v-divider>

          <v-row class="justify-end">
            <v-col cols="2" class="mr-3">
              <v-btn outlined rounded small
              color="red lighten-1" 
              class="font-weight-bold white--text ms-3"
              @click="deleteFolder(scrapFolder.id)">폴더 삭제</v-btn>
            </v-col>
          </v-row>

          <v-card-footer class="d-flex-row justify-center">
            <v-container class="pt-5 pb-0">
              <v-row class="d-flex justify-center">문제집 추출은 문제의 경우에만 가능합니다.</v-row>
              <v-row class="d-flex justify-center">정보가 포함되어 있을 경우 자동으로 걸러져서 문제집이 추출되오니 참고해주시기 바랍니다.</v-row>
            </v-container>
          </v-card-footer>

        </v-card>
      </v-container>
    </v-container>
  </v-container>
</template>

<script>
import ScrapModalList from '@/components/Profile/ScrapModalList.vue'
import drf from '@/api/drf'
import axios from 'axios'
import { mapGetters } from 'vuex'

export default {
  name: 'ScrapPostModal',
  components: {
    ScrapModalList,
  },
  data(){
    return {
      scrapDetails: [],
      credentials: {
        pid: this.scrapFolder.id,
        title: ''
      },
      toggleBookInput: true,
    }
  },
  props: {
    lid: Number,
    scrapFolder: Object,
    getScrapFolders: Function,
  },
  computed: {
    ...mapGetters(['accessToken'])
  },
  methods: {
    showBookInput() {
      // console.log('showbookinput', this.toggleBookInput);
      this.toggleBookInput = false
      // console.log('showbookinput change', this.toggleBookInput);
    },
    // 해당 폴더에 있는 문제 조회 0815 임지민
    async getFolderDetail () {
      await this.$store.dispatch('reIssue');

      axios({
        url: drf.scrap.scrap() + `${this.lid}`,
        method: 'get',
        headers: {
          Authorization: this.accessToken,
        },
      })
      .then(res => {
        // 받아온 데이터를 작성 전/후로 구분하는 작업 필요(0808 임지민)
        console.log(res)
        this.scrapDetails = res.data

      })
      .catch(err => {
        // console.log(this.accessToken)
        // console.log(this.userId)
        console.log(err);
      })
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
        // console.log('스크랩 폴더 삭제= ', res)
        this.$emit('close')
        this.$router.go()
      })
      .catch(err => {
        // console.log(this.accessToken)
        // console.log(this.userId)
        console.log('스크랩 폴더 삭제 에러= ',err);
        if(err.response.data.message === "could not execute statement; SQL [n/a]; constraint [null]; nested exception is org.hibernate.exception.ConstraintViolationException: could not execute statement"){
          this.$swal({
            icon: 'warning',
            text: '폴더 내 문제를 먼저 삭제한 후 폴더를 삭제해주세요'
          })
        }

      })
    }
    },
    // 문제집 만들기
    async createBook() {
      await this.$store.dispatch('reIssue');

      if(this.credentials.title.trim() === '') {
        this.$swal({
          icon: 'warning',
          text: '문제집 이름을 입력해주세요'
        })
        console.log('scrap detail==========', this.scrapDetails.content.length);
      } else {
        if (this.scrapDetails.content.length) {
          // 엑쇼스
          axios({
          url: drf.postFeed.workbook(),
          method: 'post',
          headers: {
            Authorization: this.accessToken,
          },
          data: this.credentials
        })
        .then(res => {
          // 받아온 데이터를 작성 전/후로 구분하는 작업 필요(0808 임지민)
          // console.log(res)
          this.$swal({
            icon: 'success',
            text: '문제집 출제가 완료되었습니다'
          })
          this.$router.go()
        })
        .catch(err => {
          // console.log(this.accessToken)
          // console.log(this.userId)
          console.log(err);
        })
        } else {
          this.$swal({
            icon : 'warning',
            text: '출제할 문제가 없습니다.'
          })
        }

      }
    }
  },
  created(){
    this.getFolderDetail()
  },
  
}
</script>

<style>
  
</style>

<style lang="stylus" scoped>
.v-label, .v-input {
  font-size: 0.7em;
}
.modal {
  &.modal-overlay {
    display: flex;
    align-items: center;
    justify-content: center;
    position: fixed;
    z-index: 30;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
  }

  &-window {
    background: whitesmoke;
    border-radius: 4px;
    overflow: hidden;
    width: auto;
  }

  &-content {
    padding: 10px;
    width: 100%;
    height: 100%
  }
}

// 오버레이 트랜지션
.modal-enter-active, .modal-leave-active {
  transition: opacity 0.4s;

  // 오버레이에 포함되어 있는 모달 윈도의 트랜지션
  .modal-window {
    transition: opacity 0.4s, transform 0.4s;
  }
}

// 딜레이가 적용된 모달 윈도가 제거된 후에 오버레이가 사라짐
.modal-leave-active {
  transition: opacity 0.6s ease 0.4s;
}

.modal-enter, .modal-leave-to {
  opacity: 0;

  .modal-window {
    opacity: 0;
    transform: translateY(-20px);
  }
}
</style>