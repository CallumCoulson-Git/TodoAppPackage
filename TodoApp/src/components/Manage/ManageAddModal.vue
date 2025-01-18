<template>
  <div v-if="showModal" class="fixed inset-0 bg-gray-800 bg-opacity-75 flex items-center justify-center">
    <div class="bg-white p-6 rounded-lg w-96">
      <h2 class="text-2xl font-bold mb-4">Add New Todo</h2>
      <form @submit.prevent="submitForm">
        <div class="mb-4">
          <label for="title" class="block text-gray-700">Title:</label>
          <input type="text" id="title" v-model="title" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" required />
        </div>
        <div class="mb-4">
          <label for="set_for" class="block text-gray-700">Set For:</label>
          <input type="datetime-local" id="set_for" v-model="set_for" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" required />
        </div>
        <div class="flex justify-end">
          <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring">Submit</button>
          <button type="button" @click="closeModal" class="ml-2 bg-gray-500 text-white px-4 py-2 rounded-lg hover:bg-gray-600 focus:outline-none focus:ring">Cancel</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showModal: false,
      title: '',
      setFor: ''
    };
  },
  methods: {
    openModal() {
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
    submitForm() {
      // Handle form submission logic here
      console.log('Title:', this.title);
      console.log('Set For:', this.setFor);
      this.closeModal();
    }
  }
};
</script>