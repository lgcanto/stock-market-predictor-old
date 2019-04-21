const requestOptions  = { encoding: 'binary', method: 'GET', uri: 'http://rss.uol.com.br/feed/economia.xml'};
const todayDate = new Date();
const request = require('request');
const parser = require('fast-xml-parser');
const json2csv = require('csvjson-json2csv');
const fs = require('fs');

request(requestOptions, function (error, response, body) {
  
  var json = parser.parse(body);
  var newsArray = json['rss']['channel']['item']; //The news RSS must be analysed before defining this
  
  newsArray.forEach(function(news){ 
    delete news.link; 
    delete news.pubDate;
    news.description = news.description.replace(/<img .*?>/g, ''); //Takes off <img> tags from the news body
  });

  var newsCsv = json2csv(newsArray);
  var fileName =  todayDate.getFullYear() + "_" + (todayDate.getMonth() + 1) + "_" + todayDate.getDate() + "_" + "news_input.csv";

  fs.writeFile(fileName, newsCsv, function(err) {
    if(err) {
        return console.log(err);
    }

    console.log("Today's news set saved.");
  });

});

