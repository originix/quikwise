<script setup lang="ts">
import { ref } from 'vue'
import { useLayoutStore } from '@/stores/layout'

const layoutStore = useLayoutStore()
const authStore = useAuthStore()

const selectedKeys = ref<string[]>(layoutStore.selectedMenu)
const menus = [
  {
    title: 'Whiteboard',
    icon: 'Presentation',
    sub: []
  },
  {
    title: 'Users',
    icon: 'User',
    sub: ['tom', 'jerry'],
    class: 'flex-1'
  }
]
const menusEnd = [
  {
    title: 'Settings',
    icon: 'Settings',
    sub: ['Profile', 'Logout'],
    class: 'shrink mb-12'
  }
]

function actionSettings(d) {
  if (d === 'Logout') {
    authStore.logout()
  }
}
</script>

<template>
  <ALayout has-sider class="sidebar-layout">
    <ALayoutSider class="sidebar-layout-sider" v-model:collapsed="layoutStore.isOpen" collapsible>
      <img
        src="@/assets/text-logo.webp"
        class="logo"
        :class="{ 'w-10 object-contain': layoutStore.isOpen }"
      />
      <AMenu
        v-model:selectedKeys="selectedKeys"
        mode="inline"
        class="flex flex-col h-[calc(100vh-4rem)]"
      >
        <!-- <div class="flex-1"> -->
        <template v-for="(item, index) of menus">
          <AMenuItem v-if="!item.sub.length" :key="(index + 1).toString()" :class="item.class">
            <CDynamicIcon :name="item.icon" />
            <span class="nav-text">{{ item.title }}</span>
          </AMenuItem>
          <ASubMenu v-else :key="(index + 1).toString()" :class="item.class">
            <template #title>
              <CDynamicIcon :name="item.icon" />
              <span class="nav-text">{{ item.title }}</span>
            </template>
            <AMenuItem v-for="(sub, iSub) of item.sub" :key="`sub-${index + iSub}`">
              {{ sub }}
            </AMenuItem>
          </ASubMenu>
        </template>
        <!-- </div> -->

        <!-- <div class="items-end m-b-50px shrink"> -->
        <ASubMenu
          v-for="(item, index) of menusEnd"
          :key="(index + 1 + menus.length).toString()"
          :class="item.class"
        >
          <template #title>
            <CDynamicIcon :name="item.icon" />
            <span class="nav-text">{{ item.title }}</span>
          </template>
          <AMenuItem
            v-for="(sub, iSub) of item.sub"
            :key="`sub-${index + iSub}`"
            @click="actionSettings(sub)"
          >
            {{ sub }}
          </AMenuItem>
        </ASubMenu>
        <!-- </div> -->
      </AMenu>
    </ALayoutSider>
  </ALayout>
</template>

<style scoped lang="scss">
.sidebar-layout {
  @apply w-0;
  display: contents;
  &-sider {
    @apply overflow-auto h-screen fixed left-0 top-0 bottom-0 bg-white;
  }

  ::v-deep(.ant-menu-item) {
    @apply flex items-center w-full;
  }

  ::v-deep(.ant-menu-submenu-title) {
    @apply flex items-center w-full;
  }

  ::v-deep(.ant-menu-inline-collapsed) {
    .nav-text {
      @apply hidden;
    }
  }
}

::v-deep(.ant-layout-sider-trigger) {
  @apply bg-white text-dark;
}

::v-deep(.ant-menu-title-content) {
  @apply flex items-center gap-2;
}

.logo {
  @apply h-32px m-4 mx-auto block;
}
</style>
