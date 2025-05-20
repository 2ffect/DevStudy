<template>
  <form @submit.prevent="onAddTodo(todoText)">
    <input v-model="todoText" type="text">
    <button>CREATE</button>
  </form>
</template>

<script setup>
  import { ref } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  const store = useCounterStore()

  const todoText = ref('')
  const onAddTodo = function () {
    store.addTodo(todoText.value)
    todoText.value = ''
  }
</script>

<style scoped>

</style>