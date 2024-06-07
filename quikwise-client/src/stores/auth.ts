import { defineStore } from 'pinia'
import { auth } from '@/services/api'
import type { ILogin } from '@/types'
import { ref } from 'vue'
import { routes } from '@/enums/modules/routes'
import router from '@/router'

export const useAuthStore = defineStore('auth', () => {
  const isLoading = ref<boolean>(false)

  async function login({ username, password }: ILogin) {
    isLoading.value = true
    const { data, isError } = await auth.login({ username, password })
    if (!isError.value) {
      console.log(data?.value?.data?.access_token)
      localStorage.setItem('token', data?.value?.data?.access_token)
      localStorage.setItem('refreshToken', data?.value?.data?.refresh_token)
      isLoading.value = false
      return
    }
    isLoading.value = false
    return data?.value?.errors
  }

  function logout() {
    localStorage.clear()
    router.push({ name: routes.LOGIN.name })
  }

  return { login, isLoading, logout }
})
