<script setup>
import AppHeader from './components/Appheader.vue'
import { RouterView } from 'vue-router'
</script>

<template>
  <div class= "bg-gradient-to-r from-blue-900 via-purple-900 to-pink-900 min-h-screen text-white">

    <header>
      <div class="container m-auto pt-5">
        <AppHeader msg="Todo Home"/>
      </div>
    </header>

    <main class="container mx-auto mt-5">
      <RouterView />
    </main>
  </div>
</template>
