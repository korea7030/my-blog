<template>
  <div v-if="pageLink.count > 0" class="m-b-50">
    <div class="pagination text-right">
      <span class="pages">
        {{ pageLink.start_index }}-{{ pageLink.end_index }}/{{ pageLink.count }}
      </span>
      <a v-if="pageLink.previous" class="btn btn-icon btn-default" @click="$emit('prev')">
        <i class="ivu-icon ivu-icon-ios-arrow-back" />
      </a>
      <a v-else href="" class="btn btn-icon btn-default disabled" :disabled="!pageLink.previous">
        <i class="ivu-icon ivu-icon-ios-arrow-back" />
      </a>
      <a v-if="pageLink.next" class="btn btn-icon btn-default" @click="$emit('next')">
        <i class="ivu-icon ivu-icon-ios-arrow-forward" />
      </a>
      <a v-else href="" class="btn btn-icon btn-default disabled" :disabled="!pageLink.next">
        <i class="ivu-icon ivu-icon-ios-arrow-forward" />
      </a>
    </div>
  </div>
</template>
<script>
  export default {
    props: {
      pageLink: {
        type: Object,
        required: true
      }
    }
  }
</script>
<style>

</style>
