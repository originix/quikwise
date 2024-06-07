<script setup lang="ts">
import { RouterView } from 'vue-router'
import { useLayoutStore } from '@/stores/layout'

const layoutStore = useLayoutStore()
</script>

<template>
  <div class="flex min-h-screen flex-row">
    <CSidebar />
    <ALayout>
      <ALayoutContent
        class="p-2 ml-200px transition-all transform-width"
        :class="{
          'ml-200px': !layoutStore.isOpen,
          'ml-80px': layoutStore.isOpen
        }"
      >
        <RouterView />
      </ALayoutContent>
    </ALayout>
  </div>
</template>

<style scoped>
.layout {
  @apply flex;
}
</style>
