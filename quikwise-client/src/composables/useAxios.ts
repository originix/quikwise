import httpClient from '@/services/api/httpClient'
import axios, { AxiosError, type AxiosRequestConfig, type CancelTokenSource } from 'axios'
import { reactive, toRefs } from 'vue'

interface IAxiosState {
  data: any
  isLoading: boolean
  isError: any
}

const state = reactive<IAxiosState>({
  data: null,
  isLoading: false,
  isError: false
})

const request = async (url: string, config?: AxiosRequestConfig) => {
  let result
  state.isLoading = true
  try {
    result = await httpClient(url, config)
    state.data = result.data
    state.isError = false
    state.isLoading = false
  } catch (error) {
    const err = error as AxiosError
    state.data = { errors: err?.response?.data?.errors, status: err?.response?.status }
    state.isError = true
    state.isLoading = false
  }
}

export function useAxios(url: string, method: string, data?: any, config?: any, params?: any) {
  const queryParams = useQueryParams()
  const cancelToken: CancelTokenSource = axios.CancelToken.source()
  const cancel = (message?: string) => {
    cancelToken.cancel(message)
    state.isLoading = false
  }

  const axiosConfig: AxiosRequestConfig = {
    ...{ ...config, method, data, params: params || queryParams },
    cancelToken: cancelToken.token
  }
  const fetch = async () => await request(url, axiosConfig)

  return {
    ...toRefs(state),
    fetch,
    cancel
  }
}
