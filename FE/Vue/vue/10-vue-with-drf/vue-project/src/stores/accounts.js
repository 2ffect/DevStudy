// store/accounts.js

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useAccountStore = defineStore('account', () => {
  const token = ref('')
  const ACCOUNT_API_URL = 'http://127.0.0.1:8000/accounts'
  const isLogin = computed(() =>{
    return token.value ? true : false
  })

  const createUser = function ({username, age, password1, password2}) {
    axios ({
      method : 'post',
      url : `${ACCOUNT_API_URL}/signup/`,
      data : {
        // ...payload
        username : username,
        age : age,
        password1 : password1,
        password2 : password2,
      }
    })
      .then (res => {
        console.log('가입 완료')
      })
      .catch(err => console.log(err))
  }

    const logIn = function ({username, password}) {
    axios ({
      method : 'post',
      url : `${ACCOUNT_API_URL}/login/`,
      data : {
        // ...payload
        username : username,
        password : password,
      }
    })
      .then (res => {
        token.value = res.data.key
      })
      .catch(err => console.log(err))
  }


  return {
    ACCOUNT_API_URL,
    token, isLogin,
    createUser,
    logIn,
  }
}, { persist: true })
