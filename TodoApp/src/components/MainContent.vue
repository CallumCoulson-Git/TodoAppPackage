<script setup>
import ListingItem from './ListingItem.vue'

const openReadmeInEditor = () => fetch('/__open-in-editor?file=README.md')
</script>

<template>
  <ListingItem>
    <template #icon>
    </template>
    <template #heading>Summary</template>

    This is a summary for ther current project, currently a todo app.
  </ListingItem>

  <ListingItem>
    <template #icon>
      
    </template>
    <template #heading>Scope</template>
    The scope of the project is to use:<br/>
    <RouterLink to="/login" target="_blank" rel="noopener">Login</RouterLink>, 
    <RouterLink to="/manage" target="_blank" rel="noopener">CRUD and forms</RouterLink>, 
    <RouterLink to="/" target="_blank" rel="noopener">Front End Simple Design</RouterLink>, 
    <RouterLink to="/database" target="_blank" rel="noopener">Database Interaction (SQLite)</RouterLink>, 
    <RouterLink to="/manage" target="_blank" rel="noopener">Dynamic Backend</RouterLink>, 
  </ListingItem>

  <ListingItem>
    <template #icon>
    </template>
    <template #heading>Resources</template>
    This project uses Vue.js, with Tailwind as the CSS framework.<br/>
    I'm using FastAPI as the backend for python, and SQLite as the database.
  </ListingItem>
</template>
