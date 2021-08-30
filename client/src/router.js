import { createRouter, createWebHashHistory } from 'vue-router'
import Ping from './components/Ping.vue'
import HelloWorld from './components/HelloWorld'

const routes = [  
  {
    path: '/ping',
    name: 'Ping',
    component: Ping
  },
  {
    path: '/',
    name: 'HelloWorld',
    component: HelloWorld
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
