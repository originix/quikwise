import type { _RouteRecordBase } from 'vue-router'

export const enum ERoutes {
  LOGIN = '/login',
  HOME = '/',
  ABOUT = '/about'
}

type RouteRecord = Pick<_RouteRecordBase, 'name' | 'path'>

type TBaseRoutes = {
  [K in keyof typeof ERoutes]: RouteRecord
}

export const routes: TBaseRoutes = {
  LOGIN: {
    name: 'LOGIN',
    path: ERoutes.LOGIN
  },
  HOME: {
    name: 'HOME',
    path: ERoutes.HOME
  },
  ABOUT: {
    name: 'ABOUT',
    path: ERoutes.ABOUT
  }
}
