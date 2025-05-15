<template>
  <div>
    <p>state : {{ store.count }}</p>
    <p>getters : {{ store.doubleCount }}</p>
    <button @click="store.increment">click</button>
    <hr>
    <Example />
  </div>
</template>

<script setup>
  import Example from './components/Example.vue'
  import { useCounterStore } from './stores/counter'
  const store = useCounterStore()

  console.log(store.count)

</script>

<style scoped>

</style>