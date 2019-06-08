<template>
  <div class="container">
    <div class="row">
      <div v-for="post in CategoryByPostList" :key="post.id" class="col-lg-8 col-md-10 mx-auto">
        <div class="post-preview">
          <nuxt-link :to="{name: 'category-cid-post-id', params: {cid: categoryId, id: post.id}}">
            <h2 class="post-title">
              [{{ post.category.category_name }}] {{ post.title }}
            </h2>
          </nuxt-link>
          <p class="post-meta">
            Posted by
            <a href="https://www.facebook.com/jaehyun.lee.37" target="_blank">
              {{ post.author_name }}
            </a>
            {{ post.created_at }}
          </p>
        </div>
        <hr>
      </div>
    </div>
    <!-- Pager -->
    <div class="clearfix">
      <Pagination :pageLink="links" @prev="getCategoryByPost(links.previous)" @next="getCategoryByPost(links.next)">
      </Pagination>
    </div>
  </div>
</template>
<script>
  import Pagination from '~/components/Pagination'

  export default {
    components: {
      Pagination
    },
    data() {
      return {
        querypage: 1,
        categoryId: this.$route.params.cid,
        CategoryByPostList: null,
        links: {
          previous: null,
          next: null,
          count: null,
          start_index: null,
          end_index: null,
          cur_page: null,
          per_page: null
        }
      }
    },
    created() {
      this.getCategoryByPost(this.querypage)
    },
    methods: {
      getCategoryByPost(page) {
        const categoryByPostUrl = 'blog/category/1'.replace('1', this.$route.params.cid)
        this.$axios.get(categoryByPostUrl, { params: { page: page } }).then((resp) => {
          if (resp.status === 200) {
            this.CategoryByPostList = resp.data.results
            this.links = resp.data.links
            this.querypage = page
          } else {
            console.log('1')
          }
        })
      }
    }
  }
</script>
