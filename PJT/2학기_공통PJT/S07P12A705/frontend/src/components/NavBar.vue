<template>
  <v-card 
      height="400"
      width="256"
      class="mx-auto"
      color="transparent"
    >
      <v-navigation-drawer permanent class="mt-2">
        <v-list-item class="mt-5">
          <v-list-item-content>
            <v-list-item-title>
              <router-link to="/">
                <v-img src="../assets/prosn_logo.png" max-width="200px" max-height="50px" class="mb-5" id="mainPage" @click="searchCleard()"></v-img>
              </router-link>
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list nav>
          <v-list-item>
            <v-list-item-content class="py-0 font-parent-mid">
              <v-list-item-title class="left-line ml-5 ms-0 mb-0 py-5 pl-5 cursor-pointer" 
              :id="items[0].urlName"
              @click="avoidAnonymous('/study')" >{{ items[0].text }}</v-list-item-title>
            

              <v-list-item-title 
                class="left-line ml-5 ms-0 mb-0 py-5 pl-5 cursor-pointer" 
                :id="items[1].urlName"
                @click="avoidAnonymous('/note')">{{ items[1].text }}</v-list-item-title>
              
              <!-- <router-link :to="`/profile/${currentUser}`" class="text-decoration-none black--text mb-0"> -->
              <v-list-item-title 
                class="left-line ml-5 ms-0 mb-0 py-5 pl-5 cursor-pointer" 
                :id="items[2].urlName"
                @click="avoidAnonymous(`/profile/${currentUser}`)">{{ items[2].text }}</v-list-item-title>
              <!-- </router-link>   -->
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>         
    </v-card>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'NavBar',
  data () {
    return {
      tmp: '',
      loginDisplay: 'd-flex',
      items: [
        { 
          text: 'S T U D Y',
          url: 'study',
          urlName: 'study',
        },
        { 
          text: 'N O T E S',
          url: 'note',
          urlName: 'note',
        },
        { 
          text: 'P R O F I L E',
          url: `profile/${this.currentUser}`,
          urlName: 'profile',
        },
      ]
    }
  },
  computed: {
    ...mapGetters(['currentUser', 'isLoggedIn',]),
  },
  watch: {
    // url이 바뀔 때마다 감시해서 nav바 상태 바꿔주기
    $route(to, from) {
      //console.log(to) // 도착지
      //console.log(from) // 출발지
      const studyTag = document.querySelector('#study')
      const profileTag = document.querySelector('#profile')
      const noteTag = document.querySelector('#note')

      if (to.name === 'mainPage') {
        // 도착지의 name에 해당하는 태그는 clicked-tab을 넣고
        // const toTag = document.querySelector(`#${to.name}`)
        // toTag.classList.add('clicked-tab')
        // const fromTag = document.querySelector(`#${from.name}`)
        // fromTag.classList.remove('clicked-tab')
        if (studyTag.classList.contains('clicked-tab')) {
          studyTag.classList.remove('clicked-tab')
        } else if (noteTag.classList.contains('clicked-tab')) {
          noteTag.classList.remove('clicked-tab')
        } else if (profileTag.classList.contains('clicked-tab')) {
          profileTag.classList.remove('clicked-tab')
        }
      } else if (to.name === 'study') {
        studyTag.classList.add('clicked-tab')

        if (noteTag.classList.contains('clicked-tab')) {
          noteTag.classList.remove('clicked-tab')
        } else if (profileTag.classList.contains('clicked-tab')) {
          profileTag.classList.remove('clicked-tab')
        }

      } else if (to.name === 'note') {
        noteTag.classList.add('clicked-tab')

        if (studyTag.classList.contains('clicked-tab')) {
          studyTag.classList.remove('clicked-tab')
        } else if (profileTag.classList.contains('clicked-tab')) {
          profileTag.classList.remove('clicked-tab')
        }

      } else if (to.name === 'profile') {
        profileTag.classList.add('clicked-tab')

        if (noteTag.classList.contains('clicked-tab')) {
          noteTag.classList.remove('clicked-tab')
        } else if (studyTag.classList.contains('clicked-tab')) {
          studyTag.classList.remove('clicked-tab')
        }
      }
      // 출발지의 name에 해당하는 태그는 clicked-tab을 빼기
    }
  },
  methods: {
    searchCleard: function(event) {
      this.$router.push({path: 'mainPage'})
            this.$store.dispatch('problem/searchKeyword', "")
    },
    avoidAnonymous(url) {
      console.log(this.currentUser);
      console.log(url);
      if (!this.isLoggedIn) {
        this.$swal({
          icon: 'warning',
          text: '로그인 후 이용해주세요'
        })
        this.$router.push({ path: '/login'})
      } else {
        this.$router.push({ path: url})
      }
    }
  },
}
</script>

<style>
  /* .left-line-perm {
    border-left: 5px solid #d9d9d9;
  } */
  .left-line {
    border-left: 5px solid #d9d9d9;
  }
  :hover.left-line{
    border-left: solid 5px #A384FF;
    font-weight: bold;
  }
  :hover.cursor-pointer {
    cursor: pointer;
  }
  .clicked-tab {
    border-left: solid 5px #A384FF;
    font-weight: bold;
    color: #774BFA;
  }
  .v-application--wrap {
    max-width: 280px;
  }
  .v-navigation-drawer__content {
    background-color: #f5f5f5;
  }
  .v-navigation-drawer__border {
    background-color: #f5f5f5;
  }

  /* 네브바 box shadow, 선 없애기 */
  .v-sheet.v-card:not(.v-sheet--outlined) {
    box-shadow: none;
  }
  .theme--light.v-navigation-drawer:not(.v-navigation-drawer--floating) .v-navigation-drawer__border {
    background-color: transparent;
  }

  /* 각 탭 아래에 생기는 마진 없애기 */
  .v-list--nav .v-list-item:not(:last-child):not(:only-child), .v-list--rounded .v-list-item:not(:last-child):not(:only-child) {
    margin-bottom: 0;
  }
</style>