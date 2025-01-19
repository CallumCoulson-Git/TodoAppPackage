<script setup>
import { ref } from 'vue';
import ListingItem from '../ListingItem.vue';
import ManageAdd from './ManageAdd.vue';
import ManageShowListing from './ManageShowListing.vue';

const showListingRef = ref(null);

function fetchListing() {
  showListingRef.value.fetchListing();
}
</script>

<template>
  <ListingItem>
    <template #icon>
    </template>
    <template #heading>Manage Entries</template>

    Below You can manage the entry listings with the specified buttons
  </ListingItem>

  <ManageShowListing ref="showListingRef" @listing-added="fetchListing">
    <template #icon>
      <i class="fas fa-plus"></i>
    </template>
    <template #heading>Add Listing</template>
    <p>Click the button below to add a new listing</p>
  </ManageShowListing>
  <ManageAdd @listing-added="fetchListing"></ManageAdd>
  <ManageControls></ManageControls>
</template>