import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './input.css'
import './output.css'

createApp(App)
  .use(router)
  .component('VueDatePicker', VueDatePicker)
  .mount('#app')
  