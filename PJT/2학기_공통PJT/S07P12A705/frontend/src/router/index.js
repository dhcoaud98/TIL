import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPageView from '@/views/MainPageView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import StudyView from '@/views/StudyView.vue'
import NoteView from '@/views/NoteView.vue'
import ProfilePageView from '@/views/ProfilePageView.vue'
import CreateStudy from '@/components/Study/CreateStudy.vue'
import CreateProblem from '@/components/Profile/CreateProblem.vue'
import CreateInfo from '@/components/Profile/CreateInfo.vue'
import CreateNote from '@/components/Note/CreateNote.vue'
import Information from '@/components/Information/Information.vue'
import Problem from '@/components/Problem/Problem.vue'
import ProblemBook from '@/components/ProblemBook/ProblemBook.vue'
import NoteDetail from '@/components/Note/NoteDetail.vue'
import editStudy from '@/components/Study/editStudy.vue'
import KakaoLogin from '@/components/SocialLogin/KakaoLogin.vue'
import GoogleLogin from '@/components/SocialLogin/GoogleLogin.vue'
import NaverLogin from '@/components/SocialLogin/NaverLogin.vue'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'mainPage',
    component: MainPageView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signUp',
    component: SignUpView
  },
  {
    path: '/study',
    name: 'study',
    component: StudyView
  },
  {
    path: '/note',
    name: 'note',
    component: NoteView
  },
  {
    path: '/note/post/:noteId',
    name: 'noteDetail',
    component: NoteDetail
  },
  {
    path: '/note/pre/:noteId',
    name: 'createNote',
    component: CreateNote
  },
  // 회원가입, 로그인 구현 후 username 받을 수 있으면 path 뒤에 /:username 붙이기(1/3 0729임지민)
  {
    path: '/profile/:uid',
    name: 'profile',
    component: ProfilePageView
  },
  {
    path: '/createstudy',
    name: 'createstudy',
    component: CreateStudy
  },
  {
    path: '/createproblem',
    name: 'createproblem',
    component: CreateProblem
  },
  {
    path: '/createinfo',
    name: 'createinfo',
    component: CreateInfo
  },
  {
    path: '/problem/:pid',
    name: 'problem',
    component: Problem
  },
  {
    path: '/problembook/:bid',
    name: 'problembook',
    component: ProblemBook
  },
  {
    path: '/information/:cid',
    name: 'information',
    component: Information
  },
  {
    path: '/editstudy/:sid',
    name: 'editstudy',
    component: editStudy,
    props: true,
  },
  {
    path: '/login/oauth2/code/kakao',
    name: 'KakaoLogin',
    component: KakaoLogin ,
  },
  {
    path: '/login/oauth2/code/google',
    name: 'googleLogin',
    component: GoogleLogin ,
  },
  {
    path: '/login/oauth2/code/naver',
    name: 'naverLogin',
    component: NaverLogin ,
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router