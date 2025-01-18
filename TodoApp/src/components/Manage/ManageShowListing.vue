<template>
  <div class="item mb-5 w-full">
    <i>
      <slot name="icon"></slot>
    </i>
    <div class="details">
      <h3 class="text-xl">
        {{ listing.heading }}
      </h3>
      <p>{{ listing.description }}</p>
      <button @click="addListing" class="btn btn-primary mt-3">Add Listing</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      listing: {}
    };
  },
  methods: {
    fetchListing() {
      const user = JSON.parse(sessionStorage.getItem('user'));
      
      fetch(`http://localhost:8000/user/${user.id}/reserves/`)
        .then(response => response.json())
        .then(data => {
          this.listing = data;
        })
        .catch(error => {
          console.error('Error fetching listing:', error);
        });
    },
    addListing() {
      // Logic to add a listing
      console.log(this.listing);
    }
  },
  mounted() {
    this.fetchListing();
  }
}
</script>