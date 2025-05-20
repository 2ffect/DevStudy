<template>
  <div>
    <h1>쇼핑 애플리케이션</h1>
      <ProductList :products="products" 
      @add-to-cart="addCartList"
      />
    <p>총 가격 : {{ totalPrice }} 원</p>
    <h1>장바구니</h1>
      <Cart :cartList="cartList"
      @delete-to-cart="deleteCartList"
      />
  </div>
</template>

<script setup>
import { ref, watchEffect } from 'vue'
import ProductList from '@/components/ProductList.vue'
import Cart from '@/components/Cart.vue'

let id = 0

const products = ref([
  { id: id++, name: '사과', price: 1000 },
  { id: id++, name: '바나나', price: 1500 },
  { id: id++, name: '딸기', price: 2000 },
  { id: id++, name: '포도', price: 3000 },
  { id: id++, name: '복숭아', price: 2000 },
  { id: id++, name: '수박', price: 5000 }
])

const cartList = ref([
])

const addCartList = function (product) {
  // console.log(product)
  cartList.value.push(product)
}

const deleteCartList = function (product) {
  const index = cartList.value.findIndex(item => item.id === product.id)

  if (index !== -1) {
    cartList.value.splice(index, 1)
  }
}

const totalPrice = ref(0)

watchEffect (() => {
  totalPrice.value = 0
  cartList.value.forEach((product) => {
    totalPrice.value += product.price
  })
})


</script>
