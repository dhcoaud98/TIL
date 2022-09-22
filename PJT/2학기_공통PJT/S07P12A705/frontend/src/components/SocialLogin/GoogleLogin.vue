<template>

</template>

<script>
import axios from 'axios';

export default {
created() {
    const googleCode = new URL(window.location.href).searchParams.get("code");
    console.log("vue에서 출력하는 googleCode ==", googleCode)
    if (googleCode) {
      axios({
        url: 'http://localhost:8080/login/oauth2/code/google' + `?code=${googleCode}`,
        method: 'get',
      })
      .then(res =>{
        console.log(res.data)
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