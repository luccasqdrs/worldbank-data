<template>
  <div>
    <a-row>
      <a-col :span="8">
        <compare-button
          :selectedKeys="selectedKeys"
        >
        </compare-button>
      </a-col>
      <a-col :offset="4" :span="12">
        <a-row>
          <a-col :span="6">
            <year-filter
              :defaultYear="selectedYear"
              :handleChange="filterYear"
            >
            </year-filter>
          </a-col>
          <a-col :span="18">
            <country-filter
              :defaultCountries="selectedCountries"
              :handleChange="filterCountries"
            >
            </country-filter>
          </a-col>
        </a-row>
      </a-col>
    </a-row>

    <a-table
      :columns="columnsData"
      :dataSource="data"
      :rowSelection="{selectedRowKeys: selectedKeys, onChange: onSelectChange}"
      :pagination="true"
    >
     <template  v-for="col in editableColumns" :slot="col" slot-scope="text, record">
       <div :key="col">
        <editable-cell :text="text" @change="onCellChange(record.key,col, $event)" />
       </div>
      </template>
    </a-table>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator'
import { AxiosResponse } from 'axios'
import TableCountryFilter from './TableCountryFilter.vue'
import TableYearFilter from './TableYearFilter.vue'
import TableCompareButton from './TableCompareButton.vue'

@Component
export default class Table extends Vue {
  selectedKeys: Array<number> = [];
  selectedYear:number = 2018;
  selectedCountries:Array<string> = ['CHN', 'IND', 'MEX', 'NGA', 'USA'];
  loading: Boolean = false;
  editableColumns = []
  columnsData = [
    {
      title: 'Country Code',
      dataIndex: 'country',
      sorter: (a, b) => a.country.toUpperCase() < b.country.toUpperCase()
    },
    {
      title: 'Country Name',
      dataIndex: 'country_name',
      sorter: (a, b) =>
        a.country_name.toUpperCase() < b.country_name.toUpperCase()
    }
  ];
  data = [];

  private mounted () {
    this.$http
      .get('/indicators/')
      .then((response: AxiosResponse) => {
        let res = response.data.map((indicator: any) => {
          let indCode = indicator.code.split('.').join('_')
          return {
            title: indicator.name,
            dataIndex: indCode,
            note: indicator.note,
            sorter: (a, b) => a[indCode] - b[indCode],
            scopedSlots: { customRender: indCode }
          }
        })
        this.columnsData.push(...res)
        this.editableColumns = res.map(ind => ind.dataIndex)
      })
    this.getData()
  }

  getData () {
    this.loading = true
    this.$http
      .get(
        `/display_data/?countries=${this.selectedCountries.join()}&years=${this.selectedYear}`
      )
      .then((response: AxiosResponse) => {
        let data = response.data
        data.forEach((row: any) => {
          row.key = row.id
        })
        this.data = data
        this.loading = false
      })
  }

  filterYear (value:number) {
    this.selectedYear = value
    this.getData()
  }

  filterCountries (value:Array<string>) {
    this.selectedCountries = value
    this.getData()
  }

  onSelectChange (selectedRowKeys: any) {
    this.selectedKeys = selectedRowKeys
  }

  onCellChange (key:number, column:string, value:number) {
    let payload:any = {}
    payload['id'] = key
    payload[column] = value
    this.$http.patch(
      '/display_data/', payload
    ).then((response: AxiosResponse) => {
      console.log(response.data)
    })
  }
}
</script>
