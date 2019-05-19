<template>
  <section class="container">
    <Nav />
    <Header />
    <CategoryByPost />
    <Footer />
  </section>
</template>

<script>
  import Header from '~/components/Header.vue'
  import Footer from '~/components/Footer.vue'
  import Nav from '~/components/Nav.vue'
  import CategoryByPost from '~/components/CategoryByPost.vue'

  export default {
    components: {
      Header,
      Footer,
      Nav,
      CategoryByPost
    }
  }
</script>
<style>
</style>
