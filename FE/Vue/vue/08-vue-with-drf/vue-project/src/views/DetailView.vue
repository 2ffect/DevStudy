<template>
  <div v-if="article">
    <h5>{{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <p>{{ article.created_at }}</p>
    <p>{{ article.content }}</p>
  </div>
</template>

<script setup>
  // 준비물
  // 1. axios
  import axios  from 'axios'
  // 2. 게시글 상세 조회 요청 경로 : 출처 = 스토어에 있음
  import { useArticleStore } from '@/stores/articles.js'
  // 3. 조회하고자 하는 게시글 id
  import { useRoute } from 'vue-router'
  // 4. 응답 받은 게시글을 저장할 위치
  import { ref, onMounted } from 'vue'

  const article = ref(null)
  const store = useArticleStore()
  const route = useRoute()

  // params id 기준으로 게시글 상세 조회 요청 
  const getArticle = function () {
    axios ({
      method : 'GET',
      url : `${store.API_URL}/api/v1/articles/${route.params.id}/`
    })
      .then(res =>{
        // console.log(res)
        // console.log(res.data)
        article.value = res.data
      })
      .catch(err => console.log(err))
  }

  onMounted(() => {
    getArticle()
  })
</script>

<style>

</style>
