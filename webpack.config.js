const path = require("path");
const webpack = require("webpack");

module.exports = {

    mode: "development",

    // define entry points
    entry: {
        app: "./src/js/main.js",
        signup: "./src/js/signup.js"

    },
    // define output point
    output:{
        path: path.resolve(__dirname, "src/dist"),
        filename: "[name].min.js",
    },
    module: {
        rules:[{
            test:/\.js$/,
            exclude:/node_modules/,
            use:[{
                loader:"babel-loader",
                options:{
                    presets:["env"]
                }
            }]
        },
        {
            test:/\.css$/,
            use:[
                "style-loader",
                "css-loader"
            ]
        },
        {
            test:/\.(jpg | png)$/,
            use:[
                "file-loader",
                {
                    loader: "image-webpack-loader",
                    options:{
                        name:"[name].[ext]",
                        outputPath:"/img/",
                        publicPath:"/img/"
                    }
                }
                
            ]
        }
]
    }
}