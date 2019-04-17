// var source_api = 'http://rss.uol.com.br/feed/economia.xml';
var requestOptions  = { encoding: 'binary', method: 'GET', uri: 'http://rss.uol.com.br/feed/economia.xml'};
var parser = require('fast-xml-parser');

var request = require('request');
request(requestOptions, function (error, response, body) {
  var json = parser.parse(body);
  var newsArray = json['rss']['channel']['item'];
  newsArray.forEach(function(news){ 
    delete news.link; 
    delete news.pubDate;
    news.description = news.description.replace(/<img .*?>/g, '');
  });
});