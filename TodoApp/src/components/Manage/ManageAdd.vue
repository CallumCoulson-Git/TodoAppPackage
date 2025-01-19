<template>
  <div class="item mb-5">
    <i>
      <slot name="icon"></slot>
    </i>
    <div class="details">
      <h3 class="text-xl">
        <slot name="heading"></slot>
      </h3>
      <slot></slot>
      <button @click="addListing" class="btn btn-primary mt-3">Add Listing</button>
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