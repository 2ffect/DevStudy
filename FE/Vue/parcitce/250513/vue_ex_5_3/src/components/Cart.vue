<template>
  <li
    v-for="product in cartList"
    :key="product.id"
  >
    {{ product.name }} - {{ product.price }}원
    <button @click="deleteToCart(product)">삭제</button>
  </li>
</template>

<script setup>
const props = defineProps({
  cartList : Object
})

const emit = defineEmits(['deleteToCart'])
const deleteToCart = function (product) {
  emit('deleteToCart', product)
}

</script>


<style scoped>

</style>