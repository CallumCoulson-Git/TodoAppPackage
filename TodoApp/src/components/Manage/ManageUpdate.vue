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
      <button @click="updateListing" class="btn btn-warning mt-3">Update Listing</button>
    </div>
    <ManageUpdateModal v-show="showModal" :reserveId="reserveId" :initialTitle="initialTitle" :initialSetFor="initialSetFor" @close="closeModal" @listing-updated="listingUpdated" />
  </div>
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