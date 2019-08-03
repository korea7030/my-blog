<template>
  <section class="container">
    <Nav />
    <Header />
    <PostList :postList="PostList" :links="links" :querypage="querypage" />
    <Footer />
  </section>
</template>

<script>
  import Header from '~/components/Header.vue'
  import Footer from '~/components/Footer.vue'
  import Nav from '~/components/Nav.vue'
  import PostList from '~/components/PostList.vue'

  export default {
    components: {
      Header,
      Footer,
      Nav,
      PostList
    },
    data() {
      return {
        querypage: 1,
        PostList: null,
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
    asyncData: async ({ app, params }) => {
      try {
        const res = await app.$axios.$get('blog/posts/', { params: { page: params.page } })
        return { PostList: res.results, links: res.links, querypage: params.page }
      } catch (e) {
        console.log(e)
      }
    }
  }
</script>
<style>
</style>
