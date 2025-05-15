<template>
  <div>
    <h2>메인 페이지</h2>
    <div 
      v-for="balance in store.balances"
      :key="balance.name"
    >
      <p>이름 : {{ balance.name }}</p>
      <p>잔고 : {{ balance.balance }}</p>
      <button @click="goUpdate(balance)">
      updateBalance
      </button>
      <hr>
    </div>
  </div>
</template>

<script setup>
  import { useRouter } from 'vue-router'
  import { useBalanceStore } from '@/stores/balance'

  const router = useRouter()

  const store = useBalanceStore()

  const goUpdate = function (balance) {
    router.push({ name: 'update', params: { name: balance.name}})
  }
</script>

<style scoped>

</style>