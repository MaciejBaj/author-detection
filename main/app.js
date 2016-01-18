var PORT = 7000;

var express = require('express');
var app = express();
var http = require('http');
var server = http.createServer(app);
var bodyParser = require('body-parser');

var PARSER_ADDRESS = 'localhost';
var PARSER_PORT = '7001';
var RESULT_ADDRESS = 'localhost';
var RESULT_PORT = '7002';

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static('public'));

app.route('/detectAuthor').post(function(req, res) {
  var parserRequestOptions = {
    host: PARSER_ADDRESS,
    path: '/parse',
    port: PARSER_PORT,
    method: 'POST'
  };

  var resultRequestOptions = {
    host: RESULT_ADDRESS,
    path: '/classify',
    port: RESULT_PORT,
    method: 'POST'
  };

  var parserRequest = http.request(parserRequestOptions, function(parserResponse) {
    var resultRequest = http.request(resultRequestOptions, function(resultResponse) {
      return res.status(200).send("text has been classified: ", resultResponse);
    });
    resultRequest.write(parserResponse);
    resultRequest.end();
  });

  parserRequest.write(req.body);
  parserRequest.end();

});

app.route('/insertNewAuthorPosition').post(function(req, res) {
  var parserRequestOptions = {
    host: PARSER_ADDRESS,
    path: '/parseAndSave',
    port: PARSER_PORT,
    method: 'POST'
  };

  var parserRequest = http.request(parserRequestOptions, function(parserResponse) {
    return res.status(200).send("current ", req.body.name, " characteristics: ", JSON.stringify(parserResponse));
  });

  parserRequest.write(req.body);
  parserRequest.end();

});

server.listen(PORT, function () {
  console.log('Express server listening on %d', PORT);
});


// Expose app
exports = module.exports = app;