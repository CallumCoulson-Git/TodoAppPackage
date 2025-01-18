<script setup>
import ListingItem from '../ListingItem.vue'
import ManageControls from './ManageControls.vue'
import ManageShowListing from './ManageShowListing.vue'
</script>

<template>
  <ListingItem>
    <template #icon>
    </template>
    <template #heading>Manage Entries</template>

    Below You can manage the entry listings with the specified buttons
  </ListingItem>

  <ManageShowListing>
    <template #icon>
      <i class="fas fa-plus"></i>
    </template>
    <template #heading>Add Listing</template>
    <p>Click the button below to add a new listing</p>
  </ManageShowListing>

  <ManageControls>
  </ManageControls>
</template>