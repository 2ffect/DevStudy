<template>
  <div>
    <p>이름 : {{ student.name }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const student = ref(route.params)

</script>

<style scoped>

</style>