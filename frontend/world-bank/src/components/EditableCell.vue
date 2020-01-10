<template>
  <div class="editable-cell">
    <div v-if="editable" class="editable-cell-input-wrapper">
      <a-input :value="value" @change="handleChange" @pressEnter="check" /><a-icon
        type="check"
        class="editable-cell-icon-check"
        @click="check"
      />
    </div>
    <div v-else class="editable-cell-text-wrapper">
      {{ value || ' ' }}
      <a-icon type="edit" class="editable-cell-icon" @click="edit" />
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator'
import { AxiosResponse } from 'axios'

@Component
export default class EditableCell extends Vue {
  @Prop() private text!: string;

    editable = false;
    value = this.text;

    handleChange (e:any) {
      const value = e.target.value
      this.value = value
    }
    check () {
      this.editable = false
      this.$emit('change', this.value)
    }
    edit () {
      this.editable = true
    }
}
</script>
