import { endpoint } from '@/enums'
import httpClient from '@/services/api/httpClient'
import type { ILogin } from '@/types'

export default {
  login: async ({ username, password }: ILogin) => {
    const { data, isLoading, isError, fetch } = useAxios(endpoint.AUTH.LOGIN, 'POST', {
      username,
      password
    })
    await fetch()
    return {
      data,
      isLoading,
      isError
    }
  },

  refreshTokenAPI: async (refreshToken: string): Promise<any> => {
    const data = await httpClient.post(endpoint.AUTH.REFRESH, {
      refresh_token: refreshToken
    })
    return {
      data
    }
  }
}
