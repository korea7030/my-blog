<template>
  <div class="container">
    <div class="row">
      <div v-for="post in CategoryByPostList" :key="post.id" class="col-lg-8 col-md-10 mx-auto">
        <div class="post-preview">
          <nuxt-link :to="{name: 'category-cid-post-id', params: {cid: categoryId, id: post.id}}">
            <h2 class="post-title">
              {{ post.title }}
            </h2>
          </nuxt-link>
          <p class="post-meta">
            Posted by
            <a href="#">
              {{ post.author_name }}
            </a>
            {{ post.created_at }}
          </p>
        </div>
        <hr>
        <!-- Pager -->
        <div class="clearfix">
          <a class="btn btn-primary float-right" href="#">
            Older Posts &rarr;
          </a>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        categoryId: this.$route.params.cid,
        CategoryByPostList: null
      }
    },
    created() {
      const categoryByPostUrl = 'blog/category/1'.replace('1', this.$route.params.cid)
      this.$axios.get(categoryByPostUrl).then((resp) => {
        if (resp.status === 200) {
          this.CategoryByPostList = resp.data
        } else {
          console.log('1')
        }
      })
    }
  }
</script>
