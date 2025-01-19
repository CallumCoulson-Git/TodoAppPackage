<template>
  <div class="item mb-5 w-full">
    <div class="details">
      <h3 class="text-xl">
        Listings
      </h3>
      <ul>
        <li v-for="reserve in reserves" :key="reserve.id" class="mb-2">
          <h4 class="text-lg font-bold">{{ reserve.title }}</h4>
          <p>Set for: {{ new Date(reserve.set_for).toLocaleString() }}</p>
        </li>
      </ul>
    </div>
    <ManageControls />
  </div>
</template>

<script>
import ManageControls from './ManageControls.vue'

export default {
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