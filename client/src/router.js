import { createRouter, createWebHistory } from 'vue-router'
import Ping from './components/Ping.vue'
import Books from './components/Books.vue'
// import HelloWorld from './components/HelloWorld'

const routes = [  
  {
    path: '/ping',
    name: 'Ping',
    component: Ping
  },
  {
    path: '/',
    name: 'Books',
    component: Books
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes 
})

export default router
