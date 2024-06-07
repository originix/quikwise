import { createRouter, createWebHistory } from 'vue-router'
import { routes } from '@/enums/modules/routes'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: () => import('../components/Layouts/DefaultLayout.vue'),
      children: [
        {
          ...routes.HOME,
          component: () => import('../views/HomeView.vue')
        },
        {
          ...routes.ABOUT,
          component: () => import('../views/AboutView.vue')
        }
      ]
    },
    {
      ...routes.LOGIN,
      component: () => import('../views/LoginView.vue')
    }
  ]
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')

  if (to.path === routes.LOGIN.path && token) {
    next(routes.HOME.path)
  } else if (to.path !== routes.LOGIN.path && !token) {
    next(routes.LOGIN.path)
  } else {
    console.log('11')
    next()
  }
})

export default router
