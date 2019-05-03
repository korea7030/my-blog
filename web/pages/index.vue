<template>
  <section class="container">
    <Nav />
    <Header />
    <PostList />
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
    }
  }
</script>
<style>
</style>
