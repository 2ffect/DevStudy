<template>
  <div>
    <h3>자식 페이지</h3>
    <p>{{ child.name }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  child : Object
})
</script>

<style scoped>

</style>