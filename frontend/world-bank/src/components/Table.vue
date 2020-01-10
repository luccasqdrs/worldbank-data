<template>
  <div>
    <div style="margin-bottom: 16px">
      <a-button type="primary" :disabled="!hasSelected" :loading="loading">Compare</a-button>
      <span style="margin-left: 8px">
        <template v-if="hasSelected">{{`Selected ${selectedRowKeys.length} items`}}</template>
      </span>
    </div>
    <a-table :columns="columnsData" :dataSource="data" :rowSelection="{selectedRowKeys: selectedRowKeys, onChange: onSelectChange}" :pagination="false">
    </a-table>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator'
import { AxiosResponse } from 'axios'

@Component
export default class Table extends Vue {
  @Prop() private countries!:Array<string>;
  selectedRowKeys:Array<string> = [];
  loading:Boolean = false;
  columnsData = [
    {
      title: 'Country Code',
      dataIndex: 'country',
      sorter: (a, b) => a.country.toUpperCase() < b.country.toUpperCase()
    },
    {
      title: 'Country Name',
      dataIndex: 'country_name',
      sorter: (a, b) => a.country_name.toUpperCase() < b.country_name.toUpperCase()
    }
  ];
  data = [];
  countrys = ['USA', 'MEX', 'IND', 'CHN', 'NGA']

  private mounted () {
    this.$http.get('http://127.0.0.1:8000/indicators/').then((response: AxiosResponse) => {
      this.columnsData.push(...response.data.map((indicator:any) => {
        let indCode = indicator.code.split('.').join('_')
        return {
          title: indicator.name,
          dataIndex: indCode,
          note: indicator.note,
          sorter: (a, b) => a[indCode] - b[indCode]
        }
      }))
    })
    this.$http.get(`http://127.0.0.1:8000/display_data/?countrys=${this.countrys.join()}&years=2018`).then((response: AxiosResponse) => {
      let data = response.data
      data.forEach((row:any) => { row.key = row.id })
      this.data.push(...data)
    })
  }

  get hasSelected () {
    return this.selectedRowKeys.length > 0
  }

  onSelectChange (selectedRowKeys:any) {
    this.selectedRowKeys = selectedRowKeys
  }
}
</script>
