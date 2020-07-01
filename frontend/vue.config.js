module.exports = {
    devServer: {
        host: '0.0.0.0',
        port: 8080
    },
    lintOnSave: false,
    chainWebpack: config => {
        config
            .plugin('html')
            .tap(args => {
                args[0].title = 'Crypto Follower'
                return args
            })
    }
}