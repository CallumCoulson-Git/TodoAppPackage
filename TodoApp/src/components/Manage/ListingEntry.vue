<template>
  <div class="flex justify-between items-center mb-2">
    <div class="w-half">
      <h4 class="text-lg font-bold">{{ reserve.title }}</h4>
      <p>Set for: {{ new Date(reserve.set_for).toLocaleString() }}</p>
    </div>
    <div class="w-half">
      <ManageControls :reserveId="reserve.id" :reserve="reserve" @listing-removed="handleListingRemoved" @listing-updated="handleListingUpdated" />
    </div>
  </div>  
</template>

<script>
import ManageControls from './ManageControls.vue';

export default {
  components: {
    ManageControls
  },
  props: {
    reserve: {
      type: Object,
      required: true
    }
  },
  methods: {
    handleListingRemoved() {
      this.$emit('listing-removed');
    },
    handleListingUpdated() {
      this.$emit('listing-updated');
    }
  }
}
</script>