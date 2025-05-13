<template>
  <h1>App.vue</h1>
  <Parent :user-name="userName"
  @change-user-name="onChangeUserName"/>
</template>

<script setup>
  import Parent from '@/components/Parent.vue';

  import { ref } from 'vue'
  const userName = ref('Alice')

  const onChangeUserName = function () {
    userName.value = 'Chalie'
  }
</script>

<style scoped>

</style>