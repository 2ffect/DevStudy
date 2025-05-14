import { createRouter, createWebHistory, useRoute } from 'vue-router'
import { ref } from 'vue'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import UserView from '@/views/UserView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/user/:username',
      name: 'user',
      component: UserView,
      beforeEnter: (to, from) => {
        console.log(to, from)
        console.log(to.params.username)
        if (to.params.username === 'admin') {
          return true
        } else {
          alert('admin 아님')
          return { name : 'home' }
        }
      }
    }
  ]
})

export default router
