// store/articles.js
import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([
    {id: 1, title: 'title 1', content: 'content 1'},
    {id: 2, title: 'title 2', content: 'content 2'},
  ])
  
  const API_URL = 'http://127.0.0.1:8000'
  const getArticles = function () {
    axios({
      method: 'GET',
      // 자주 요청 보내게 될 API_URL 변수로 관리
      url: `${API_URL}/api/v1/articles/`
    })
      .then(res => {
        // console.log(res)
        // console.log(res.data)
        articles.value = res.data
      })
      .catch(err => console.log(err))
  }


  return { 
    articles, API_URL,
    getArticles,
  }
}, { persist: true })
