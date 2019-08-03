<template>
  <section class="container">
    <Nav />
    <Header />
    <PostContent :postDetail="postDetail" />
    <Footer />
  </section>
</template>

<script>
  import Header from '~/components/Header.vue'
  import Footer from '~/components/Footer.vue'
  import Nav from '~/components/Nav.vue'
  import PostContent from '~/components/PostContent.vue'

  export default {
    components: {
      Header,
      Footer,
      Nav,
      PostContent
    },
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
    asyncData: async ({ app, params }) => {
      try {
        const postDetailUrl = 'blog/category/c1/post/p1'.replace('c1', params.cid).replace('p1', params.id)
        const res = await app.$axios.$get(postDetailUrl)
        return { postDetail: res }
      } catch (e) {
        console.log('err' + e)
      }
    }
  }
</script>
<style>
</style>
