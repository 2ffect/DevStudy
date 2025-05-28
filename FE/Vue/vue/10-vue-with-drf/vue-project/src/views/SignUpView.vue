<template>
  <div>
    <form @submit.prevent="signup">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username">
      <br>
      <label for="age">age : </label>
      <input type="number" id="age" v-model="age">
      <br>
      <label for="password1">password1 : </label>
      <input type="password" id="password1" v-model="password1">
      <br>
      <label for="password2">password2 : </label>
      <input type="password" id="password2" v-model="password2">
      <br>
      <input type="submit" value="signup">
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useAccountStore } from '@/stores/accounts.js'
  const username = ref(null)
  const password1 = ref(null)
  const password2 = ref(null)
  const age = ref(null)
  const store = useAccountStore()

  const signup = function () {
    const userInfo = {
      username: username.value,
      age : age.value,
      password1: password1.value,
      password2: password2.value,
    }
    store.createUser(userInfo)
  }

</script>

<style>

</style>
