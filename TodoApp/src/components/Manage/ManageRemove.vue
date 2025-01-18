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
      <button @click="removeListing" class="btn btn-danger mt-3">Remove Listing</button>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    removeListing() {
      // Logic to remove a listing
      console.log('Listing removed');
    }
  }
}
</script>