<template>
  <div>
    <li>
      {{ product.name }} - {{ product.price }} 원
      <button>장바구니에 추가</button>
    </li>
  </div>
</template>

<script setup>
const props = defineProps({
  product : Object,
})

</script>

<style scoped>

</style>