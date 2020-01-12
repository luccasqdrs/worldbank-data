<template>
  <div>
    <a-select
      showSearch
      placeholder="Select a year"
      :defaultValue="defaultYear"
      style="width: 200px"
      @change="handleChange"
    >
      <a-select-option v-for="i in years" :key="i">{{i}}</a-select-option>
    </a-select>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator'
import { AxiosResponse } from 'axios'

@Component
export default class TableYearFilter extends Vue {
  @Prop() defaultYear;
  @Prop() handleChange;

  get years () {
    let yearsList = []
    for (let i = 1960; i < 2020; i++) {
      yearsList.push(i)
    }
    return yearsList
  }
}
</script>
