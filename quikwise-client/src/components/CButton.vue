<script setup lang="ts">
import { useAttrs, useSlots } from 'vue'
import { Button } from 'ant-design-vue'

const props = useAttrs()
const listeners = useSlots()
</script>

<template>
  <Button v-on="listeners" v-bind="$attrs">
    <slot />
  </Button>
</template>

<style scoped></style>
