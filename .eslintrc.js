module.exports = {
    parser: '@babel/eslint-parser',
    env: {
        browser: true,
        commonjs: true,
        es6: true,
        node: true,
    },
    parserOptions: {
        ecmaVersion: 2021,
        ecmaFeatures: {
            impliedStrict: true,
            jsx: true,
        },
        sourceType: 'module',
    },
    plugins: ['react', 'react-hooks'],
    extends: [
        'eslint:recommended',
        'plugin:react/recommended',
        'plugin:react-hooks/recommended',
    ],
    settings: {
        react: {
            version: 'detect',
        },
    },
    rules: {
        // You can do your customizations here...
        // For example, if you don't want to use the prop-types package,
        // you can turn off that recommended rule with: 'react/prop-types': ['off']
    },
};
