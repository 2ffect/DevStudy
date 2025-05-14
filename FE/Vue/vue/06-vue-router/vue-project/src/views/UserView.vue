<template>
  <div>
    <h1>User Page</h1>
    <button @click="goHome">Home</button>
    <h2>현재 경로에 관련된 정보 {{ user }}</h2>
    <h2>현재 경로에 관련된 정보 {{ user.id }}</h2>
    <hr>
    <RouterLink :to="{ name: 'userProfile'}">Profile</RouterLink>
    <RouterLink :to="{ name: 'userPosts'}">Posts</RouterLink>
    <RouterView />
    
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter, RouterLink, RouterView, onBeforeRouteLeave } from 'vue-router'

const route = useRoute()
const router = useRouter()
const user = ref(route.params)

console.log(route)
console.log(router)

const goHome = function () {
  router.push(
    {name: 'home'}
  )
}

onBeforeRouteLeave((to, from) => {
  const answer = window.confirm('야외수업 가실래용 ?')
  if (answer === false) {
    return false
  }
})

</script>

<style scoped>

</style>