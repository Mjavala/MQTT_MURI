import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/homePage.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/muri/historical',
    name: 'historical',
    // --- Async components - https://vuejs.org/v2/guide/components-dynamic-async.html --- //
    component: () => import('../components/historicalPage.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
