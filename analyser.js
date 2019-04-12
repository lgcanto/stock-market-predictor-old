const deepai = require('deepai');

deepai.setApiKey('7cbaba1f-6200-474f-9398-b22c03b502f2');

async function start(){
  var resp = await deepai.callStandardApi("sentiment-analysis", {
    text: "Aeroporto de Guarulhos proíbe decolagens da Avianca por falta de pagamento",
  });
  console.log(resp);
}

start();