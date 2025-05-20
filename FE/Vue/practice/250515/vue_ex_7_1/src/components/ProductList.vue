<template>
  <div>
    <h1>Product List</h1>
    <ul v-for="product in store.products" :key="product.id">
      <li>{{ product.id }} - {{ product.title }} - {{ product.body }}</li>
    </ul>  
  </div>
</template>

<script setup>
  import { useProductStore } from '@/stores/product'
  const store = useProductStore()
  console.log(store)
</script>

<style scoped>

</style>