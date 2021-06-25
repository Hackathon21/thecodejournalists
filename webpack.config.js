const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    entry: {
        react: path.join(__dirname, 'frontend/src/index'),
        django: path.join(__dirname, 'frontend/assets/js/index'),
    },
    output: {
        path: path.join(__dirname, 'frontend/assets/dist'),
        filename: '[name]-bundle.js'
    },
    resolve: {
        extensions: ['*', '.js', '.jsx'],
        alias: {
            Assets: path.resolve(__dirname, 'frontend/assets/'),
            Images: path.resolve(__dirname, 'frontend/assets/images/'),
            Styles: path.resolve(__dirname, 'frontend/assets/sass/'),
            Scripts: path.resolve(__dirname, 'frontend/assets/js/'),
        },
    },
    plugins: [
        new BundleTracker({
            path: __dirname,
            filename: 'webpack-stats.json'
        }),
        new MiniCssExtractPlugin(),
    ],
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
            },
            {
                test: /\.(css)$/,
                use: [MiniCssExtractPlugin.loader, 'css-loader']
            },
            {
                test: /\.(s(a|c)ss)$/,
                exclude: /\.module.(s(a|c)ss)$/,
                use: [MiniCssExtractPlugin.loader, 'css-loader', 'sass-loader']
            },
            {
                test: /\.(woff|woff2|eot|ttf|svg|jpg|png)$/,
                use: {
                    loader: 'url-loader',
                },
            },
        ],
    },
}
