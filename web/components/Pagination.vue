<template>
  <nav v-if="pageLink.count > 0" aria-label="Page navigation example">
    <ul class="pagination pg-blue justify-content-center">
      <li class="page-item">
        <a v-if="pageLink.previous" href="#" class="page-link" @click="$emit('prev')">
          <span class="text-danger">
            Prev
          </span>
        </a>
        <a v-else class="page-link" :disabled="!pageLink.previous">
          Prev
        </a>
      </li>
      <li class="page-item">
        <a class="page-link">
          {{ pageLink.cur_page }}
        </a>
      </li>
      <li class="page-item">
        <a v-if="pageLink.next" href="#" class="page-link" @click="$emit('next')">
          <span class="text-warning">
            Next
          </span>
        </a>
        <a v-else class="page-link" :disabled="!pageLink.next">
          Next
        </a>
      </li>
    </ul>
  </nav>
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
