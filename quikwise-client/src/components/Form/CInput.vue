<script setup lang="ts">
import {
  Input as AInput,
  InputPassword as APasswordInput,
  Textarea as ATextarea
} from 'ant-design-vue'
import type { Rule } from 'ant-design-vue/es/form'

const props = defineProps<{
  type: string
  modelValue: string
  label?: string
  name: string
  rules?: Rule[]
}>()

const emit = defineEmits(['update:modelValue'])
const modelValue = ref(props.modelValue)

const currentComponent = computed(() => {
  switch (props.type) {
    case 'password':
      return APasswordInput
    case 'textarea':
      return ATextarea
    case 'text':
    default:
      return AInput
  }
})

watch(
  () => props.modelValue,
  (newVal) => {
    modelValue.value = newVal
  }
)

const updateValue = (event: Event) => {
  const input = event.target as HTMLInputElement
  emit('update:modelValue', input.value)
}
</script>

<template>
  <AFormItem :label="label" :name="name" :rules="rules">
    <component
      :is="currentComponent"
      size="large"
      v-bind="$attrs"
      :value="modelValue"
      @input="updateValue"
    />
    <slot />
  </AFormItem>
</template>
