<script setup lang="ts">
const props = defineProps({
  isLoading: Boolean,
  image: {
    type: String,
    default: 'https://gw.alipayobjects.com/zos/rmsportal/JiqGstEfoWAOHiTxclqi.png'
  },
  title: {
    type: String,
    default: ''
  }
})
</script>

<template>
  <aSkeletonButton class="skeleton" active v-if="isLoading" shape="rounded" size="large" />
  <a-card hoverable v-else class="body">
    <template #cover>
      <img class="img" :src="image" />
    </template>
    <a-card-meta :title="title">
      <slot />
    </a-card-meta>
  </a-card>
</template>

<style scoped lang="scss">
.skeleton {
  ::v-deep(.ant-skeleton-button) {
    @apply min-w-60 h-162px w-full;
  }
}
.body {
  @apply min-w-60;
}
.img {
  @apply h-24 w-full object-cover;
}
</style>
