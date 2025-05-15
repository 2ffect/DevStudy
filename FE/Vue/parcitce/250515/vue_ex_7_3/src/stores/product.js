import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useProductStore = defineStore('product', () => {
  const products = ref([])

  const productCount = computed(() => products.value.length)

  const deleteProduct = function (productId) {
    // 요소를 직접 수정하는 대신에 splice 메서드를 사용하여 새로운 배열을 생성하여 상태를 업데이트
    const index = products.value.findIndex(product => product.id === productId)
    if (index !== -1) {
      products.value.splice(index, 1)
    }
  }
  
  const loaddata = function () {
    axios.get('https://jsonplaceholder.typicode.com/posts')
      .then(response => {
        console.log('응답 데이터:', response.data)
        products.value = response.data
      })
      .catch(err => {
        console.error('상품 데이터 로딩 실패:', err)
      })
  }

  return {
    products, 
    productCount, 
    deleteProduct,
    loaddata,
  }
})
