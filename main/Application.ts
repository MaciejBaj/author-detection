'use strict';

import * as bodyParser from 'body-parser';
import * as express from 'express';
import * as http from 'http';

const PORT = 7000;

export class Application {

  private app: any;
  private server: any;

  constructor() {
    this.app = express();
    this.server = http.createServer(this.app);
    this.app.use(bodyParser.json());
    this.app.use(bodyParser.urlencoded({extended: false}));
    this.app.use(express.static('public'));
  
    this.webpackDevMiddlewares(this.app);

    this.app.route('/parseAndRecognize').post((req, res) => {
      console.log(req.body);
      res.status(200).send("OK");
    });
  }


  
  public start() {
    this.server.listen(PORT, () => {
      console.log('Express server listening on %d', PORT);
    });
  }
  
  private webpackDevMiddlewares(app) {

    let webpackDevMiddleware = require('webpack-dev-middleware');
    let webpack = require('webpack');
    let webpackConfig = require('./webpack.config');
    let webpackCompiler = webpack(webpackConfig);

    this.app.use(
      webpackDevMiddleware(webpackCompiler, {
        hot: true,
        stats: {
          colors: true
        }
      })
    );
  }
}
