<template>
  <div>
    <a-row>
      <a-col :span="8">
        <div>
          <a-button type="primary" :disabled="!hasSelected" :loading="loading">Compare</a-button>
          <span style="margin-left: 8px">
            <template v-if="hasSelected">{{`Selected ${selectedRowKeys.length} items`}}</template>
          </span>
        </div>
      </a-col>
      <a-col :offset="4" :span="12">
        <a-row>
          <a-col :span="6">
            <a-select
              showSearch
              placeholder="Select a year"
              :defaultValue="selectedYear"
              style="width: 200px"
              @change="filterYear"
            >
              <a-select-option
              v-for="i in years"
              :key="i"
              >{{i}}</a-select-option>
            </a-select>
          </a-col>
          <a-col :span="18">
            <a-select
              mode="multiple"
              :defaultValue="selectedCountries"
              style="width: 100%"
              @change="filterCountries"
              placeholder="Please select countries"
              :maxTagCount="5"
              :maxTagTextLength="11"
            >
              <a-select-option
                v-for="country in countries"
                :key="country.code"
              >{{country.name}}</a-select-option>
            </a-select>
          </a-col>
        </a-row>
      </a-col>
    </a-row>

    <a-table
      :columns="columnsData"
      :dataSource="data"
      :rowSelection="{selectedRowKeys: selectedRowKeys, onChange: onSelectChange}"
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
import EditableCell from './EditableCell.vue'

@Component
export default class Table extends Vue {
  selectedRowKeys: Array<string> = [];
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
  selectedYear: Number = 2018;
  data = [];
  selectedCountries = ['CHN', 'IND', 'MEX', 'NGA', 'USA'];
  countries: Array<any> = [];

  get years () {
    let yearsList = []
    for (let i = 1960; i < 2020; i++) {
      yearsList.push(i)
    }
    return yearsList
  }

  private mounted () {
    this.$http
      .get('/countries/')
      .then((response: AxiosResponse) => {
        this.countries = response.data
      })
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

  get hasSelected () {
    return this.selectedRowKeys.length > 0
  }

  getData () {
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
      })
  }

  filterYear (value:Number) {
    this.selectedYear = value
    this.getData()
  }

  filterCountries (value:Array<string>) {
    this.selectedCountries = value
    this.getData()
  }
  onSelectChange (selectedRowKeys: any) {
    this.selectedRowKeys = selectedRowKeys
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

<style>
  .editable-cell {
    position: relative;
  }

  .editable-cell-input-wrapper,
  .editable-cell-text-wrapper {
    padding-right: 24px;
  }

  .editable-cell-text-wrapper {
    padding: 5px 24px 5px 5px;
  }

  .editable-cell-icon,
  .editable-cell-icon-check {
    position: absolute;
    right: 0;
    width: 20px;
    cursor: pointer;
  }

  .editable-cell-icon {
    line-height: 18px;
    display: none;
  }

  .editable-cell-icon-check {
    line-height: 28px;
  }

  .editable-cell:hover .editable-cell-icon {
    display: inline-block;
  }

  .editable-cell-icon:hover,
  .editable-cell-icon-check:hover {
    color: #108ee9;
  }

  .editable-add-btn {
    margin-bottom: 8px;
  }
</style>
