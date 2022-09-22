<template>
	<v-container class="mt-5 px-0 px-md-3">
		<!-- v-for 사용하기 -->
		<my-post-list-items
			v-for="(userPost, idx) in userPosts"
			:key="idx"
			:userPost="userPost"
		></my-post-list-items>
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
import MyPostListItems from './MyPostListItems.vue';
import { mapGetters } from 'vuex';

export default {
	name: 'MyPostList',
	components: {
		MyPostListItems,
	},
	data() {
		return {
			userPosts: [],
			nowPage: 1,
			clickPage: null,
			endPage: 0,
			value: null,
			page: 0,
		};
	},
	computed: {
		...mapGetters(['accessToken', 'currentUser']),
	},
	created() {
		this.getMyPostlist();
	},
	methods: {
		async getMyPostlist() {
			await this.$store.dispatch('reIssue');

			const params = {
				page: 0,
				size: 4,
				sort: 'updated,DESC',
			};
			const profileOwnerId = this.$route.params.uid;
			// 유저의 포스트 조회
			axios({
				url: drf.api + 'user/' + 'post/' + `${profileOwnerId}`,
				method: 'get',
				headers: {
					Authorization: this.accessToken,
				},
				params: params,
			}).then((res) => {
				console.log('userPost =', res.data.content);
				this.userPosts = res.data.content;
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
				url: drf.api + 'user/' + 'post/' + `${this.currentUser}`,
				method: 'get',
				headers: {
					Authorization: this.accessToken,
				},
				params: params,
			}).then((res) => {
				console.log('userPost =', res.data.content);
				this.userPosts = res.data.content;
			});
		},
	},
};
</script>

<style></style>
