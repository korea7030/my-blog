<template>
  <div class="container">
    <div class="row">
      <div v-for="post in PostList" :key="post.id" class="col-lg-8 col-md-10 mx-auto">
        <div class="post-preview">
          <nuxt-link :to="{name: 'category-cid-post-id', params: {cid: post.category, id: post.id}}">
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
        PostList: null,
        links: {
          previous: null,
          next: null,
          count: null,
          start_index: null,
          end_index: null,
          cur_page: null
        }
      }
    },
    created() {
      this.$axios.get('blog/posts/').then((resp) => {
        if (resp.status === 200) {
          this.PostList = resp.data.results
          this.links = resp.data.links
        } else {
          console.log('1')
        }
      }).catch((err) => {
        console.log(err)
      })
    }
  }
</script>
