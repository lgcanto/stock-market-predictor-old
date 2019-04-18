const requestOptions  = { encoding: 'binary', method: 'GET', uri: 'http://rss.uol.com.br/feed/economia.xml'};
const request = require('request');
const parser = require('fast-xml-parser');
const json2csv = require('csvjson-json2csv');

request(requestOptions, function (error, response, body) {
  
  var json = parser.parse(body);
  var newsArray = json['rss']['channel']['item'];
  
  newsArray.forEach(function(news){ 
    delete news.link; 
    delete news.pubDate;
    news.description = news.description.replace(/<img .*?>/g, '');
  });

  var newsCsv = json2csv(newsArray);
  console.log(newsCsv);

});

