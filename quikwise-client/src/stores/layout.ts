import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useLayoutStore = defineStore('layout', () => {
  const isOpen = ref<boolean>(false)
  const selectedMenu = ref<string[]>(['1'])

  return { isOpen, selectedMenu }
})
