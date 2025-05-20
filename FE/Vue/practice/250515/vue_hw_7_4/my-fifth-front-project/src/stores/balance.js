import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('balance', () => {
  const balances = ref([
    {
    name: '김하나',
    balance: 100000
    },
    {
    name: '김두리',
    balance: 10000
    },
    {
    name: '김서이',
    balance: 100
    },  
  ])

  const fineName = function (selectedName) {
    const findbalances = balances.value.find((balance) => balance.name === selectedName)
    return findbalances
  }

  const onUpdate = function (selectedName) {
    const balance = balances.value.find((balance) => balance.name === selectedName)
    balance.balance += 1000
  }

  return {
    balances,
    fineName,
    onUpdate,
  }
}, {persist : true})