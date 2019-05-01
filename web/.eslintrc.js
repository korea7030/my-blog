module.exports = {
  root: true,
  env: {
    browser: true,
    es6: true,
    node: true
  },
  parserOptions: {
    parser: 'babel-eslint',
    sourceType: 'module'
  },
  plugins: [],
  extends: [
    '@nuxtjs',
    'plugin:vue/recommended'
  ],
  rules: {
    /* eslint-disable */
    'no-console': 'off',
    'indent': 'off',
    'vue/script-indent': ['error', 2, {'baseIndent': 1}],
    'vue/html-self-closing': ['error', {
      'html': {
        'void': 'never',
        'normal': 'always',
        'component': 'any'
      }
    }],
    'vue/singleline-html-element-content-newline': ['warn', {
      'ignoreWhenNoAttributes': true,
      'ignoreWhenEmpty': true,
      'ignores': ['Button']
    }],
    'vetur.validation.template': false,
    'vue/html-closing-bracket-newline': 'error'
  }
}

