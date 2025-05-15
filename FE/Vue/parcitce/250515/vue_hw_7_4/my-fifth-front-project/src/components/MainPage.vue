<template>
  <header>
    <div>
      <MainView />
    </div>
  </header>
</template>

<script setup>
  import { ref } from 'vue'
  import { RouterLink, RouterView } from 'vue-router'
  import MainView from '@/views/MainView.vue'
  import UpdateView from '@/views/UpdateView.vue'


</script>

<style scoped>

</style>