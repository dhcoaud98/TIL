import Vue from 'vue'
import Vuex from 'vuex'

import accounts from '@/store/modules/accounts.js'
import createPersistedState from "vuex-persistedstate";
// import info from './modules/info.js'
// import note from './modules/note.js'
import problem from './modules/problem.js'
// import search from './modules/search.js'
// import study from './modules/study.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {},
	getters: {},
	mutations: {},
	actions: {},
  modules: {
    accounts,
    // info,
    // note,
    problem,
    // search,
    // study
  },
  plugins: [
		createPersistedState({
			storage: sessionStorage,
		}),
	],
})

