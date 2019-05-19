<template>
  <!-- Post Content -->
  <article>
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
          <div class="post-heading">
            <h1>{{ postDetail.title }}</h1>
            <!-- <h2 class="subheading">
              Problems look mighty small from 150 miles up
            </h2>-->
            <span class="meta">Posted by
              <a href="#">
                {{ postDetail.author_name }}
              </a>
              on {{ postDetail.created_at }}</span>
          </div>
        </div>
        <div class="col-lg-8 col-md-10 mx-auto">
          <VueMarkdown>
            {{ postDetail.content }}
          </VueMarkdown>
        </div>
      </div>
    </div>
  </article>
</template>
<script>
  import VueMarkdown from 'vue-markdown'

  export default {
    components: {
      VueMarkdown
    },
    data() {
      return {
        postDetail: {
          id: null,
          title: null,
          content: null,
          category: null,
          created_at: null,
          draft: true,
          author_name: null,
          author: null
        }
      }
    },
    created() {
      const postDeatilUrl = 'blog/category/1/post/2'.replace('1', this.$route.params.cid).replace('2', this.$route.params.id)
      this.$axios.get(postDeatilUrl).then((resp) => {
        if (resp.status === 200) {
          this.postDetail = resp.data
        } else {
          console.log('1')
        }
      })
    }
  }
</script>
