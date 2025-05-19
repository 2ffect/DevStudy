<template>
  <div>
    <h3>Article List</h3>
    <p>ㅇㅅㅇ ㅅㄹㅎ</p>
    <ArticleListItem 
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
  import ArticleListItem from '@/components/ArticleListItem.vue'
  import { useArticleStore } from '@/stores/articles.js'
  const store = useArticleStore()
</script>

