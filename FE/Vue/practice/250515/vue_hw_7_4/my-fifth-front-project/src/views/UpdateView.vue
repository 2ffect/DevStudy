<template>
  <div>
    <h1>데이터 수정 페이지</h1>
    <p>이름 : {{ route.params.name }}</p>
    <p>잔고 : {{ findbalance.balance }}</p>
    <button @click="onUpdate(name.name)">+</button>
  </div>
</template>

<script setup>
  import { useRoute } from 'vue-router'
  import { useBalanceStore } from '@/stores/balance'

  const route = useRoute()
  const store = useBalanceStore()
  console.log(store)

  const findbalance = store.fineName(route.params.name)
  console.log(findbalance)

  const onUpdate = function () {
    store.onUpdate(route.params.name)
  }

</script>

<style scoped>

</style>