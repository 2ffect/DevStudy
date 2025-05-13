<template>
  <h1>부모 페이지 입니다</h1>
  <ChildPage 
    v-for="child in children"
    :key="child.name"
    :child="child"
    @give-me-allowance="updateBalance"
  />
</template>

<script setup>
  import { ref } from 'vue'
  import ChildPage from './ChildPage.vue';

  const children = ref([
    { name : '김하나', age : 30, balance : 100000},
    { name : '김두리', age : 30, balance : 10000},
    { name : '김서이', age : 30, balance : 1000},
  ])

  const onSomeEvent = function (arg) {
    console.log('이벤트 발생 !!')
    console.log(arg)
    arg.balance += 1000
  }
</script>

<style scoped>

</style>