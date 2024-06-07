import { reactive } from 'vue'
import { useRoute } from 'vue-router'

export function useQueryParams() {
  const route = useRoute()

  const queryParams = reactive<any>({
    ...route?.query
  })

  return {
    ...queryParams
  }
}
