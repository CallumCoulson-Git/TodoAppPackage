<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const errorMessage = ref('')
const isLoggedIn = ref(false)
const router = useRouter()

const handleSubmit = async () => {
  if (!email.value || !password.value) {
    errorMessage.value = 'All fields are required'
    return
  }

  try {
    const response = await fetch('http://localhost:8000/token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: new URLSearchParams({
        username: email.value,
        password: password.value,
      }),
    })
    if (!response.ok) {
      throw new Error('Login failed')
    }

    const data = await response.json()
    console.log('Login successful:', data)
    isLoggedIn.value = true
    sessionStorage.setItem('token', data.access_token)
    sessionStorage.setItem('email', JSON.stringify({ email: email.value }))
    sessionStorage.setItem('user', JSON.stringify({ id: data.user.id}))
    router.push('/manage')  // Redirect to manage page
  } catch (error) {
    console.error('Error:', error)
    errorMessage.value = 'Login failed'
  }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center">
    <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
      <h2 class="text-2xl font-bold mb-6 text-center text-black">Login</h2>
      <form @submit.prevent="handleSubmit">
        <div v-if="errorMessage" class="mb-4 text-red-500 text-center">
          {{ errorMessage }}
        </div>
        <div class="mb-4">
          <label for="email" class="block text-gray-700">Email</label>
          <input
            type="email"
            id="email"
            v-model="email"
            class="w-full text-black px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300"
            required
          />
        </div>
        <div class="mb-6">
          <label for="password" class="block text-gray-700">Password</label>
          <input
            type="password"
            id="password"
            v-model="password"
            class="w-full text-black px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300"
            required
          />
        </div>
        <button
          type="submit"
          class="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring focus:border-blue-300"
        >
          Login
        </button>
      </form>
      <p class="mt-4 text-center text-gray-700">
        Don't have an account? 
        <RouterLink to="/register" class="text-blue-500 hover:underline">Register</RouterLink>
      </p>
    </div>
  </div>
</template>