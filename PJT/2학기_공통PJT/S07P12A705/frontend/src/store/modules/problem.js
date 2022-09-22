import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import drf from '@/api/drf.js'

Vue.use(Vuex)

export default ({
  namespaced: true,
  state: {
    componentName: '',
    inputChange: '',
  },
  getters: {
    // isSearched는 현재 검색창에 단어를 검색했는지를 판별하기 위함!
    isSearched: (state) => !!state.inputChange,
    inputChange: (state) => state.inputChange
  },
  mutations: {
    SET_COMPONENT_NAME: (state, componentName) => state.componentName = componentName,
    SET_SEARCH_WORLD: (state, inputChange) => state.inputChange = inputChange
  },
  actions: {
    changeComponentName ({commit}, componentName) {
      commit
      console.log(componentName)
      // commit('SET_COMPONENT_NAME', componentName)
      // localStorage.setItem('componentName', componentName)
    },
    searchKeyword ({commit}, inputChange) {
      console.log('searchKeyword : ', inputChange)
      commit('SET_SEARCH_WORLD', inputChange)
    },

    async selectCategory(toDB) {
      // await this.$store.dispatch('reIssue')
      this.selectedProb = []
      this.selectedInfo = []
      if (this.feedFlag == 0) { // 카테고리로 문제 선택
        if (toDB == 'whole' && this.titleSearch == '') {
          this.selectedDB =  toDB
          this.selectedProb = []
          console.log("toBD =", toDB)
          const params = {
            page: 0,
            size: 5, 
            sort: 'updated,DESC',
          } 
          axios({
            url: drf.api + 'post' + '/problem',
            method: 'get',
            headers: {
              Authorization : this.accessToken,
            },
            params: params
          })
          .then(res => {
            this.mainProbs = res.data.content
            console.log("problem = ",this.mainProbs)
            this.endPage = res.data.totalPages 
            // console.log("totalPage =", res.data)
          })
          .catch(err => {
            console.log("에러")
            console.log(err)
          })
        } else {
          this.selectedProb = []
          console.log('toDB =', toDB)
          this.selectedDB =  toDB
          this.titleSearch = this.inputChange
          console.log('inputChange : ', this.inputChange)
          console.log('code : ', toDB)
          const params = {
            title : this.inputChange === undefined ? "" : this.inputChange,
            code : toDB,
            dtype : 'Problem',
            page : 0,
            size : 5,
            sort: 'updated,DESC'
          }
          axios({
            url: drf.api + 'post/' + 'search',
            method: 'get',
            headers: {
              Authorization : this.accessToken,
            },
            params: params,
          })
          .then(res => {
            console.log("prob 서치 =", res.data.content)
            this.selectedProb = res.data.content
          })
          .catch(err => {
            console.log("err=",err)
          })
        }
      } else if (this.feedFlag == 2){ // 카테고리로 정보 검색
        if (toDB == 'whole') {
          this.selectedDB =  toDB
          this.selectedInfo = []
          console.log("toBD =", toDB)
          const params = {
            page: 0,
            size: 5, 
            sort: 'updated,DESC',
          } 
          axios({
            url: drf.api + 'post' + '/information',
            method: 'get',
            headers: {
              Authorization : this.accessToken,
            },
            params: params
          })
          .then(res => {
            this.mainInfos = res.data.content
            console.log("info 전체 = ",this.mainInfos)
            this.endPage = res.data.totalPages 
            // console.log("totalPage =", res.data)
          })
          .catch(err => {
            console.log("에러")
            console.log(err)
          })
        } else {
          this.mainInfos = []
          console.log('toDB =', toDB)
          this.selectedDB =  toDB
          const params = {
            title : ``,
            code : toDB,
            dtype : 'Information',
            page : 0,
            size : 5,
            sort: 'updated,DESC'
          }
          axios({
            url: drf.api + 'post/' + 'search',
            method: 'get',
            headers: {
              Authorization : this.accessToken,
            },
            params: params,
          })
          .then(res => {
            console.log(res)
            console.log("info 서치=", res.data.content)
            this.selectedInfo = res.data.content
          })
          .catch(err => {
            console.log("err=",err)
          })
        }
      } 
    }  
  }
})
