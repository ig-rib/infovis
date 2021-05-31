import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Semana1 from '../views/homework/semana1/Semana1.vue'
import Semana3 from '../views/homework/semana3/Semana3.vue'
import Semana6 from '../views/homework/semana6/Semana6.vue'
import TPDatosPersonales from '../views/homework/tp-datos-personales/TPDatosPersonales.vue'
import OneGbOfData from '../views/homework/one-gb-of-data/OneGbOfData.vue'
import HomeworkContainer from '../views/homework/HomeworkContainer.vue'


Vue.use(VueRouter)

const deployRoute = ''

const routes = [
  {
    path: deployRoute + '/',
    name: 'Home',
    component: Home,
  },
  {
    path: deployRoute + '/homework',
    name: 'homework',
    component: HomeworkContainer,
    children: [
      {
        path: 'semana1',
        name: 'semana1',
        component: Semana1
      },
      {
        path: 'semana3',
        name: 'semana3',
        component: Semana3
      },
      {
        path: 'semana6',
        name: 'semana6',
        component: Semana6
      },
      {
        path: 'tp-datos-personales',
        name: 'tp-datos-personales',
        component: TPDatosPersonales
      },
      {
        path: 'one-gb-of-data',
        name: 'one-gb-of-data',
        component: OneGbOfData
      }
    ]
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
