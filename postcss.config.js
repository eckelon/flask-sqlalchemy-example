module.exports = {
  parser: 'postcss-scss',
  plugins: [
    require('cssnano')({}),
    require('autoprefixer')({}),
    require('postcss-nested')({}),
  ],
}