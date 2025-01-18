<template>
  <div v-if="showModal" class="modal-overlay">
    <div class="modal-container">
      <h2>Add New Todo</h2>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="title">Title:</label>
          <input type="text" id="title" v-model="title" required />
        </div>
        <div class="form-group">
          <label for="set_for">Set For:</label>
          <input type="datetime-local" id="set_for" v-model="setFor" required />
        </div>
        <button type="submit">Submit</button>
        <button type="button" @click="closeModal">Cancel</button>
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

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-container {
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 300px;
}

.form-group {
  margin-bottom: 15px;
}

button {
  margin-right: 10px;
}
</style>