<template>
  <div class="flex justify-between items-center rounded-lg p-5">
    <div class="flex items-center">
      <i class="fas fa-edit mr-2"></i>
      <ManageUpdate class="item"></ManageUpdate>
    </div>
    <div class="flex items-center">
      <i class="fas fa-trash mr-2"></i>
      <ManageRemove class="item"></ManageRemove>
    </div>
  </div>
</template>

<script>
import ManageRemove from './ManageRemove.vue';
import ManageUpdate from './ManageUpdate.vue';

export default {
  components: {
    ManageRemove,
    ManageUpdate,
  }
}
</script>

<style>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');
</style>