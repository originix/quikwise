<script setup lang="ts">
const isLoading = ref<boolean>(true)

onMounted(() => {
  setTimeout(() => {
    isLoading.value = false
  }, 3000)
})
</script>

<template>
  <div class="card">
    <CCardWhiteBoard :isLoading v-for="(item, index) in 5" :key="index" :title="`test-${index}`" />
  </div>
</template>

<style scoped lang="scss">
.card {
  @apply auto-cols-max gap-4 grid 2xl:grid-cols-6 xl:grid-cols-5 lg:grid-cols-3 md:grid-cols-2 grid-cols-1;
  .body {
    @apply col-auto;
  }
  ::v-deep(.img) {
    @apply h-40 xs:h-24;
  }
}
</style>
