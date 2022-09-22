// const HOST = 'http://localhost:8080/api/';
const HOST = 'http://i7a705.p.ssafy.io:8080/api/';
const SOCIAL = 'http://i7a705.p.ssafy.io:8080/';
// 유저 관련
const USER = 'user/';
// 스터디 관련
const STUDY = 'study/';
// 댓글 관련
const COMMENT = 'comment/';
// 문제, 정보 관련
const POSTFEED = 'post/';
// 오답노트 관련
const WRONGANSWER = 'wrongAnswer/';
// 문제 풀이 현황 관련
const SOLVING = 'solving/';
// 스크랩 관련
const SCRAP = 'scrap/'


export default {
	accounts: {
		login: () => HOST + USER + 'login/',
		join: () => HOST + USER + 'join/',
		logout: () => HOST + USER + 'logout/',
    ranking: () => HOST + USER + 'ranking/',
		reissue: () => HOST + USER + 'reissue/',
	},
	api: HOST,
	social: SOCIAL,
	study: {
		study: () => HOST + STUDY,
		// + `${pageId}/`,
	},
	comment: {
		COMMENT,
	},
	postFeed: {
		problem: () => HOST + POSTFEED + 'problem/',
		information: () => HOST + POSTFEED + 'information/',
		likeordis: () => HOST + POSTFEED +'click/',
		workbook: () => HOST + POSTFEED + 'workbook/',
	},
	wrongAnswer: {
		wrongAnswer: () => HOST + WRONGANSWER,
	},
	solving: {
		solving: () => HOST + SOLVING,
	},
	scrap: {
		scrap: () => HOST + SCRAP,
		folder: () => HOST + SCRAP + 'folder/'
	
	}
};

