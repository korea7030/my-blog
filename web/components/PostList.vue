<template>
  <div class="container">
    <div class="row">
      <div v-for="post in pList" id="my-table" :key="post.id" class="col-lg-8 col-md-10 mx-auto">
        <div class="post-preview">
          <nuxt-link :to="{name: 'category-cid-post-id', params: {cid: post.category, id: post.id}}">
            <h2 class="post-title">
              [{{ post.category_name }}] {{ post.title }}
            </h2>
          </nuxt-link>
          <p class="post-meta">
            Posted by
            <a href="#">
              {{ post.author_name }}
            </a>
            {{ post.created_at }}
          </p>
        </div>
        <hr>
      </div>
    </div>
    <!-- Pager -->
    <div class="clearfix">
      <Pagination :pageLink="links" @prev="getPostList(links.previous)" @next="getPostList(links.next)">
      </Pagination>
    </div>
  </div>
</template>
<script>
  import Pagination from '~/components/Pagination'

  export default {
    components: {
      Pagination
    },
    props: {
      postList: {
        type: Array,
        required: true
      },
      links: {
        type: Object,
        required: true
      }
    },
    data() {
      return {
        querypage: 1
      }
    },
    computed: {
      pList: function () {
        return this.postList
      }
    },
    methods: {
      getPostList(page) {
        this.$axios.get('blog/posts/',
                        { params: { page: page }
                        }).then((resp) => {
          if (resp.status === 200) {
            this.postList = resp.data.results
            this.links = resp.data.links
            this.querypage = page
          } else {
            console.log('1')
          }
        })
      }
    }
  }
</script>
