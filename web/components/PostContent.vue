<template>
  <!-- Post Content -->
  <article>
    <div class="container">
      <div class="row">
        <div class="col-md-10 mx-auto" style="margin-bottom:20px;">
          <div class="post-heading">
            <h1>{{ postDetail.title }}</h1>
            <!-- <h2 class="subheading">
              Problems look mighty small from 150 miles up
            </h2>-->
            <span class="meta">Posted by
              <a href="https://www.facebook.com/jaehyun.lee.37" target="_blank">
                {{ postDetail.author_name }}
              </a>
              on {{ postDetail.created_at }} | </span>
            <span style="float:right;">
              {{ postDetail.read_count }} Views
            </span>
          </div>
        </div>
        <hr>
        <div class="col-lg-8 col-md-10 mx-auto" v-html="postDetail.content" />
      </div>
    </div>
    <div class="comments">
      <vue-disqus ref="disqus" :shortname="disqusShortname" :identifier="disqusId"></vue-disqus>
    </div>
  </article>
</template>
<script>
  import kramed from 'kramed'

  export default {
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
          author: null,
          read_count: 0
        }
      }
    },
    computed: {
      disqusShortname() {
        return 'korea7030'
      },
      disqusId() {
        return 'p' + this.postDetail.category + this.postDetail.id
      }
    },
    created() {
      console.log(this.$route.params.cid)
      console.log(this.$route.params.id)
      const postDeatilUrl = 'blog/category/c1/post/p1'.replace('c1', this.$route.params.cid).replace('p1', this.$route.params.id)
      this.$axios.get(postDeatilUrl).then((resp) => {
        if (resp.status === 200) {
          this.postDetail = resp.data
          kramed.setOptions({
            renderer: new kramed.Renderer(),
            gfm: true,
            tables: true,
            breaks: true,
            pedantic: true,
            sanitize: true,
            smartLists: true,
            smartypants: true
          })
          kramed.defaults = {
            // Lexer options (both block and inline lexers)
            gfm: true,
            tables: true,
            mathjax: true,

            // Kramed options
            highlight: true,

            // Renderer options
            langPrefix: 'lang-',
            smartypants: true,
            headerAutoId: true
          }
          this.postDetail.content = kramed(this.postDetail.content)
        } else {
          console.log('error')
        }
      })
    }
  }
</script>
