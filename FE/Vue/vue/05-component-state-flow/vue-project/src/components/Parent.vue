<template>
  <h1>Parent</h1>
  <p>{{ userName }}</p>
  <Child 
    :user-name="userName"
    parent-name="Bella"
    @change-user-name="$emit('changeUserName')"
  />
</template>

<script setup>
  import Child from './Child.vue';
  
  const props = defineProps({
    userName: String
  })

  // console.log(props)
  // console.log(props.userName)
</script>

<style scoped>

</style>