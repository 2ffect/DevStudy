<!-- views/LoginView.vue -->

<template>
  <div>
    <form @submit.prevent="onLogIn">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username">
      <br>
      <label for="password">password : </label>
      <input type="password" id="password" v-model="password">
      <br>

      <input type="submit" value="signup">
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useAccountStore } from '@/stores/accounts.js'
  const username = ref(null)
  const password = ref(null)
  const store = useAccountStore()

  const onLogIn = function () {
    const userInfo = {
      username: username.value,
      password: password.value,
    }
    store.logIn(userInfo)
  }

</script>

<style>

</style>
