<template>
  <div>
    <h3>자식 페이지입니다</h3>
    <p>이름 : {{ child.name }}</p>
    <p>나이 : {{ child.age }}</p>
  </div>
</template>

<script setup>
  const props = defineProps({
    child: Object,
  })

</script>

<style scoped>
div {
  border: 1px solid black;
  padding: 20px;
}
</style>