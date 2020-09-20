import Vue from 'vue'
import RegisterPage from './RegisterPage.vue'

import BootstrapVue from 'bootstrap-vue'
Vue.use(BootstrapVue)

import axios from 'axios'
Vue.prototype.$http = axios
Vue.prototype.$api_url = 'http://localhost:5000'


import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)

Vue.config.productionTip = false

new Vue({
    render: h => h(RegisterPage),
  }).$mount('#app')
  