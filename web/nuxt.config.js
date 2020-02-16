import pkg from './package'

const baseURL = (process.env.NODE_ENV !== 'production') ? 'http://localhost:8000/' : 'http://www.jhdevblog.com:8000/'

export default {
  mode: 'universal',

  /*
  ** Headers of the page
  */
  head: {
    title: 'JH DEV BLOG',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'DRF + Nuxt.js 프레임워크 기반 블로그' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      { rel: 'stylesheet', type: 'text/css', href: 'https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic'},
      { rel: 'stylesheet', type: 'text/css', href: 'https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800'}
    ]
  },

  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },

  /*
  ** Global CSS
  */
  css: [
    { src: '~/node_modules/highlight.js/styles/atom-one-dark.css', lang: 'css' },
    '~assets/vendor/bootstrap/css/bootstrap.css',
    '~assets/vendor/fontawesome-free/css/all.css',
    '~assets/css/main.css'
  ],

  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    '~plugins/disqus',
    // '~/plugins/axios',
  ],

  /*
  ** Axios module configuration
  */
  /*
  ** Nuxt.js modules
  */

  modules: [
    // Doc: https://bootstrap-vue.js.org/docs/
    'bootstrap-vue/nuxt',
    '@nuxtjs/pwa',
    '@nuxtjs/axios', // axios add
    '@nuxtjs/markdownit',
    ['@nuxtjs/google-analytics', {
      id: 'UA-65871545-2'
    }],
    'nuxt-seo',
    '@nuxtjs/sitemap'
  ],
  seo: {
    title: "JH DEV Blog"
  },
  axios: {
    baseURL: baseURL, ssr: false
  },
  sitemap: {
    hostname: 'http://www.jhdevblog.com',
    gzip: true,
    exclude: [
      '/admin/**',
      ':8000/admin/**'
    ],
    routes() {
      return axios.get('http://www.jhdevblog.com/category').then(res => res.data.map(category => '/category/' + category.id))
    }
  },
  markdownit: {
    injected: true,
    preset: 'default',
    linkify: true,
    breaks: true,
    use: [
      'markdown-it-highlightjs'
    ]
  },
  /*
  ** Build configuration
  */
  build: {
    extractCSS: true,
    /*
    ** You can extend webpack config here
    */
    extend (config, ctx) {
      // Run ESLint on save
      if (ctx.isDev && ctx.isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  }
}
