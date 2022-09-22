<template>
  <v-bottom-navigation v-model="icons.value" class="blue-navbar fixed-bottom align-center justify-space-around">
    <!-- url이 같은 상태에서는 상단으로 이동하고, 다른 상태에서는 지정된 url로 이동하기 (0808 임지민 완료)-->
    <div @click="checkUrl('/')">
      <button type="button" :value="icons[0].value" class="col-3 pa-0 transparent">
        <span class="material-icons font-30 text-decoration-none icon-white">
            {{ icons[0].text }}
        </span>
      </button>
    </div>
    <div @click="checkUrl('/study')">
      <button type="button" :value="icons[1].value" class="col-3 pa-0 transparent">
        <span class="material-icons font-30 text-decoration-none icon-white">
            {{ icons[1].text }}
        </span>
      </button>
    </div>
    <div @click="checkUrl('/note')">
      <button type="button" :value="icons[2].value" class="col-3 pa-0 transparent">
        <span class="material-icons font-30 text-decoration-none icon-white">
            {{ icons[2].text }}
        </span>
      </button>
    </div>
    <div @click="checkUrl(`/profile/${currentUser}`)">
      <button type="button" :value="icons[3].value" class="col-3 pa-0 transparent">
        <span class="material-icons font-30 text-decoration-none icon-white">
            {{ icons[3].text }}
        </span>
      </button>
    </div>
  </v-bottom-navigation>
</template>
""
<script>
import { mapGetters } from 'vuex'

export default {
  data() {
    return {
      icons: [
        { 
          value: 'recent',
          text: 'home',
          urlName: '/'
        },
        { 
          value: 'favorites',
          text: 'groups',
          urlName: '/study'
        },
        { 
          value: 'nearby',
          text: 'sticky_note_2',
          urlName: '/note'
        },
        { 
          value: 'nearby',
          text: 'person',
          urlName: `/profile/${this.currentUser}`
        },
      ],

    }
  },
  computed: {
  ...mapGetters(['currentUser'])
  },
  methods : {
    checkUrl(urlName) {
      if (window.location.href.endsWith(urlName)) {
        // console.log(true)
        window.scrollTo({
          top: 0,
          left: 0,
          behavior: 'smooth'
        })
      } else {
        this.$router.push({ path: urlName })
      }
    }
  }
}
</script>

<style>
.fixed-bottom {
    position: fixed;
    bottom: 0;
    height: 56px;
}
.font-30 {
    font-size: 30px;
}

/* box shadow 없애기 */
.v-item-group.v-bottom-navigation {
  box-shadow: none;
}

.icon-white {
  color: #f7f7f7;
}
</style>

<style scoped>
.blue-navbar {
  background-color: #c297fa;
}
</style>