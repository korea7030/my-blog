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
        <div class="markdown-body" v-html="$md.render(postDetail.content)" />
      </div>
    </div>
    <div class="comments">
      <vue-disqus ref="disqus" :shortname="disqusShortname" :identifier="disqusId"></vue-disqus>
    </div>
  </article>
</template>
<script>
  // import marked from 'marked'

  export default {
    layout: 'blog',
    data() {
      return {
        postDetail: {
          id: null,
          title: null,
          content: '',
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
      const postDeatilUrl = 'blog/category/c1/post/p1'.replace('c1', this.$route.params.cid).replace('p1', this.$route.params.id)
      this.$axios.get(postDeatilUrl).then((resp) => {
        if (resp.status === 200) {
          this.postDetail = resp.data
          // this.postDetail.content = marked(this.postDetail.content)
        } else {
          console.log('error')
        }
      })
    }
  }
</script>
<style>
  @import "https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/3.0.1/github-markdown.css";

  .markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
  }

  @media (max-width: 767px) {
    .markdown-body {
      padding: 15px;
    }
  }
</style>
