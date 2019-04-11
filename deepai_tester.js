// Get the 'deepai' package here (Compatible with browser & nodejs):
//     https://www.npmjs.com/package/deepai

// Example posting a text URL

const deepai = require('deepai'); // OR include deepai.min.js as a script tag in your HTML

// deepai.setApiKey('YOUR_API_KEY');
deepai.setApiKey('7cbaba1f-6200-474f-9398-b22c03b502f2');

var resp = await deepai.callStandardApi("sentiment-analysis", {
        // text: "YOUR_TEXT_URL",
        text: "Aeroporto de Guarulhos proíbe decolagens da Avianca por falta de pagamento",
});

console.log(resp);