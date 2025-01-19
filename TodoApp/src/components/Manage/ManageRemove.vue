<template>
  <button @click="removeListing" class="btn btn-danger">Remove</button>
</template>

<script>
export default {
  props: {
    reserveId: {
      type: Number,
      required: true
    }
  },
  methods: {
    async removeListing() {
      try {
        const token = sessionStorage.getItem('token');
        const response = await fetch(`http://localhost:8000/reserve/${this.reserveId}`, {
          method: 'DELETE',
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });

        if (!response.ok) {
          console.log(response);
          throw new Error('Failed to remove listing');
        }

        this.$emit('remove');
      } catch (error) {
        console.error('Error:', error);
      }
    }
  }
}
</script>