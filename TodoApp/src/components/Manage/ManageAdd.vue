<template>
  <div class="item mb-5 flex">
    <div class="details  bg-white text-gray-700 p-4 rounded-lg shadow-lg w-100">
      <i class="fas fa-plus mr-2"></i>
      <button @click="addListing" class="btn btn-primary font-bold">Add Listing</button>
    </div>
    <ManageAddModal v-show="showModal" @close="closeModal" @listing-added="listingAdded" />
  </div>
</template>

<script>
import ManageAddModal from './ManageAddModal.vue';

export default {
  components: {
    ManageAddModal
  },
  data() {
    return {
      showModal: false
    };
  },
  methods: {
    addListing() {
      console.log('Modal Open');
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
    listingAdded() {
      this.$emit('listing-added');
    }
  }
}
</script>