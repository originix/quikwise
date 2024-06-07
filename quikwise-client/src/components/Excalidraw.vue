<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import { Excalidraw } from '@excalidraw/excalidraw'
import { createElement, ReactElement } from 'react'
import { createRoot } from 'react-dom/client'

const excalidrawWrapper = ref<HTMLDivElement | null>(null)
const stateExcalidraw = reactive({
  appState: {},
  elements: [],
  files: {}
})
const readOnly = ref(false)
let excalidrawAPI = null

const setExcalidrawAPI = (api: any) => {
  excalidrawAPI = api
}

const onChange = (elements: any[], appState: any, files: any) => {
  // console.log(elements)
  stateExcalidraw.elements = elements
  stateExcalidraw.appState = appState
  stateExcalidraw.files = files
}

onMounted(() => {
  if (excalidrawWrapper.value) {
    const ExcalidrawComponent = Excalidraw.default || Excalidraw

    const root = createRoot(excalidrawWrapper.value)

    root.render(
      createElement(ExcalidrawComponent, {
        initialData: {
          appState: { ...stateExcalidraw.appState },
          elements: stateExcalidraw.elements,
          files: stateExcalidraw.files || undefined
        },
        excalidrawAPI: (api: any) => setExcalidrawAPI(api),
        onChange: (elements: any[], appState: any, files: any) =>
          onChange(elements, appState, files),
        viewModeEnabled: readOnly.value
      }) as ReactElement
    )
  }
})
</script>

<template>
  <div class="excalidraw-wrapper" ref="excalidrawWrapper"></div>
</template>

<style scoped>
.excalidraw-wrapper {
  height: 100vh;
  width: 100%;
}
</style>
