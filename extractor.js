var source_api = 'http://rss.uol.com.br/feed/economia.xml';
var parser = require('fast-xml-parser');

var request = require('request');
request(source_api, function (error, response, body) {
  var json = parser.parse(body);
  var newsArray = json['rss']['channel']['item'];
});