<template>
  <b-pagination
    v-model="pageLink.cur_page"
    :total-rows="pageLink.count"
    :per-page="pageLink.per_page"
    aria-controls="my-table"
  ></b-pagination>
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
