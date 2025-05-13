<template>
  <ProductListItem 
    v-for="product in products"
    :key="product.id"
    :product="product"
  />
</template>

<script setup>
import ProductListItem from './ProductListItem.vue';

const props = defineProps({
  products: Object,
})

</script>

<style scoped>

</style>