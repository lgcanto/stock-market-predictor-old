const fs = require('fs');
const csv2json = require('csvjson-csv2json');
const todayDate = new Date();
const deepai = require('deepai');
deepai.setApiKey('7cbaba1f-6200-474f-9398-b22c03b502f2');

var fileNameInput =  todayDate.getFullYear() + "_" + (todayDate.getMonth() + 1) + "_" + todayDate.getDate() + "_" + "news_input.csv";
var fileNameOutput =  todayDate.getFullYear() + "_" + (todayDate.getMonth() + 1) + "_" + todayDate.getDate() + "_" + "news_outputt.csv";

// async function deepaiAnalyser(newsDescription){
//   var resp = await deepai.callStandardApi("sentiment-analysis", {
//     text: newsDescription
//   });
//   console.log(resp);
//   return resp;
// }

fs.readFile(fileNameInput, {encoding: 'utf-8'}, function(err,data){
  if (!err) {
    var newsArray = csv2json(data);

    for (i = 0; i < newsArray.length; i++) { 
      // var deepaiReponse = deepaiAnalyser(newsArray[i].description);
    }

  } else {
      console.log(err);
  }
});

async function start(){
  var resp = await deepai.callStandardApi("sentiment-analysis", {
    text: "Aeroporto de Guarulhos proíbe decolagens da Avianca por falta de pagamento",
  });
  console.log(resp);
}

start();