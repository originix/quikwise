import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'
import VueDevTools from 'vite-plugin-vue-devtools'
import Components from 'unplugin-vue-components/vite'
import { AntDesignVueResolver } from 'unplugin-vue-components/resolvers'
import unocss from 'unocss/vite'
import theme from './src/configs/theme'
import { presetAttributify, presetUno, transformerDirectives } from 'unocss'
import AutoImport from 'unplugin-auto-import/dist/vite'

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    host: true,
    port: Number(process.env.VITE_PORT) || 5173
  },
  plugins: [
    vue(),
    vueJsx(),
    VueDevTools(),
    Components({
      dirs: ['src/components'],
      resolvers: [
        AntDesignVueResolver({
          importStyle: false // css in js
        })
      ]
    }),
    AutoImport({
      include: [
        /\.[tj]sx?$/, // .ts, .tsx, .js, .jsx
        /\.vue$/,
        /\.vue\?vue/, // .vue
        /\.md$/ // .md
      ],

      dirs: ['src/composables/**', 'src/stores/**', 'src/utils/**'],

      eslintrc: {
        enabled: true // <-- this
      },
      // global imports to register
      imports: [
        // presets
        'vue',
        'vue-router',
        {
          axios: [
            ['default', 'axios'] // import { default as axios } from 'axios',
          ]
        }
      ],
      dts: true
    }),
    unocss({
      transformers: [transformerDirectives()],
      content: {
        filesystem: ['**/*.{html,js,ts,jsx,tsx,vue,svelte,astro}']
      },
      presets: [presetUno(), presetAttributify()],
      theme: {
        colors: { ...theme.colors }
      },
      rules: []
    })
  ],
  define: {
    'process.env': {
      IS_PREACT: false
    }
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  css: {
    preprocessorOptions: {
      less: {
        modifyVars: {
          'primary-color': theme.colors.primary
        },
        javascriptEnabled: true
      }
    }
  }
})
