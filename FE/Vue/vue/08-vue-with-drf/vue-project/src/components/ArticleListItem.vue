<template>
  <div>
      <h5>{{ article.id }}</h5>
      <p>{{ article.title }}</p>
      <p>{{ article.content }}</p>
      <RouterLink :to="{ name : 'DetailView' , params: {id : article.id}}"> [DETAIL]</RouterLink>
      <hr>
  </div>
</template>

<script setup>
  import { RouterLink } from 'vue-router'
  const props = defineProps({
    article: Object
  })

</script>
