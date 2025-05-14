import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import UserView from '@/views/UserView.vue'
import UserPosts from '@/components/UserPosts.vue'
import UserProfile from '@/components/UserProfile.vue'
import LoginView from '@/views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView,
    },
    {
      // vue 에서는 : 를 사용해 매개변수 표기
      path: '/user/:id',
      // name: 'user',
      component: UserView,
      children: [
        { path: '', name: 'user', component: UserProfile},
        // UserProfile 은 UserView의 <RoutereView> 내부에 렌더링
        { path: 'profile', name: 'userProfile', component: UserProfile},
        // UserPosts 는 UserView의 <RoutereView> 내부에 렌더링
        { path: 'posts', name: 'userPosts', component: UserPosts},
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      beforeEnter: (to, from) => {
        console.log(to, from)
        const isLoggined = true
        if (isLoggined) {
          return { name:'home'}
        }
      }
    },
  ],
})

// router.beforeEach((to, from) => {
//   const isLoggined = false

//   if (!isLoggined && to.name !=='login') {
//     alert('로그인 하세요')
//     return { name: 'login' }
//   }
//   // console.log(to, from)
// })

export default router
