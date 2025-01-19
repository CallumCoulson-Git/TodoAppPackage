<template>
    <button @click="updateListing" class="btn btn-warning">Update Listing</button>
    <ManageUpdateModal v-show="showModal" :reserveId="reserveId" :initialTitle="initialTitle" :initialSetFor="initialSetFor" @close="closeModal" @listing-updated="listingUpdated" />
</template>

<script>
import ManageUpdateModal from './ManageUpdateModal.vue';

export default {
  components: {
    ManageUpdateModal
  },
  props: {
    reserveId: {
      type: Number,
      required: true
    },
    initialTitle: {
      type: String,
      required: true
    },
    initialSetFor: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      showModal: false
    };
  },
  methods: {
    updateListing() {
      console.log('Modal Open');
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
    listingUpdated() {
      this.$emit('listing-updated');
    }
  }
}
</script>