<script setup>
import { computed } from 'vue'
import * as icons from 'lucide-vue-next'

const props = defineProps({
  name: {
    type: String,
    required: true
  },
  size: {
    type: [Number, String],
    default: 20
  },
  color: {
    type: String,
    default: 'black'
  },
  strokeWidth: Number,
  defaultClass: String
})

const icon = computed(() => icons[props.name])
const _color = computed(() => {
  return props.color
})
</script>

<template>
  <component
    :is="icon"
    :size="size"
    :color="_color"
    :stroke-width="strokeWidth"
    :default-class="defaultClass"
  />
</template>
