<template>
  <!-- 모달을 위한 요소들 -->
  <v-container class="scrap-modal" appear>
    <v-container class="scrap-modal scrap-modal-overlay" @click.self="$emit('close')">
      <v-container class="scrap-modal-window pa-0 mx-0 d-flex justify-center">

        <!-- 2022.08.16 Following (남성은) -->
        <v-card width="400" class="rounded-lg scrap-modal-content pa-0">
          <v-container>
            <v-row>
              <v-col cols="12" class="d-flex justify-space-between">
                <h3 class="ms-2">나를 팔로우한 사람들</h3>
                <v-btn @click="$emit('close')" icon><v-icon>mdi-close</v-icon></v-btn>
              </v-col>
            </v-row>

            <v-divider class="mx-1 my-2"></v-divider>

            <v-row>
              <v-col class="pa-0">
                <v-container class="pt-0" max-height="400px">
                  <div v-for="(myFollowerElem,idx) in myFollowerList" :key="idx">
                    <v-btn @click="profileEvent(myFollowerElem.id)" plain x-large class=" purple--text text--darken-1 d-flex justify-space-between bottom-lined" width="100%">
                      <h4>유저이름: {{myFollowerElem.name}}</h4>
                      <h4>포인트: {{myFollowerElem.point}}</h4>
                    </v-btn>
                    <v-divider></v-divider>
                  </div>
                </v-container>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-container>
    </v-container>
  </v-container>  
</template>  

<script>
import drf from '@/api/drf.js'
import axios from 'axios'
import { mapGetters } from 'vuex'

export default {
  name: 'MyFollowerModal',
  data: () => ({
    myFollowerList: []
  }),
  computed: {
    ...mapGetters(['accessToken', 'currentUser'])
  },
  methods: {
    profileEvent(uid) {
      this.$router.push({ path: `../profile/${uid}`})
      this.$router.go()
    },  
  },
  created() {
    axios({
          url: drf.api + 'user/follower',
          method: 'get',
          headers: {
            Authorization : this.accessToken,
          },
        })
        .then(res => {
          this.myFollowerList = res.data.content
        })
        .catch(err => {
          console.log(err)
        })
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