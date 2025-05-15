<template>
  <div>
    <nav>
      <RouterLink :to="{name:'main'}">main</RouterLink>
    </nav>
    <h1>pinia + router 연습하기</h1> 
    <RouterView />
  </div>
</template>

<script setup>
  import MainPage from '@/components/MainPage.vue';
  import UpdateView from './views/UpdateView.vue';
  import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>

</style>