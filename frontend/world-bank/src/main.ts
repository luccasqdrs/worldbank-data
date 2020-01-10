import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { Layout, Menu, Table, Button } from 'ant-design-vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)
Vue.use(Layout)
Vue.use(Menu)
Vue.use(Table)
Vue.use(Button)
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
