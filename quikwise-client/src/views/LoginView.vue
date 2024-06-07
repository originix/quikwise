<script setup lang="ts">
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import type { ILogin } from '@/types'
import { routes } from '@/enums/modules/routes'

const authStore = useAuthStore()
const formRef = ref()
const router = useRouter()

const form = ref<ILogin>({
  username: '',
  password: ''
})

const error = ref<string | null>('')

const handleSubmit = async () => {
  const data = await authStore.login(form.value)
  if (data) {
    error.value = data?.[0]?.desc?.[0]
    return
  }
  router.push({ name: routes.HOME.name }).then(() => {})
}
</script>

<template>
  <div
    class="login-container flex justify-center items-center min-h-screen bg-gradient-to-r from-blue-400 to-purple-600 font-sans"
  >
    <div class="login-card">
      <div class="form-section">
        <img src="@/assets/text-logo.webp" class="w-50" />
        <h1 class="text-3xl mb-8 font-bold">Log In</h1>
        <AForm ref="formRef" @finish="handleSubmit" class="space-y-4" :model="form">
          <CInput
            v-model="form.username"
            placeholder="Username"
            type="text"
            name="username"
            :rules="[{ required: true, message: 'Please input your username!', trigger: 'change' }]"
          />
          <CInput
            v-model="form.password"
            placeholder="Password"
            type="password"
            name="password"
            :rules="[{ required: true, message: 'Please input your password!', trigger: 'change' }]"
          >
            <a class="float-right text-gray-500">Forgot Password?</a>
          </CInput>
          <CButton
            type="primary"
            htmlType="submit"
            class="w-full bg-primary hover:bg-primary-dark"
            :loading="authStore.isLoading"
            >Login
          </CButton>
          <a-alert :show-icon="false" type="error" :message="error" banner v-if="error" />
        </AForm>
        <div class="text-center my-4 text-gray-500">or continue with</div>
        <div class="social-buttons flex justify-center space-x-4">
          <CButton shape="circle" class="bg-white">
            <CDynamicIcon name="Facebook" />
          </CButton>
          <CButton shape="circle" class="bg-white">
            <CDynamicIcon name="Github" />
          </CButton>
          <CButton shape="circle" class="bg-white">
            <CDynamicIcon name="Google" />
          </CButton>
        </div>
        <div class="text-center mt-4 text-gray-500">
          Don't have an account yet? <a class="text-primary">Sign up for free</a>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.login-container {
  @apply bg-gradient-to-r from-cyan-500 to-blue-500;
}

.login-card {
  @apply w-full bg-white p-8 rounded-lg shadow-lg flex max-w-400px;

  .form-section {
    @apply w-full mx-auto flex items-center flex-col;
  }
}

@media (max-width: 768px) {
  .login-card {
    @apply flex-col;
  }

  .image-section {
    @apply mb-4;
    order: -1;
  }
}
</style>
