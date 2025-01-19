<script setup>
import { defineProps } from 'vue'
import { RouterLink, useRoute, useRouter } from 'vue-router'

const props = defineProps({
  msg: {
    type: String,
    required: true,
  },
})

const route = useRoute()
const router = useRouter()
const isUserLoggedIn = sessionStorage.getItem('user') !== null

const handleLogout = () => {
  sessionStorage.clear()
  router.push('/login')
}
</script>

<template>
  <header class="w-full bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 text-white p-4 rounded-lg mt-25">
    <div class="container mx-auto flex justify-between items-center">
      <div class="text-2xl font-bold">
        {{ msg }}
      </div>
      <nav class="space-x-4">
        <p>
          <strong>Current route path:</strong> {{ route.fullPath }}
        </p>
        <RouterLink to="/" class="hover:text-gray-400">Home</RouterLink>
        <RouterLink v-if="isUserLoggedIn" to="/manage" class="hover:text-gray-400">Manage</RouterLink>
        <RouterLink v-if="!isUserLoggedIn" to="/login" class="hover:text-gray-400">Login</RouterLink>
        <button v-if="isUserLoggedIn" @click="handleLogout" class="hover:text-gray-400">Logout</button>
      </nav>
    </div>
  </header>
</template>