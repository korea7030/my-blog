<template>
  <!-- Navigation -->
  <nav id="mainNav" class="navbar navbar-expand-lg navbar-light fixed-top">
    <div class="container">
      <a class="navbar-brand" href="index.html">
        Start Bootstrap
      </a>
      <button
        class="navbar-toggler navbar-toggler-right"
        type="button"
        data-toggle="collapse"
        data-target="#navbarResponsive"
        aria-controls="navbarResponsive"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        Menu
        <i class="fas fa-bars" />
      </button>
      <div id="navbarResponsive" class="collapse navbar-collapse">
        <b-nav pills class="navbar-nav ml-auto">
          <b-nav-item active class="nav-item">
            Active
          </b-nav-item>
          <b-nav-item class="nav-item">
            Link
          </b-nav-item>
          <b-nav-item-dropdown
            id="my-nav-dropdown"
            text="Dropdown"
            toggle-class="nav-link-custom"
            right
          >
            <b-dropdown-item v-for="category in categoryList" :key="category.id">
              <nuxt-link :to="{name: 'category-cid-post', params: {cid: category.id}}">{{ category.category_name }}</nuxt-link>
            </b-dropdown-item>
          </b-nav-item-dropdown>
        </b-nav>
      </div>
    </div>
  </nav>
</template>
<script>
  export default {
    data() {
      return {
        categoryList: null
      }
    },
    created() {
      this.$axios.get('blog/').then((resp) => {
        if (resp.status === 200) {
          this.categoryList = resp.data
        } else {
          console.log('1')
        }
      }).catch((err) => {
        console.log(err)
      })
    }

  }
</script>
