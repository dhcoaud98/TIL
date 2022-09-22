<template>
	<v-container class="mt-5 px-0 px-md-3">
		<v-row>
			<v-col class="text-center">
				<p v-if="!myStudys.length">아직 신청한 스터디가 없습니다</p>
			</v-col>
		</v-row>
		<my-study-list-items
			v-for="(myStudy, idx) in myStudys"
			:key="idx"
			:myStudy="myStudy"
		></my-study-list-items>
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
import MyStudyListItems from './MyStudyListItems.vue';
import { mapGetters } from 'vuex';

export default {
	name: 'MyStudyList',
	components: {
		MyStudyListItems,
	},
	data() {
		return {
			value: null,
			nowPage: 1,
			endPage: 0,
			myStudys: [],
			page: 0,
			noMyStudy: false,
		};
	},
	computed: {
		...mapGetters(['accessToken']),
	},
	created() {
		// 0813 오채명
		// 전체 스터디 조회
		const params = {
			page: 0,
			size: 5,
		};
		console.log('내 스터디 확인하기~');

		axios({
			url: drf.study.study() + 'me',
			method: 'get',
			headers: {
				Authorization: this.accessToken,
			},
			params: params,
		})
			.then((res) => {
				console.log('res1=', res.data.content);
				this.myStudys = res.data.content;
				this.endPage = res.data.totalPages;
				console.log('totalPages =', res.data.totalPages);
			})
			.catch((err) => {
				console.log('에러');
				console.log(err);
			});
		// if (!this.myStudys.length) {
		//   this.noMyStudy = true
		// }
	},
	methods: {
		// 페이지 네이션 엑시오스
		handlePage() {
			console.log('event = ', Number(event.target.ariaLabel.slice(-1)));
			this.page = Number(event.target.ariaLabel.slice(-1));

			const params = {
				page: this.page - 1,
				size: 5,
				//sort: onUpdated, 'desc'
			};
			axios({
				url: drf.study.study() + 'me',
				method: 'get',
				headers: {
					Authorization: this.accessToken,
				},
				params: params,
			})
				.then((res) => {
					console.log('res2=', res.data.content);
					this.myStudys = res.data.content;
				})
				.catch((err) => {
					console.log('에러');
					console.log(err);
				});
		},
	},
};
</script>

<style></style>
