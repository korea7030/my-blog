<template>
  <div style="font-family: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;">
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand href="/">JH dev blog</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item-dropdown text="Category" right>
            <b-dropdown-item v-for="category in categoryList" :key="category.id">
              <nuxt-link :to="{name: 'category-cid-post', params: {cid: category.id}}">
                {{ category.category_name }}
              </nuxt-link>
            </b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        categoryList: null,
        active_el: 0
      }
    },
    created() {
      this.$axios.get('blog/').then((resp) => {
        if (resp.status === 200) {
          this.categoryList = resp.data.results
        } else {
          console.log('1')
        }
      }).catch((err) => {
        console.log(err)
      })
    },
    methods: {
      activate(el) {
        this.active_el = el
      }
    }
  }
</script>
