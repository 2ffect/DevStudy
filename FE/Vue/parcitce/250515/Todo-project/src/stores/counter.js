import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  // 사용자가 값을 CUD 할 때 반응 할 수 있도록 반응형으로 작성
  let id = 0

  // todo 객체 만들기
  const todos = ref([
      // input:checkbox 와 v-for 의 key 로 쓰일 id 필요
      // let 으로 id 정의
      { id: id ++, text: 'vue 공부', isDone: false},
      { id: id ++, text: 'JS 공부', isDone: false},
      { id: id ++, text: 'django 공부', isDone: true},
  ])

  // Todo 추가
  const addTodo = function (todoText) {
    todos.value.push({
      id: id ++,
      isDone: false,
      text: todoText
    })
  }

  // Todo 삭제
  const deleteTodo = function (selectedId) {
    // 넘겨 받은 id 값을 기준으로 todos 전체를 순회하고, 넘겨 받은 id를 제외한 todo 들만 모아서 새로운 배열 반환
    todos.value = todos.value.filter(todo => todo.id != selectedId)

    // // 인덱스를 찾은 뒤 해당 위치에서 하나만 제거
    // const index = todos.value = todos.value.findIndex((todo) => todo.id === selectedId)
    // todos.value.splice(index, 1)
  }

  // Todo 수정
  const updateTodo = function (selectedId) {
    todos.value = todos.value.map((todo) => {
      if (todo.id === selectedId) {
        todo.isDone = !todo.isDone
      }
      return todo
    })
  }

  // 반드시 값 선언 시 리턴에 작성
  return {
    todos,
    addTodo, deleteTodo, updateTodo,

  }
} , { persist : true })
