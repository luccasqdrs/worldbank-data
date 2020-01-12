<template>
  <div>
    <a-button type="primary" :disabled="!hasSelected">Compare</a-button>
    <span style="margin-left: 8px">
      <template v-if="hasSelected">{{`Selected ${selectedKeys.length} items`}}</template>
    </span>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator'
import { AxiosResponse } from 'axios'

@Component
export default class TableCompareButton extends Vue {
  @Prop() selectedKeys:Array<number>;
  @Prop() handleClick;

  get hasSelected () {
    return this.selectedKeys.length > 0
  }
}
</script>
