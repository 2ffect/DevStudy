import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('product', () => {
  let id = 0

  const products = ref([
    {id: id++, title: 'Product1', body: 'quia et sucipit'},
    {id: id++, title: 'Product2', body: 'quo iure voluptatem'},  
    {id: id++, title: 'Product3', body: 'requdiandae'},
  ])
  return {
    products
  }
})
