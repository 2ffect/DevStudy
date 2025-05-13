<template>
  <h1>ChildItem</h1>
  <p>{{ item.id }}</p>
  <p>{{ item.item }}</p>
  <!-- 버튼 클릭시 someEvent 발생 -->
   <!-- <button @click="$emit('someEvent')">클릭</button> -->
  <!-- emit 이벤트 선언 활용 -->
  <button @click="buttonClick">클릭</button>
</template>

<script setup>
  const props = defineProps({
    item: Object,
  })

  const emit = defineEmits(['someEvent'])
  const buttonClick = function () {
    emit('someEvent', props.item, '파인애플') 
  }
</script>

<style scoped>

</style>