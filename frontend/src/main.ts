import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { Layout, Menu, Table, Button, Select, Row, Col, Icon, Input } from 'ant-design-vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import EditableCell from '@/components/EditableCell.vue'

Vue.use(VueAxios, axios)
Vue.use(Layout)
Vue.use(Menu)
Vue.use(Table)
Vue.use(Button)
Vue.use(Select)
Vue.use(Row)
Vue.use(Col)
Vue.use(Icon)
Vue.use(Input)
Vue.component('editable-cell', EditableCell)
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
