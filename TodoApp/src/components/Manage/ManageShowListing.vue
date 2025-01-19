<template>
  <div class="item mb-5 w-full">
    <div class="details">
      <h3 class="text-xl">
        Listings
      </h3>
      <ul>
        <li v-for="reserve in reserves" :key="reserve.id" class="mb-2">
          <ListingEntry :reserve="reserve" @listing-removed="fetchListing" @listing-updated="fetchListing"/>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import ListingEntry from './ListingEntry.vue';

export default {
  components: {
    ListingEntry
  },
  data() {
    return {
      reserves: []
    };
  },
  methods: {
    fetchListing() {
      const user = JSON.parse(sessionStorage.getItem('user'));
      const token = sessionStorage.getItem('token');
      
      fetch(`http://localhost:8000/user/${user.id}/reserves/`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
        .then(response => response.json())
        .then(data => {
          this.reserves = data;
          console.log('Listing fetched:', data);
        })
        .catch(error => {
          console.error('Error fetching listing:', error);
        });
    },
  },
  mounted() {
    this.fetchListing();
  }
}
</script>