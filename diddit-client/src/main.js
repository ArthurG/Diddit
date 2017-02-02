// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './views/App'
import Home from './views/Home'
import Signup from './views/Signup'

import VueRouter from 'vue-router'
import VueResource from 'vue-resource'

Vue.use(VueResource)
Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
  {path: '/', component: App},
  {path: '/home', component: Home},
  {path: '/signup', component: Signup}
  ]
})

/* eslint-disable no-new */
new Vue({
  router
}).$mount('#app')
