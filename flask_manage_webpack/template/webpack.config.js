const path = require('path');
const webpack = require('webpack');

/*
 * Webpack Plugins
 */
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');
const ManifestPlugin = require('webpack-manifest-plugin');
const CopyPlugin = require('copy-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

// take debug mode from the environment
const debug = (process.env.NODE_ENV !== 'production');

const rootAssetPath = path.join(__dirname, 'assets');

module.exports = {
  // configuration
  context: __dirname,
  entry: {
    main_js: path.join(__dirname, 'assets', 'js', 'main.js'),
    main_css: [
      path.join(__dirname, 'assets', 'css', 'main.css'),
    ],
  },
  output: {
    path: path.join(__dirname, 'app', 'static'),
    publicPath: "/static/",
    filename: "js/[name].[contentHash].js",
    chunkFilename: "js/[name].[contentHash].chunk.js"
  },
  optimization: {
  minimizer: [
   new UglifyJsPlugin({
        cache: true,
        parallel: true,
        sourceMap: true,
        uglifyOptions: {
          output: {
            comments: false
          }
        }
    }),
    new OptimizeCssAssetsPlugin({
      assetNameRegExp: /\.css$/g,
      cssProcessor: require('cssnano'),
      cssProcessorPluginOptions: {
        preset: ['default', { discardComments: { removeAll: true } }],
      },
      canPrint: true
    }),
  ],
},
  resolve: {
    extensions: ['.js', '.css'],
  },
  devtool: 'source-map',
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader,
            options: {
              hmr: debug,
            },
          },
          'css-loader',
          {
            loader: 'postcss-loader'
          }
        ],
      },
      { test: /\.html$/, loader: 'raw-loader' },
      { test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: 'url-loader', options: { limit: 10000, mimetype: 'demolication/font-woff' } },
      { test: /\.js$/, exclude: /node_modules/, loader: 'babel-loader', query: { presets: ['@babel/preset-env'], cacheDirectory: true } },
    ],
  },
  plugins: [
    new CleanWebpackPlugin(),
    new MiniCssExtractPlugin({ filename: 'css/[name].[contentHash].css', }),
//    new webpack.ProvidePlugin({ $: 'jquery', jQuery: 'jquery' }),

    new CopyPlugin([
      {
        from: `${rootAssetPath}`,
        to: `${path.join(__dirname, 'demo', 'static')}/[path]/[name].[contentHash].[ext]`,
        test: /\.(ttf|eot|svg|png|jpe?g|gif|ico)(\?.*)?$/i,
        toType: 'template',
      },

    ], {copyUnmodified: true}),
    new ManifestPlugin(
    {
        map: (file) => {
        // Remove hash in manifest key
        file.name = file.name.replace(/(\.[a-f0-9]{32})(\..*)$/, '$2');
        return file;
        },
    }),
  ].concat(debug ? [] : [
    // production webpack plugins go here
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: JSON.stringify('production'),
      } }),
  ]),
};
