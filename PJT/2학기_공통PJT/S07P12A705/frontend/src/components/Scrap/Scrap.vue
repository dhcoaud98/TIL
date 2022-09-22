<template>
  <!-- 모달을 위한 요소들 -->
  <v-container class="scrap-modal" appear>
    <v-container class="scrap-modal scrap-modal-overlay" @click.self="$emit('close')">
      <v-container class="scrap-modal-window pa-0 mx-0 d-flex justify-center">
        <!-- 2022.07.27 스크랩 (남성은) -->
        <v-card width="400" class="rounded-lg scrap-modal-content pa-0">
          <v-container>
            <v-row>
              <v-col cols="12" class="d-flex justify-space-between">
                <div class="d-flex flex-row align-center">
                  <v-icon large>mdi-folder-open</v-icon>
                  <h3 class="ms-2">Scrap</h3>
                  <!-- <p>hi : {{pid}}</p> -->
                </div>
                <div>
                  <v-btn @click="getScrapFolders" icon><v-icon>restart_alt</v-icon></v-btn>
                  <v-btn @click="$emit('close')" icon><v-icon>mdi-close</v-icon></v-btn>
                </div>
              </v-col>
            </v-row>

            <v-divider class="mx-1 my-2"></v-divider>

            <v-row>
              <v-col class="pa-0">
                <v-container>
                  <v-row>
                    <v-col class="pa-0">
                      <!-- {{scrapFolders}} -->
                      <scrap-list :scrapFolders="scrapFolders" :getScrapFolders="getScrapFolders"
                      @emit-folder="catchFolderId"></scrap-list>
                    </v-col>
                  </v-row>
                </v-container>
              </v-col>
            </v-row>

            <v-divider class="mx-1 my-2"></v-divider>

            <v-row class="my-2">

              <!-- 리스트 만들기 -->
              <!-- 2. 새로운 리스트를 만들수 있는 폼 -->
              <!-- 새로운 리스트를 만들고 생성 버튼을 누르면 다시 사라짐 -->
              <v-col cols="12" class="d-none" id="create-scrap-form">
                <v-form ref="form" @submit.prevent="createScrap"> 
                  <v-row>
                    <v-col cols="9" class="py-1">
                      <v-text-field label="문제 리스트 이름을 입력하세요" 
                      maxlength="20" 
                      v-model="scrapTitle"
                      counter required dense></v-text-field>
                    </v-col>
                    <!-- <p>{{scrapTitle}}</p> -->
                    <v-col cols="3" class="pa-0">
                      <v-btn color="purple lighten-2" text outlined rounded type="submit" width="100%"><h3 class="purple--text text--lighten-1">생성</h3></v-btn>
                    </v-col>
                  </v-row>
                </v-form>
              </v-col>

              <!-- 새로운 목록 추가 버튼과 스크랩 버튼 -->
              <v-col cols="12" class="py-1">
                <!-- 새로운 목록 추가 버튼 -->
                <!-- 1. 버튼을 누르면 새로운 리스트를 만들 수 있는 폼이 나옴. 위에 있음 -->
                <v-btn rounded width="100%" @click="openCreateScrap">
                  새로운 목록 추가
                </v-btn>
              </v-col>
              <v-col cols="12" class="py-1">

                <!-- 체크한 리스트에 해당 문제를 스크랩 할 수 있는 버튼 -->
                <v-btn rounded color="#A384FF" class="white--text" width="100%" @click="scrapPost">
                  스크랩
                </v-btn>
              </v-col>
            </v-row>
            <div @checkedFolder="catchFolderId" :lid="lid">
              <p></p>
            </div>
          </v-container>
        </v-card>
      </v-container>
    </v-container>
  </v-container>  
</template>  

<script>
import ScrapList from '@/components/Scrap/ScrapList.vue'
import drf from '@/api/drf.js'
import axios from 'axios'
import { mapGetters } from 'vuex'

export default {
  name: 'Scrap',

  data: () => ({
    scrapTitle: '',
    scrapFolders: [],
    lid: null,
  }),
  components : {
    ScrapList,
  },
  props: {
    pid: Number,
  },
  computed: {
    ...mapGetters(['accessToken'])
  },
  methods: {
    // 새로운 리스트를 생성할 수 있는 폼
    openCreateScrap () {
      console.log('열려라 참깨');
      const createScrapForm = document.querySelector("#create-scrap-form")
      console.log(createScrapForm.classList);
      createScrapForm.classList.remove('d-none')
    },
    // 새로운 리스트를 작성한 후 내보내기
    createScrap () {
      const createScrapForm = document.querySelector("#create-scrap-form")
      createScrapForm.classList.add('d-none')
      if (this.scrapTitle.trim() !== '') {
      axios({
        url: drf.scrap.folder(),
        method: 'post',
        headers: {
          Authorization: this.accessToken,
        },
        data: {
          title: this.scrapTitle
        }
        })
        .then(res => {
          console.log('스크랩 폴더 만들기=', res);
          this.getScrapFolders()

        })
        .catch(err => {
          console.log('스크랩 폴더 만들기 에러', err);
        })
      } else {
        this.$swal({
          icon: 'warning',
          text: '폴더 이름을 입력해주세요'
        })
      }
    },
    getScrapFolders() {
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
    },
    // 선택된 폴더 아이디를 emit해서 받기 0815 임지민
    catchFolderId(lid) {
      this.lid = lid
      // console.log('캐치했다=', this.lid); // ok
    },

    // 문제 스크랩 하기 엑쇼스 0816 임지민
    scrapPost() {
      console.log('문제 스크랩= ', this.pid, this.lid)
      axios({
      url: drf.scrap.scrap(),
      method: 'post',
      headers: {
        Authorization: this.accessToken,
      },
      data: {
        pid: this.pid,
        lid: this.lid,
      }
      })
      .then(res => {
        console.log('문제 스크랩 =', res); // ok
        this.$swal({
          icon: 'success',
          text: '문제 스크랩이 완료되었습니다.'
        })
      })
      .catch(err => {
        console.log('문제 스크랩 에러= ', err); 
        if( err.status === 400) {
          this.$swal({
            icon: 'error',
            text: '이미 해당 폴더로 스크랩된 문제입니다.'
          })
        }
      })
    }

  },
  created() {
    this.getScrapFolders()
    console.log(this.pid)
  }
}
</script>

<style>

</style>

<style lang="stylus" scoped>
.scrap-modal {
  &.scrap-modal-overlay {
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

  &-scrap-window {
    background: whitesmoke;
    border-radius: 4px;
    overflow: hidden;
    width: auto;
  }

  &-scrap-content {
    padding: 10px;
    width: 100%;
    height: 100%
  }
}

// 오버레이 트랜지션
.scrap-modal-enter-active, .scrap-modal-leave-active {
  transition: opacity 0.4s;

  // 오버레이에 포함되어 있는 모달 윈도의 트랜지션
  .scrap-modal-window {
    transition: opacity 0.4s, transform 0.4s;
  }
}

// 딜레이가 적용된 모달 윈도가 제거된 후에 오버레이가 사라짐
.scrap-modal-leave-active {
  transition: opacity 0.6s ease 0.4s;
}

.scrap-modal-enter, .scrap-modal-leave-to {
  opacity: 0;

  .scrap-modal-window {
    opacity: 0;
    transform: translateY(-20px);
  }
}
</style>