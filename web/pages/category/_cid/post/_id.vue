<template>
  <section class="container">
    <Nav />
    <Header />
    <PostContent />
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
    }
  }
</script>
<style>
</style>
