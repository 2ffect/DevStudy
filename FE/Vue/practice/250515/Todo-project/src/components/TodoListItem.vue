<template>
  <div>
    <input type="checkbox" :id="todo.id" v-model="isDone" >
    <!-- 
      label의 for와 같은 값을 가진 id를 찾아서
      label에 작성된 textContent 를 click 하면 
      찾아둔 동일 id를 가진 요소에 focus
    -->
    <label :for="todo.id" :class="{'is-done' : todo.isDone}">{{ todo.text }}</label>
    <button @click="ondeleteTodo">삭제</button>
  </div>
</template>

<script setup>
  import { ref, watch } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  
  const props = defineProps({
    todo: Object
  })
  
  const store = useCounterStore()
  const isDone = ref(props.todo.isDone)
  
  watch(isDone, () => {
    store.updateTodo(props.todo.id)
  })

  const ondeleteTodo = function() {
    store.deleteTodo(props.todo.id)
  }
  
</script>

<style scoped>
.is-done {
  text-decoration: line-through;
}
</style>