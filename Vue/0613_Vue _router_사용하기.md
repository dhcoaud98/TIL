# 06.13

## Vue router 사용하기



1. 프로젝트 생성 및 이동

   ```
   $ vue create my-router-app
   $ cd my-router-app
   ```

2. Vue Router plugin 설치(Vue CLI 환경)

   ```
   $ vue add router
   ```

3. commit & History mode 사용 여부 (Yes)

4. 프로젝트 변화

   1. App.vue 코드

   2. router/index.js 생성

      - 라우트에 관련된 정보 및 설정이 작성 되는 곳

   3. views 디렉토리 생성

      - ```
        <router-link>
        ```

        - 사용자 네비게이션을 가능하게 하는 컴포넌트
        - 목표 경로는 'to' prop으로 지정됨
        - HTML5 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 브라우저가 페이지를 다시 로드 하지 않도록함
        - a 태그지만 우리가 알고 있는 GET 요청을 보내는 a 태그와 조금 다르게, 기본 GET 요청을 보내는 이벤트를 제거한 형태로 구성됨

      - ```
        <router-view>
        ```

        - 주어진 라우트에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
        - 실제 component가 DOM에 부착되어 보이는 자리를 의미
        - router-link를 클릭하면 해당 경로와 연결되어 있는 index.js에 정의한 컴포넌트가 위치

   4. History mode

      - HTML History API를 사용해서 router를 구현한 것
      - 브라우저의 히스토리는 남기지만 실제 페이지는 이동하지 않는 기능을 지원
      - 즉, 페이지를 다시 로드하지 않고 URL을 탐색할 수 있음 (SPA의 단점 중 하나인 "URL이 변경되지 않는다"를 해결한다.)
      - history 객체는 사용자를 자신의 방문 기록 앞과 뒤로 보내거나, 기록의 특정 지점으로 이동하는 등 유용한 메서드와 속성을 가진다.

## 2. Named routes

- 다음과 같이 사용

  1. `App.vue`

  ```java
  <template>
    <div id="app">
      <nav>
        <router-link v-bind:to="{ name: 'home' }">Home</router-link> | 
        <!-- <router-link v-bind:to="{ name: 'about' }">About</router-link> |    -->
        <router-link v-bind:to="{ name: 'lunch' }">Lunch</router-link> |
        <router-link v-bind:to="{ name: 'lotto', params: { lottoNum: 6 } }">Lotto</router-link>
      </nav>
      <router-view/>
    </div>
  </template>
  
  <style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
  
  nav {
    padding: 30px;
  }
  
  nav a {
    font-weight: bold;
    color: #2c3e50;
  }
  
  nav a.router-link-exact-active {
    color: #42b983;
  }
  </style>
  ```

  1. `index.js`

  ```java
  import Vue from 'vue'
  import VueRouter from 'vue-router'
  import HomeView from '../views/HomeView.vue'
  import TheLotto from '../views/TheLotto.vue'
  import TheLunch from '../views/TheLunch.vue'
  
  Vue.use(VueRouter)
  
  const routes = [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    // },
    {
      path: '/lotto/:lottoNum',
      name: 'lotto',
      component: TheLotto
    },
    {
      path: '/lunch',
      name: 'lunch',
      component: TheLunch
    }
  ]
  
  const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
  })
  
  export default router
  ```
