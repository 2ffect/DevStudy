<template>
  <div>
    <h1>Article page</h1>
    <ArticleList />
    <RouterLink :to="{ name: 'CreateView'}"> [CREATE] </RouterLink>
  </div>
</template>

<script setup>
  import ArticleList from '@/components/ArticleList.vue'
  import { useArticleStore } from '@/stores/articles.js'
  import { onMounted } from 'vue'
  import { RouterLink } from 'vue-router'
  const store = useArticleStore()

  onMounted(() => {
    store.getArticles()
  })
</script>

<style>

</style>
