<template>
  <div>
    <h1>부모 페이지 입니다</h1>
    <ChildPage 
      v-for="child in children"
      :key="child.name"
      :child="child"
    />
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import ChildPage from './ChildPage.vue';

  const children = ref([
    { name : '김하나', age : 30 },
    { name : '김두리', age : 20 },
    { name : '김서이', age : 10 },
  ])

</script>

<style scoped>
div {
  border: 1px solid black;
}
</style>