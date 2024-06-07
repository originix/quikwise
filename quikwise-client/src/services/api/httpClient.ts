import { interceptorRequest, interceptorRequestError } from './interceptors/request'
import { interceptorResponse, interceptorResponseError } from './interceptors/response'

const httpClient = axios.create({
  baseURL: env.apiUrl,
  timeout: 180000, // 3 mins
  headers: {
    'Content-Type': 'application/json',
    accept: 'application/json'
  },
  withCredentials: false // Backend set to false
})

httpClient.interceptors.request.use(interceptorRequest, interceptorRequestError)
httpClient.interceptors.response.use(interceptorResponse, interceptorResponseError)

export default httpClient
