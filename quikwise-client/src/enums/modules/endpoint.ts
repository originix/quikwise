export const enum EEndpoint {
  AUTH = '/v1/auth'
}

type TBaseEndpoint = {
  [K in keyof typeof EEndpoint]: {
    LOGIN: string
    REFRESH: string
    REGISTER: string
    VERIFY: string
  }
}

export const endpoint: TBaseEndpoint = {
  AUTH: {
    LOGIN: `${EEndpoint.AUTH}/login`,
    REFRESH: `${EEndpoint.AUTH}/refresh`,
    REGISTER: `${EEndpoint.AUTH}/register`,
    VERIFY: `${EEndpoint.AUTH}/verify`
  }
}
