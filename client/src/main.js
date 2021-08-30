// eslint-disable-next-line no-unused-vars
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'

import App from './App.vue'
import router from './router.js'
import { createApp } from 'vue'



const app = createApp(App).use(router)
app.mount('#app');

