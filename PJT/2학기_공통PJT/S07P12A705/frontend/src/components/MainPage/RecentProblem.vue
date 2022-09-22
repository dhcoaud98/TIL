<template>
	<div>
		<v-row class="pa-0 ma-0" rounded>
			<v-col cols="12" class="pa-0">
				<!-- <div v-if="selectedProb"> -->
				{{ this.selectedProb }}
				<recent-problem-items
					v-for="(mainProb, idx) in mainProbs"
					:key="idx"
					:mainProb="mainProb"
				></recent-problem-items>
				<v-pagination
					v-model="nowPage"
					:length="endPage"
					color="#A384FF"
					circle
					@input="handlePage()"
				></v-pagination>
				<!-- </div>
        <div v-if="mainProbs">
          {{mainProbs}}
          <recent-problem-items 
            v-for="(mainProb, idx) in mainProbs"
            :key="idx"
            :mainProb="mainProb"
          ></recent-problem-items>
          <v-pagination
            v-model="nowPage"
            :length="endPage"
            color="#A384FF"
            circle
            @input="handlePage()"
          ></v-pagination> -->
				<!-- </div> -->
			</v-col>
		</v-row>
	</div>
</template>

<script>
import axios from 'axios';
import drf from '@/api/drf';
import RecentProblemItems from '../MainPage/RecentProblemItems.vue';
import { mapGetters } from 'vuex';

export default {
	data() {
		return {
			totalProbs: [],
			// mainProbs: [],
			nowPage: 1,
			clickPage: null,
			endPage: 1,
			value: null,
			page: 0,
			// selectedProb:[],
		};
	},
	props: {
		selectedDB: String,
		selectedProb: Array,
		mainProbs: Array,
	},
	components: {
		RecentProblemItems,
	},
	computed: {
		...mapGetters(['accessToken']),
		isSearched() {
			return this.$store.getters['problem/isSearched'];
		},
		inputChange() {
			return this.$store.getters['problem/inputChange'];
		},
	},
	created() {
		// 페이지 렌더링 될 때 첫번 째 엑시오스
		// 1. 검색어가 있을 때!
		// if(this.selectedDB != 'whole'){
		//   console.log(this.selectedProb)
		// } else { // 2. 검색어 없을 때
		//   const params = {
		//     page: 0,
		//     size: 5,
		//     sort: 'updated,DESC',
		//   }
		//   axios({
		//     url: drf.api + 'post' + '/problem',
		//     method: 'get',
		//     headers: {
		//       Authorization : this.accessToken,
		//     },
		//     params: params
		//   })
		//   .then(res => {
		//     this.mainProbs = res.data.content
		//     console.log("problem = ",this.mainProbs)
		//     this.endPage = res.data.totalPages
		//     console.log("totalPage =", res.data)
		//   })
		//   .catch(err => {
		//     console.log("에러")
		//     console.log(err)
		//   })
		// }
	},
	methods: {
		handlePage() {
			console.log('event page= ', Number(event.target.ariaLabel.slice(-1)));
			this.page = Number(event.target.ariaLabel.slice(-1));
			// 1. 검색어 있을 때
			if (this.selectedDB != 'whole') {
				const params = {
					title: ``,
					code: this.selectedDB,
					dtype: 'Problem',
					page: this.page - 1,
					size: 5,
					sort: 'updated,DESC',
				};
				axios({
					url: drf.api + 'post/' + 'search',
					method: 'get',
					headers: {
						Authorization: this.accessToken,
					},
					params: params,
				})
					.then((res) => {
						console.log('prob 서치 =', res.data.content);
						this.selectedProb = res.data.content;
					})
					.catch((err) => {
						console.log('err=', err);
					});
			} else {
				// 2. 검색어 없을 때
				const params = {
					page: this.page - 1,
					size: 5,
					sort: 'updated,DESC',
				};
				axios({
					url: drf.api + 'post' + '/problem',
					method: 'get',
					headers: {
						Authorization: this.accessToken,
					},
					params: params,
				})
					.then((res) => {
						console.log('넘어온 data = ', res.data.content);
						this.mainProbs = res.data.content;
						console.log('현재 data =', this.mainProbs);
					})
					.catch((err) => {
						console.log('에러');
						console.log(err);
					});
			}
		},
	},
};
</script>

<style scoped></style>
