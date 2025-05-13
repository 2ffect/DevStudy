<template>
  <h1>Child</h1>
  <p>{{ userName }}</p>
  <p>{{ parentName }}</p>
  <button @click="$emit('changeUserName')">click</button>
  <ChildItem 
    v-for="item in items"
    :key="item.id"
    :item="item"
    @some-event="onSomeEvent" 
  />
</template>

<script setup>
  import { ref } from 'vue'
  import ChildItem from './ChildItem.vue'

  defineProps({
    userName: String,
    parentName: String
  })

  const items = ref([
    { id: 1, item: '사과'},
    { id: 2, item: '딸기'},
    { id: 3, item: '바나나'},
  ])

  const onSomeEvent = function (arg, name) {
    console.log('이벤트 발생 !!')
    for (let i = 0; i<items.value.length; i += 1) {
      if (arg.id === items.value[i].id) {
        items.value[i].item = name
      }
    }
  }
</script>

<style scoped>

</style>