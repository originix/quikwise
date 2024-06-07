import type { AxiosRequestConfig } from 'axios'

export const interceptorRequest = (request: AxiosRequestConfig) => {
  const token = localStorage.getItem('token')
  if (token) {
    request.headers!.Authorization = `Bearer ${token}`
  }
  return request
}

export const interceptorRequestError = (error: any) => {
  return Promise.reject(error)
}
