<template>
	<v-container fluid class="pa-0 pt-0 pt-md-10 mt-0">
		<!-- row 1: 메인 피드와 sidebar 모두를 감싸는 줄 -->
		<!-- <v-row v-if="!isSearched"> -->
		<v-row>
			<!-- col 1: 메인 피드 부분 -->
			<v-col cols="12" md="7" lg="8" class="mt-2 white pt-0 px-0 rounded-lg">
				<!-- row 1-1: 상단 탭; 문제/문제집, 정보 -->
				<v-row class="d-flex mt-8 ms-8">
					<img src="@/assets/prosn_logo_sm.png" alt="..." class="small-logo" />
					<h2 class="ms-3 dark--text font-weight-regular">F E E D</h2>

					<!-- 피드에 문제, 정보, 스터디 작성을 위한 드롭다운 0817 임지민 -->
					<v-col class="py-0 text-end pr-5 mr-5">
						<div class="mr-5" v-if="isLoggedIn">
							<v-menu offset-y>
								<template v-slot:activator="{ on, attrs }">
									<v-btn icon v-bind="attrs" v-on="on">
										<v-icon color="#a384ff">mdi-plus</v-icon>
									</v-btn>
								</template>
								<v-list>
									<v-list-item v-for="(item, index) in items" :key="index" link>
										<v-list-item-title
											style="color: #a384ff"
											@click="moveToCreate(item.url)"
											>{{ item.title }}</v-list-item-title
										>
									</v-list-item>
								</v-list>
							</v-menu>
						</div>
					</v-col>
				</v-row>

				<!-- 검색창 -->
				<v-col cols="12" class="mt-5 py-0 px-6">
					<v-text-field
						label="🔍 검색어를 입력하세요"
						solo
						rounded
						class="ma-0"
						@keyup.enter="onInputKeyword"
					></v-text-field>
				</v-col>

				<!-- 카테고리  -->
				<v-row class="bottom-border-grey pb-5 mr-2 mx-5 mb-0">
					<v-chip-group column mandatory active-class="clicked-chip">
						<!-- <v-chip class="mr-2 my-2 border-grey" @click="selectCategory('whole','전체')" id="whole" small>#전체</v-chip> -->
						<div v-for="category in categories" :key="category.toDB">
							<v-chip
								class="mr-2 my-2 border-grey"
								:id="category.toDB"
								@click="selectCategory(category.toDB)"
								small
							>
								#{{ category.toUser }}</v-chip
							>
						</div>
					</v-chip-group>
					<div v-if="feedFlag === 1">
						<span class="pt-5">문제집은 검색 기능이 제공되지 않습니다.</span>
					</div>
					<div v-else>
						<div
							v-if="selectedDB != 'whole'"
							class="result"
							style="color: #a384ff; display: inline"
						>
							<div v-for="(categorie, idx) in categories" :key="idx">
								<h2
									style="display: inline"
									v-if="categorie.toDB === selectedDB"
								>
									{{ categorie.toUser }}
									<span v-if="selectedDB != 'whole'" class="pt-5"
										>에 대한 검색 결과입니다.</span
									>
								</h2>
							</div>
						</div>
						<div
							v-if="isSearched"
							class="result"
							style="color: #a384ff; display: inline"
						>
							<h2>
								{{ inputChange }}
								<span class="pt-5">에 대한 검색 결과입니다.</span>
							</h2>
						</div>
					</div>
				</v-row>

				<v-toolbar dark class="mt-10 mx-4" height="45px">
					<v-tabs background-color="#CCA5FE" grow>
						<v-col class="px-0">
							<v-tab class="pa-0" @click="changeToProblemFeed">
								<p
									class="font-weight-regular text-center mb-0"
									style="font-size: 1.2rem"
								>
									PROBLEM/BOOK
								</p>
							</v-tab>
						</v-col>
						<v-col class="px-0">
							<v-tab class="pa-0" @click="changeToInfoFeed">
								<p
									class="font-weight-regular text-center mb-0"
									style="font-size: 1.2rem"
								>
									INFORMATION
								</p>
							</v-tab>
						</v-col>
					</v-tabs>
				</v-toolbar>

				<!-- row 1-2: 피드 컨텐츠 부분 -->
				<v-row>
					<v-col>
						<!-- 메인 피드 1. -- 문제 -->
						<!-- <recent-problem v-if="selectedProb" id="problemFeed" :class="`${problemFeedClass}`" :selectedDB="selectedDB" :selectedProb="selectedProb"></recent-problem> -->
						<recent-problem
							id="problemFeed"
							:class="`${problemFeedClass}`"
							:mainProbs="mainProbs"
						></recent-problem>
						<!-- 메인 피드 2. -- 문제집 -->
						<!-- <main-book v-if="selectedDB != 'whole'" id="BookFeed" :class="`${bookFeedClass}`" :selectedBooks="selectedBooks"></main-book>   
            <main-book v-else id="BookFeed" :class="`${bookFeedClass}`" :mainBooks="mainBooks"></main-book>             -->
						<!-- 메인 피드 3. -- 정보 -->
						<info
							v-if="selectedDB != 'whole'"
							id="infoFeed"
							:class="`${infoFeedClass}`"
							:selectedDB="selectedDB"
							:selectedInfo="selectedInfo"
						></info>
						<info
							v-else
							id="infoFeed"
							:class="`${infoFeedClass}`"
							:mainInfos="mainInfos"
						></info>
					</v-col>
				</v-row>
			</v-col>

			<!-- col 2: 사이드 바 -->
			<v-col md="5" lg="4" class="d-md-flex d-none grey lighten-4">
				<side-bar></side-bar>
			</v-col>
		</v-row>

		<!-- row 2: 메인 피드와 sidebar 모두를 감싸는 줄 (검색 결과가 있을 경우 검색 페이지) -->
		<!-- <v-row v-if="isSearched">
      <search-result-view ></search-result-view>
    </v-row>  -->
	</v-container>
</template>

<script>
import RecentProblem from '../components/MainPage/RecentProblem.vue';
import info from '../components/MainPage/info.vue';
import SideBar from '@/components/SideBar.vue';
import SearchResultView from '@/views/SearchResultView.vue';
import axios from 'axios';
import drf from '@/api/drf.js';
import { mapGetters } from 'vuex';
export default {
	name: 'MainPageView',
	data() {
		return {
			items: [
				{
					title: 'PROBLEM +',
					url: '/createproblem',
				},
				{
					title: 'INFORMATION +',
					url: '/createinfo',
				},
				{
					title: 'STUDY +',
					url: '/createstudy',
				},
			],
			searchTitle: '',
			selectedUser: '전체',
			selectedDB: 'whole',
			toDB: 'whole',
			toUser: '',
			categories: [
				{ toDB: 'whole', toUser: '전체' },
				{ toDB: 'NW', toUser: '네트워크' },
				{ toDB: 'OS', toUser: '운영체제' },
				{ toDB: 'DS', toUser: '자료구조' },
				{ toDB: 'DB', toUser: '데이터베이스' },
				{ toDB: 'AL', toUser: '알고리즘' },
				{ toDB: 'OOP', toUser: '객체지향' },
				{ toDB: 'PL', toUser: '프로그래밍 언어' },
				{ toDB: 'CS', toUser: '컴퓨터 구조' },
				{ toDB: 'TC', toUser: '기술동향' },
				{ toDB: 'SC', toUser: '보안' },
				{ toDB: 'ETC', toUser: '기타' },
			],
			feedFlag: 0,
			problemFeedClass: 'd-flex',
			bookFeedClass: 'd-none',
			infoFeedClass: 'd-none',
			mainInfos: [],
			mainBooks: [],
			mainProbs: [],
			selectedProb: [],
			selectedInfo: [],
			selectedBooks: [],
			titleSearch: '',
		};
	},
	components: {
		RecentProblem,
		info,
		SideBar,
		SearchResultView,
	},
	computed: {
		isSearched() {
			return this.$store.getters['problem/isSearched'];
		},
		inputChange() {
			return this.$store.getters['problem/inputChange'];
		},
		...mapGetters(['accessToken', 'currentUser', 'isLoggedIn']),
	},
	methods: {
		moveToCreate(url) {
			this.$router.push({ path: url });
		},
		changeToProblemFeed() {
			this.feedFlag = 0;
			// console.log(this.feedFlag)
			this.problemFeedClass = 'd-flex';
			this.bookFeedClass = 'd-none';
			this.infoFeedClass = 'd-none';
		},
		changeToInfoFeed() {
			this.feedFlag = 2;
			this.problemFeedClass = 'd-none';
			this.bookFeedClass = 'd-none';
			this.infoFeedClass = 'd-flex';
		},

		onInputKeyword: async function (event) {
			this.searchTitle = event.target.value;
			this.selectCategory(this.toDB);
		},

		async selectCategory(toDB) {
			this.toDB = toDB;
			console.log('호출 toDB : ', toDB);
			// await this.$store.dispatch('reIssue')
			this.selectedProb = [];
			this.selectedInfo = [];
			// this.selectedUser = toUser
			if (this.feedFlag == 0) {
				// 카테고리로 문제 선택
				console.log('문제만 조회');
				if ((toDB === 'whole' || toDB === '') && this.searchTitle === '') {
					console.log('태그가 빈값이나 전체. 검색어 없음. 태그 없음');
					this.selectedDB = toDB;
					this.selectedProb = [];
					const params = {
						page: 0,
						size: 5,
						sort: 'created,DESC',
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
							this.mainProbs = res.data.content;
							console.log('problem = ', this.mainProbs);
							this.endPage = res.data.totalPages;
							// console.log("totalPage =", res.data)
						})
						.catch((err) => {
							console.log('에러');
							console.log(err);
						});
				} else {
					console.log('태그 있거나, 검색있거나, 둘 다 있거나');
					this.selectedProb = [];
					this.selectedDB = toDB;
					this.titleSearch = this.inputChange;

					console.log('title: ', this.searchTitle);
					console.log('code : ', this.selectedDB);
					const params = {
						title: this.searchTitle,
						code: this.selectedDB === 'whole' ? '' : this.selectedDB,
						dtype: 'Problem',
						page: 0,
						size: 5,
						sort: 'created,DESC',
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
							console.log('prob 서치1 =', res.data.content);
							// this.selectedProb = null;
							this.mainProbs = res.data.content;
						})
						.catch((err) => {
							console.log('err=', err);
						});
				}
			} else if (this.feedFlag == 2) {
				// 카테고리로 정보 검색
				if (toDB == 'whole') {
					this.selectedDB = toDB;
					this.selectedInfo = [];
					const params = {
						page: 0,
						size: 5,
						sort: 'created,DESC',
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
							this.mainInfos = res.data.content;
							console.log('info 전체 = ', this.mainInfos);
							this.endPage = res.data.totalPages;
							// console.log("totalPage =", res.data)
						})
						.catch((err) => {
							console.log('에러');
							console.log(err);
						});
				} else {
					this.mainInfos = [];
					this.selectedDB = toDB;
					const params = {
						title: ``,
						code: toDB,
						dtype: 'Information',
						page: 0,
						size: 5,
						sort: 'created,DESC',
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
							console.log(res);
							console.log('info 서치=', res.data.content);
							this.selectedInfo = res.data.content;
						})
						.catch((err) => {
							console.log('err=', err);
						});
				}
			}
		},
		init() {
			this.titleSearch = this.inputChange;
			if (this.titleSearch) {
				this.selectCategory(this.toDB);
			}
			const params = {
				// page: 0,
				// size: 5,
				sort: 'created,DESC',
			};
			// axios({
			// 	url: drf.api + 'post' + '/problem',
			// 	method: 'get',
			// 	headers: {
			// 		Authorization: this.accessToken,
			// 	},
			// 	params: params,
			// })
			// 	.then((res) => {
			// 		this.mainProbs = res.data.content;
			// 		console.log('problem = ', this.mainProbs);
			// 		this.endPage = res.data.totalPages;
			// 		console.log('totalPage =', res.data);
			// 	})
			// 	.catch((err) => {
			// 		console.log('에러');
			// 		console.log(err);
			// 	});
			// 정보
			axios({
				url: drf.postFeed.information(),
				method: 'get',
				params: params,
			})
				.then((res) => {
					this.mainInfos = res.data.content;
				})
				.catch((err) => {
					console.log(err);
				});

			// 문제
			axios({
				url: drf.postFeed.problem(),
				method: 'get',
			})
				.then((res) => {
					this.mainProbs = res.data.content;
				})
				.catch((err) => {
					console.log(err);
				});

			axios({
				url: drf.postFeed.workbook(),
				mehtod: 'get',
			})
				.then((res) => {
					console.log('문제집 조회 =', res.data);
					this.mainBooks = res.data.content;
				})
				.catch((err) => {
					console.log(err);
				});
		},
	},
	created() {
		this.init();
	},
};
</script>

<style>
.bottom-line {
	border-bottom: #a384ff 3px solid;
}
.v-application--wrap {
	max-width: none;
}

/* before로 색을 지정해주니까 hover 했을 때 색이 흰색으로 정상적으로 바뀜 */
.tab-hover::before {
	color: #616161;
}
:hover.tab-hover,
.clicked-main-tab {
	background: #a384ff;
	color: white;
	border-top-left-radius: 10px;
	border-top-right-radius: 10px;
	cursor: pointer;
}
.border-white {
	border: 1px solid white;
}
.container {
	max-width: none;
}
.w-100 {
	width: 100%;
}

/* 2022.08.02. 커스텀 스크롤바 */
/* 필요한 다른 view에서 가져다 쓰면 됨 */
::-webkit-scrollbar {
	width: 8px; /* 스크롤바의 너비 */
}

::-webkit-scrollbar-thumb {
	height: 30%; /* 스크롤바의 길이 */
	background: #a384ff; /* 스크롤바의 색상 */

	border-radius: 10px;
}

::-webkit-scrollbar-track {
	background: rgba(172, 35, 252, 0.2); /*스크롤바 뒷 배경 색상*/
}
.small-logo {
	height: 40px;
	width: 40px;
}
</style>
