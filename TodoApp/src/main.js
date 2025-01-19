import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './input.css'
import './output.css'
import PrimeVue from 'primevue/config';
import Aura from '@primevue/themes/aura';
import DatePicker from 'primevue/datepicker';

const app = createApp(App);
app.use(router)
app.use(PrimeVue, {
  theme: {
      preset: Aura,
      options: {
          prefix: 'p',
          darkModeSelector: 'system',
          cssLayer: false
      }
  }
});
app.component('DatePicker', DatePicker);

app.mount('#app');