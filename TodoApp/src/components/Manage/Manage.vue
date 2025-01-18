<script setup>
import ListingItem from './ListingItem.vue'
import { ref } from 'vue'
import ManageAdd from './ManageAdd.vue';
import ManageRemove from './ManageRemove.vue';
import ManageUpdate from './ManageUpdate.vue';
import ManageShowListing from './ManageShowListing.vue';

const openReadmeInEditor = () => fetch('/__open-in-editor?file=README.md')
</script>

<template>
  <ListingItem>
    <template #icon>
    </template>
    <template #heading>Manage Entries</template>

    Below You can manage the entry listings with the specified buttons
  </ListingItem>


</template>

<ManageShowListing>
  <template #icon>
    <i class="fas fa-eye"></i>
  </template>
  <template #heading>Show Listing</template>
  <p>Click the button below to show the listing</p>
</ManageShowListing>
