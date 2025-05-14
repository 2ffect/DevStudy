<template>
  <div>
    <h1>User Profile</h1>
    <p>Username : {{ user.username }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
console.log(route)
const user = ref(route.params)

</script>

<style scoped>

</style>