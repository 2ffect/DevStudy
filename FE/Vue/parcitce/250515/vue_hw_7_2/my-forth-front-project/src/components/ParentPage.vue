<template>
  <div>
    <h2>부모 컴포넌트</h2>
    <p>{{ family.father }}</p>
    <p>{{ family.mother }}</p>
    <ChildPage 
      v-for="child in family.children"
      :key="child.name"
      :child="child"
    />
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  
  import ChildPage from './ChildPage.vue';
  
  const props = defineProps({
    family: Object,
  })

</script>


<style scoped>

</style>