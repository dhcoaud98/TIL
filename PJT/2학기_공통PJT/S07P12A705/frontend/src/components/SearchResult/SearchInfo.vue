<template>
	<div>
		<v-row class="pa-0 ma-0" rounded>
			<v-col cols="12" class="pa-0">
				<search-info-items
					v-for="(info, idx) in infos"
					:key="idx"
					:info="info"
				></search-info-items>
				<v-pagination
					v-model="nowPage"
					:length="endPage"
					color="#A384FF"
					circle
					@input="handlePage()"
				></v-pagination>
			</v-col>
		</v-row>
	</div>
</template>

<script>
import axios from 'axios';
import drf from '@/api/drf';
import SearchInfoItems from '@/components/SearchResult/SearchInfoItems.vue';
import { mapGetters } from 'vuex';

export default {
	data() {
		return {
			totalInfos: [],
			infos: [],
			nowPage: 1,
			clickPage: null,
			endPage: 0,
			value: null,
			page: 0,
		};
	},
	components: {
		SearchInfoItems,
	},
	computed: {
		...mapGetters(['accessToken'])
	},
	created() {
		// 0810 오채명 : 밑에 코드 절때로 건들이지 말기
		// 페이지 렌더링 될 때 첫번 째 엑시오스
		const params = {
			page: 0,
			size: 5,
			sort: 'updated,DESC',
		};
		axios({
			// 0808 오채명 : 모든 게시글, 문제 가져올 때 확인하려고 위의 주소로 했는데, 밑에꺼로 해야함
			url: drf.api + 'post' + '/information',
			method: 'get',
			headers: {
				Authorization: this.accessToken,
			},
			params: params,
			//page=0&size=3&sort=updated,desc
		})
			.then((res) => {
				this.infos = res.data.content;
				console.log('infos = ', this.infos);
				// console.log(res.data.totalPages)
				this.endPage = res.data.totalPages;
			})
			.catch((err) => {
				console.log('에러');
				console.log(err);
			});
	},
	methods: {
		handlePage() {
			console.log('event = ', Number(event.target.ariaLabel.slice(-1)));
			this.page = Number(event.target.ariaLabel.slice(-1));

			const params = {
				page: this.page - 1,
				size: 5,
				sort: 'updated,DESC',
			};
			axios({
				url: drf.api + 'post' + '/information',
				method: 'get',
				headers: {
					Authorization: this.accessToken,
				},
				params: params,
			})
				.then((res) => {
					console.log('넘어온 data = ', res.data.content);
					this.infos = res.data.content;
					console.log('현재 data =', this.infos);
				})
				.catch((err) => {
					console.log('에러');
					console.log(err);
				});
		},
	},
};
</script>

<style scoped></style>
