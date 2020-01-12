import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { Layout, Menu, Table, Button, Select, Row, Col, Icon, Input } from 'ant-design-vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import EditableCell from '@/components/EditableCell.vue'
import TableYearFilter from '@/components/TableYearFilter.vue'
import TableCountryFilter from '@/components/TableCountryFilter.vue'
import TableCompareButton from '@/components/TableCompareButton.vue'

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
Vue.component('country-filter', TableCountryFilter)
Vue.component('year-filter', TableYearFilter)
Vue.component('compare-button', TableCompareButton)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
