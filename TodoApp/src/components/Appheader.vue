<script setup>
import { defineProps } from 'vue'
import { RouterLink, useRoute } from 'vue-router'

const props = defineProps({
  msg: {
    type: String,
    required: true,
  },
})

const route = useRoute()
const isUserLoggedIn = sessionStorage.getItem('user') !== null
console.log(isUserLoggedIn)
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
        <RouterLink v-if="isUserLoggedIn" to="/listings" class="hover:text-gray-400">Listings</RouterLink>
        <RouterLink to="/" class="hover:text-gray-400">Home</RouterLink>
        <RouterLink to="/manage" class="hover:text-gray-400">Manage</RouterLink>
        <RouterLink to="/login" class="hover:text-gray-400">Login</RouterLink>
        
      </nav>
    </div>
  </header>
</template>