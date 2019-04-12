var source_api = 'http://rss.uol.com.br/feed/economia.xml';

var request = require('request');
request(source_api, function (error, response, body) {
  console.log('error:', error); // Print the error if one occurred
  console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
  console.log('body:', body); // Print the HTML for the Google homepage.
});