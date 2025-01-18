<script setup>
defineProps({
  msg: {
    type: String,
    required: true,
  },
})
</script>

<template>
  <div class="p-6 max-w-sm mx-auto bg-black rounded-xl shadow-lg flex items-center gap-x-4">
    <h1 class="flex flex-row size-48 bg-center bg-fuchsia-900">{{ msg }}</h1>

  </div>
</template>