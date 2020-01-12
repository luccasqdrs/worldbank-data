<template>
  <div>
    <a-select
      mode="multiple"
      :defaultValue="defaultCountries"
      style="width: 100%"
      @change="handleChange"
      placeholder="Please select countries"
      :maxTagCount="5"
      :maxTagTextLength="11"
    >
      <a-select-option v-for="country in countries" :key="country.code">{{country.name}}</a-select-option>
    </a-select>
  </div>

</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator'
import { AxiosResponse } from 'axios'

@Component
export default class TableCountryFilter extends Vue {
  @Prop() defaultCountries:Array<string>;
  @Prop() handleChange;
  countries:Array<string> = [];

  private mounted () {
    this.$http
      .get('/countries/')
      .then((response: AxiosResponse) => {
        this.countries = response.data
      })
  }
}
</script>
