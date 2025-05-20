<template>
  <div class="card-container">
    <div class="card"
      v-for="card in businessCards"
      :key="card.name"
    >
      <h4 class="card-title"> 이름 : {{ card.name }}</h4>
      <p class="card-context">직함 : {{ card.title }}</p>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  businessCards: Object
})

</script>

<style scoped>
.card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 24px;
  margin-top: 40px;
}

.card {
  width: 300px;
  padding: 20px;
  border: 1px solid #e0e0e0;
  background-color: #fff;
  box-sizing: border-box;
  border-radius: 4px;
  text-align: center;
}

.card-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
}

.card-context {
  font-size: 16px;
  color: #444;
}

</style>