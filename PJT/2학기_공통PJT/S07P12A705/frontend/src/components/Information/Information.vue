<template>
	<!-- 2022.08.04 정보 페이지 -->
	<v-container mt-5>
		<v-row class="mt-5 justify-space-between">
			<h2>{{ infoDetail.title }}</h2>
			<v-btn @click="goBack()" text class="font-weight-bold">뒤로가기</v-btn>
		</v-row>

		<v-row>
			<v-col>
				<span v-for="tag in infoDetail.tags" :key="tag">
					<v-chip small color="#A384FF" class="white--text mr-2"
						>#{{ tag }}</v-chip
					>
				</span>
			</v-col>
		</v-row>

		<v-row>
			<v-card
				outlined
				class="mx-3 mb-2 pa-3 overflow-y-auto text-truncate"
				max-height="100px"
				width="100%"
			>
				<v-card-text>
					{{ infoDetail.mainText }}
				</v-card-text>
			</v-card>
		</v-row>

		<!-- 저작권 / 버튼 -->
		<v-row class="d-flex justify-space-between">
			<!-- 출제자 정보 -->
			<v-col class="pa-0">
				<span class="grey--text mr-2 mb-1"
					>Created by.
					<v-btn
						class="px-0 mb-1 font-weight-bold"
						plain
						@click="profileEvent(infoDetail.writer.id)"
					>
						{{ infoDetail.writer.name }}
					</v-btn>
				</span>
			</v-col>

			<!-- <v-col @click="profileEvent(infoDetail.writer.id)">
        <div class="me-4 d-flex align-center font-weight-mid">Created By. {{ infoDetail.writer.name }}</div>
      </v-col> -->

			<!-- 버튼: 남이 작성한 정보 -->
			<v-col
				v-if="currentUser != infoDetail.writer.id"
				cols="8"
				class="pa-0 justify-end d-flex align-center"
			>
				<!-- 좋아요 버튼 -->
				<div>
					<v-btn
						class="ms-1"
						icon
						color="dark lighten-2"
						@click="changeLikeStatus"
						id="upIcon"
						large
					>
						<v-icon>{{ upText }}</v-icon>
					</v-btn>
					<span>{{ infoDetail.numOfLikes }}</span>
				</div>
				<!-- 싫어요 버튼 -->
				<div>
					<v-btn
						class="ms-1"
						icon
						color="dark lighten-2"
						@click="changeHateStatus"
						id="downIcon"
						large
					>
						<v-icon>{{ downText }}</v-icon>
					</v-btn>
					<span>{{ infoDetail.numOfDislikes }}</span>
				</div>
				<!-- 스크랩 버튼 -->
				<div v-if="isLoggedIn">
					<v-btn
						class="ms-2"
						icon
						color="dark lighten-2"
						@click="openScrapModal"
						id="scrapIcon"
						large
					>
						<v-icon>{{ scrapText }}</v-icon>
					</v-btn>
					<!-- <scrap @close="closeScrapModal" v-if="scrapModal" :pid="probDetail.id"></scrap> -->
					<scrap
						@close="closeScrapModal"
						v-if="scrapModal"
						:pid="infoDetail.id"
					></scrap>
				</div>
			</v-col>

			<!-- 내가 작성한 정보 -->
			<v-col v-else cols="8" class="pa-0 justify-end d-flex align-center">
				<div v-if="isLoggedIn">
					<!-- 스크랩 버튼 -->
					<v-btn
						class="ms-2"
						icon
						color="dark lighten-2"
						@click="openScrapModal"
						id="scrapIcon"
						large
					>
						<v-icon>{{ scrapText }}</v-icon>
					</v-btn>
					<!-- 삭제 -->
					<v-btn
						type="submit"
						color="red"
						rounded
						outlined
						class="ms-1"
						large
						@click="deleteinfo"
						>삭제</v-btn
					>
				</div>
			</v-col>
		</v-row>

		<v-divider color="#A384FF" class="mt-6"></v-divider>

		<v-row>
			<!-- 댓글 -->
			<v-col cols="12" class="pa-0">
				<info-modal-reply
					:commentList="commentList"
					:cid="infoDetail.id"
				></info-modal-reply>
			</v-col>
		</v-row>
	</v-container>
</template>

<script>
import InfoModalReply from '@/components/InfoModal/InfoModalReply.vue';
import { mapGetters } from 'vuex';
import axios from 'axios';
import drf from '@/api/drf.js';
import Scrap from '@/components/Scrap/Scrap.vue';

export default {
	name: 'Information',
	data() {
		return {
			upText: 'thumb_up_off_alt',
			downText: 'thumb_down_off_alt',
			scrapText: 'bookmark_border',
			scrapModal: false,
			infoDetail: [],
			commentList: [],
		};
	},
	components: {
		InfoModalReply,
		Scrap,
	},
	computed: {
		...mapGetters(['accessToken', 'currentUser', 'isLoggedIn']),
	},
	methods: {
		// 2022.08.04. 라우터 경로 연결
		goBack() {
			this.$router.go(-1);
		},
		openScrapModal() {
			this.scrapModal = true;
			console.log('openModal');
		},
		closeScrapModal() {
			this.scrapModal = false;
			console.log('closeModal');
		},
		profileEvent(uid) {
			this.$router.push({ path: `../profile/${uid}` });
		},
		changeLikeStatus() {
			if (this.isLoggedIn) {
				/* 
        버튼 클릭하면 색이 바뀌도록
        thumb up --> thumb up off alt
        thumb down --> thumb down off alt
        bookmark border --> bookmark
        */

				// 좋아요 엑쇼스 0815 임지민
				// axios 보내기
				axios({
					url: drf.postFeed.likeordis(),
					method: 'post',
					headers: {
						Authorization: this.accessToken,
					},
					data: {
						pid: this.probdetail.id,
						type: true,
					},
				})
					.then((res) => {
						// 받아온 데이터를 작성 전/후로 구분하는 작업 필요(0808 임지민)
						console.log(res);
						this.probdetail.numOfLikes = res.data.numOfLikes;
					})
					.catch((err) => {
						// console.log(this.accessToken)
						// console.log(this.userId)
						console.log(err);
					});
				/* 싫어요가 눌려 있는 상태에서 좋아요를 누르면 싫어요가 취소되는 것도 추가 */
				// console.log(document.querySelector('#correctStatus'));
				if (this.upText === 'thumb_up_off_alt') {
					// 좋아요를 눌러야 하는데 이미 싫어요가 눌려져 있는 상태
					if (this.downText === 'thumb_down') {
						// console.log(this.downText)
						this.changeHateStatus();
						this.downText = 'thumb_down_off_alt';
					}
					this.upText = 'thumb_up';
				} else {
					this.upText = 'thumb_up_off_alt';
				}
			}
		},
		changeHateStatus() {
			if (this.isLoggedIn) {
				// 싫어요 엑쇼스 0815 임지민
				// axios 보내기
				axios({
					url: drf.postFeed.likeordis(),
					method: 'post',
					headers: {
						Authorization: this.accessToken,
					},
					data: {
						pid: this.probdetail.id,
						type: false,
					},
				})
					.then((res) => {
						// 받아온 데이터를 작성 전/후로 구분하는 작업 필요(0808 임지민)
						console.log(res);
						this.probdetail.numOfDislikes = res.data.numOfDislikes;
					})
					.catch((err) => {
						// console.log(this.accessToken)
						// console.log(this.userId)
						console.log(err);
					});
				/* 좋아요가 눌려 있는 상태에서 싫어요를 누르면 좋아요가 취소되는 것도 추가 */
				if (this.downText === 'thumb_down_off_alt') {
					this.downText = 'thumb_down';
					// 싫어요를 눌렀는데 이미 좋아요가 눌러져 있는 상태
					if (this.upText === 'thumb_up') {
						this.changeLikeStatus();
						this.upText = 'thumb_up_off_alt';
					}
				} else {
					this.downText = 'thumb_down_off_alt';
				}
			}
		},
		changeScrapStatus() {
			if (this.scrapText === 'bookmark_border') {
				this.scrapText = 'bookmark';
			} else {
				this.scrapText = 'bookmark_border';
			}
		},

		// 내가 작성한 정보 삭제하기(0815 오채명)
		deleteprob() {
			const userDecision = confirm('정말로 삭제하시겠습니까?');
			if (userDecision) {
				axios({
					url: drf.api + 'post' + `/${this.infoDetail.id}`,
					method: 'delete',
					headers: {
						Authorization: this.accessToken,
					},
				})
					.then((res) => {
						console.log('res.data = ', res.data);
						// console.log("삭제 되었습니다. ", res)
						this.$router.push('/');
					})
					.catch((err) => {
						console.log('에러');
						console.log(err);
					});
				// this.$router.go(); // 새로고침
			}
		},
	},
	created() {
		// console.log('problem ')
		const infoId = this.$route.params.cid;
		// console.log('probid=', probId)

		axios({
			url: drf.api + 'post/' + `${infoId}`,
			method: 'get',
			headers: {
				Authorization: this.accessToken,
			},
		})
			.then((res) => {
				console.log('res:', res); //ok
				this.infoDetail = res.data;
				this.commentList = res.data.comments.reverse();
			})
			.catch((err) => {
				console.log(err);
			});
	},
};
</script>

<style></style>
