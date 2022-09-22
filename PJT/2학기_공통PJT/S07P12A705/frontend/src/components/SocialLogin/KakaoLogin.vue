<template>

</template>

<script>
import axios from 'axios';
import drf from '@/api/drf';
export default {
created() {
    const kakaoCode = new URL(window.location.href).searchParams.get("code");
    console.log("vue에서 출력하는 kakaoCode ==", kakaoCode)
    if (kakaoCode) {
      axios({
        // url:'http://localhost:8080/login/oauth2/code/kakao' + `?code=${kakaoCode}`,
        url:`${drf.social}login/oauth2/code/kakao?code=${kakaoCode}`,
        method: 'get',
      })
      .then(res =>{
        console.log(res.data)
        console.log(res.data.accessToken)
        /*
        accessToken: "EWpduMJ8S1-JROOFJYwtuUSfLBPqwAxP1J8Ou6VdCj102wAAAYKq1JQz"
        email: "dhcoaud98@gmail.com"
        name: "오채명"
        oauthId: 2392181117
        platform: "KAKAO"
        refreshToken: "71QJsxvUXvvfdwrb2WUb6g4ZdktUYu4Sebpjuz2pCj102wAAAYKq1JQx"
        */
        this.$store.dispatch(
          'saveToken',
           res.data.accessToken
        );
        this.$store.dispatch('saveEmail', res.data.email);
        this.$store.dispatch('saveName', res.data.name);
        this.$store.dispatch('saveId', res.data.oauthId);
        this.$store.dispatch('savePlatform', res.data.platform)
        this.$store.dispatch('saveRefreshToken', res.data.refreshToken);
        this.$router.push({path:"/"})
      })
      .catch(err => {
        console.log("에러",err)
      })
    }
  }

}
</script>

<style>

</style>