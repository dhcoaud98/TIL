<template>
	<v-container class="mt-5 px-0 px-md-3">
		<!-- v-for 사용하기 -->
		<solved-problem-list-items
			v-for="(userSolving, idx) in userSolvings"
			:key="idx"
			:userSolving="userSolving"
		></solved-problem-list-items>
		<br />
		<v-pagination
			v-model="nowPage"
			:length="endPage"
			color="#A384FF"
			circle
			@input="handlePage()"
		></v-pagination>
	</v-container>
</template>

<script>
import axios from 'axios';
import drf from '@/api/drf';
import SolvedProblemListItems from './SolvedProblemListItems.vue';
import { mapGetters } from 'vuex';

export default {
	name: 'SolvedProblemList',
	components: {
		SolvedProblemListItems,
	},
	data() {
		return {
			userSolvings: [],
			nowPage: 1,
			endPage: 0,
		};
	},
	computed: {
		...mapGetters(['accessToken', 'currentUser']),
	},
	created() {
		this.getSovledProblem();
	},
	methods: {
		async getSovledProblem() {
			await this.$store.dispatch('reIssue');
			const params = {
				page: 0,
				size: 4,
				sort: 'updated,DESC',
			};
			// 유저의 solving problem 조회
			axios({
				url: drf.api + 'solving',
				method: 'get',
				headers: {
					Authorization: this.accessToken,
				},
				params: params,
			}).then((res) => {
				console.log('userSolvings =', res.data.content);
				this.userSolvings = res.data.content;
				this.endPage = res.data.totalPages;
			});
		},
		handlePage() {
			console.log('event = ', Number(event.target.ariaLabel.slice(-1)));
			this.page = Number(event.target.ariaLabel.slice(-1));

			const params = {
				page: this.page - 1,
				size: 4,
				sort: 'updated,DESC',
			};
			axios({
				url: drf.api + 'solving',
				method: 'get',
				headers: {
					Authorization: this.accessToken,
				},
				params: params,
			}).then((res) => {
				console.log('userSolvings =', res.data.content);
				this.userSolvings = res.data.content;
			});
		},
	},
};
</script>

<style></style>
