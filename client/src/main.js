import App from './App.vue'
import router from './router.js'
import { createApp } from 'vue'

const app = createApp(App).use(router);
app.mount('#app');

