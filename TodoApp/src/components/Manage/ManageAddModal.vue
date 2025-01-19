<template>
  <div class="fixed inset-0 bg-gray-800 bg-opacity-75 flex items-center justify-center">
    <div class="bg-white p-6 rounded-lg w-96">
      <h2 class="text-2xl font-bold mb-4 text-gray-700">Add New Todo</h2>
      <form @submit.prevent="submitForm">
        <div class="mb-4">
          <label for="title" class="block text-gray-700">Title:</label>
          <input type="text" id="title" v-model="title" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" required />
        </div>
        <div class="mb-4">
          <label for="setFor" class="block text-gray-700">Set For:</label>
          <DatePicker v-model="setFor" dateFormat="dd/mm/yy" showTime hourFormat="24" />
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
import { ref } from 'vue';

const setFor = ref();

export default {
  data() {
    return {
      title: '',
      setFor: ''
    };
  },
  methods: {
    closeModal() {
      this.$emit('close');
    },
    async submitForm() {
      try {
        const user = JSON.parse(sessionStorage.getItem('user'));
        const token = sessionStorage.getItem('token');
        const response = await fetch(`http://localhost:8000/reserve/?user_id=${user.id}`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
          },
          body: JSON.stringify({
            title: this.title,
            set_for: this.setFor
          })
        });

        if (!response.ok) {
          console.log(response);
          throw new Error('Failed to add listing');
        }

        const data = await response.json();
        console.log('Listing added:', data);
        this.$emit('listing-added');
        this.closeModal();
      } catch (error) {
        console.error('Error:', error);
      }
    }
  }
};
</script>
