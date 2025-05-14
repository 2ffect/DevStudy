<template>
  <div>
    <h1>학생 상세 정보 목록입니다.</h1>
    <div  v-for="student in students" :key="student.name">
      <p @click="goDetail(student)"> {{ student.name }} 학생 정보 보기 </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import route from '../router'

const students = ref([
  {name: '김하나'},
  {name: '김두리'},
  {name: '김서이'},
])

const goDetail = function (student) {
  route.push({ name: 'detail', params: { name: student.name } })
}

</script>

<style scoped>

</style>