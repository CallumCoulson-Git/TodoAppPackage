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
  </div>
</template>

<script>
export default {
  methods: {
    addListing() {
      // Logic to add a listing
      console.log('Listing added');
    }
  }
}
</script>