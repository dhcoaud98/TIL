<template>

</template>

<script>
import axios from 'axios';
import drf from '@/api/drf';
export default {
created() {
    const naverCode = new URL(window.location.href).searchParams.get("code");
    const naverState = new URL(window.location.href).searchParams.get("state");
    console.log("vue에서 출력하는", new URL(window.location.href))
    console.log("vue에서 출력하는", new URL(window.location.href).searchParams.get("state"))
    console.log("vue에서 출력하는 naverCode ==", naverCode)
    if (naverCode) {
      axios({
        // url: 'http://localhost:8080/login/oauth2/code/naver' + `?code=${naverCode}` + `&state=${naverState}`,
        url:`${drf.social}login/oauth2/code/naver?code=${naverCode}&state=${naverState}`,
        method: 'get',
      })
      .then(res =>{
        console.log("naverres=", res)
        // accessToken: "AAAAObAM1RLz9MiUMInVEtYt1r4FxNtO6rY8p-gTIrb-rj-5ENpaFLoRAMo5QIyyOzC9SuSJ9qswnEweSj3mlQaffl4"
        // email: "dhcoaud98@naver.com"
        // name: "오채명"
        // oauthId: "JJf2eatBY8myGe2pzafyfn_8_RD47U7VVltK6RP0kzg"
        // platform: "NAVER"
        // refreshToken: "1VOHkxs0xO7fOZddClBMis6P5J
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