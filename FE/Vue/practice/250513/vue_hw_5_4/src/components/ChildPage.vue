<template>
  <h3>자식 페이지 입니다.</h3>
  <p>이름 : {{ child.name }}</p>
  <p>나이 : {{ child.age }}</p>
  <p>용돈 : {{ child.balance }}</p>
  <button @click="buttonClick">용돈 주세요.</button>
</template>

<script setup>
  const props = defineProps({
    child : Object,
  })

  const emit = defineEmits(['giveMeAllowance'])
  const buttonClick = function () {
    emit('giveMeAllowance', props.child)
  }

</script>

<style scoped>

</style>