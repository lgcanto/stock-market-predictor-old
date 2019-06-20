const fs = require('fs');
const csv2json = require('csvjson-csv2json');
const json2csv = require('csvjson-json2csv');
const todayDate = new Date();
const deepai = require('deepai');
deepai.setApiKey('7cbaba1f-6200-474f-9398-b22c03b502f2');

var fileNameInput =  todayDate.getFullYear() + "_" + (todayDate.getMonth() + 1) + "_" + todayDate.getDate() + "_" + "news_input.csv";
var fileNameOutput =  todayDate.getFullYear() + "_" + (todayDate.getMonth() + 1) + "_" + todayDate.getDate() + "_" + "news_output.csv";

async function deepaiAnalyser(newsDescription){
  var resp = await deepai.callStandardApi("sentiment-analysis", {
    text: newsDescription
  });
  return resp.output[0];
}

fs.readFile(fileNameInput, {encoding: 'utf-8'}, function(err,data){
  if (!err) {
    var newsArray = csv2json(data);

    var i = 0;
    function myLoop () {
      setTimeout(function () {
        deepaiAnalyser(newsArray[i].description).then(function(value) {
          newsArray[i].sentiment = value;
          i++;
          if (i < newsArray.length) {         
            myLoop ();
          }
          else{
            console.log(newsArray);
            var resultCsv = json2csv(newsArray);
            fs.writeFile(fileNameOutput, resultCsv, function(err) {
              if(err) {
                  return console.log(err);
              }

              console.log("Today's output saved.");
            });
          }
        });
      }, 500);
    };
    myLoop();

  } else {
      console.log(err);
  }
});