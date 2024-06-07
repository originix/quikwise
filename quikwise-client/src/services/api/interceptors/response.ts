import { HTTP_STATUS_CODE } from '@/enums'
import { auth } from '@/services/api'

// Flags related to refreshToken

const win: Window = window

interface IRefreshFlags {
  isRefreshingToken: boolean
  refreshTokenPromise: Promise<any> | null
}

const refreshFlags: IRefreshFlags = {
  isRefreshingToken: false,
  refreshTokenPromise: null
}

// Logout
const logout = () => (win.location = '/logout')

const refreshToken = async () => {
  if (refreshFlags.isRefreshingToken) {
    return refreshFlags.refreshTokenPromise
  }

  refreshFlags.refreshTokenPromise = (async () => {
    const refreshTokenLocalStorage = localStorage.getItem('refreshToken')
    if (!refreshTokenLocalStorage) {
      throw new Error('missing refresh token')
    }
    const { data } = await auth.refreshTokenAPI(refreshTokenLocalStorage)
    localStorage.setItem('refreshToken', data?.data?.refresh_token ?? '')
    localStorage.setItem('token', data?.data?.access_token ?? '')
  })()

  // Real refresh token process
  try {
    refreshFlags.isRefreshingToken = true
    await refreshFlags.refreshTokenPromise
  } catch (error) {
    logout()
  } finally {
    // eslint-disable-next-line
    refreshFlags.isRefreshingToken = false
  }

  return null
}

export const interceptorResponse = (response: any) => {
  return response
}

export const interceptorResponseError = async (error: any) => {
  const {
    response: { status: statusCode }
  } = error
  const xReqRetry = error.config.headers['x-req-retry']
  let $error = null

  switch (statusCode) {
    case HTTP_STATUS_CODE.BAD_REQUEST:
      $error = {
        title: 'There was a problem with your request.',
        message: 'Please try again.'
      }
      break
    // case HTTP_STATUS_CODE.UNAUTHORIZED:
    //   if (xReqRetry >= 1 || refreshFlags.isRefreshingToken) {
    //     // If retry more than threshold, stop refreshToken and log user out
    //     // or if got 401 when refresh token, log user out
    //     // since this request is failed because of another reason
    //     // logout()
    //   } else {
    //     // Try refreshing token
    //     await refreshToken()
    //     // Count how many times this request try to call the same fetch again
    //     // eslint-disable-next-line
    //     error.config.headers['x-req-retry'] = xReqRetry ? xReqRetry + 1 : 1
    //     // And call the same fetch again
    //     return httpClient.request(error.config)
    //   }
    //
    //   break

    case HTTP_STATUS_CODE.FORBIDDEN:
      win.location = '/forbidden'
      break

    case HTTP_STATUS_CODE.NOT_FOUND:
      // redirect to 404 page
      setTimeout(() => {
        win.location = '/404'
      }, 300)

      break
    case HTTP_STATUS_CODE.INTERNAL_SERVER_ERROR:
      $error = {
        title: 'There was an unexpected error.',
        message: 'Please try again.'
      }
      break
    case HTTP_STATUS_CODE.BAD_GATEWAY:
      // redirect to 502 page
      // window.location = "/502";
      break
    default:
  }

  if ($error) {
    // TODO: Dispatch erorr to store
  }

  return Promise.reject(error)
}
