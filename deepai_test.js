const deepai = require('deepai');
deepai.setApiKey('7cbaba1f-6200-474f-9398-b22c03b502f2');

async function start(){
  var resp = await deepai.callStandardApi("sentiment-analysis", {
    text: "Associação denuncia Rede\/Itaú ao Cade por venda casada e prática predatória\",\"A Abipag (Associação Brasileira de Instituições de Pagamentos), entrou com uma representação no Cade (Conselho Administrativo de Defesa Econômica) contra o Itaú Unibanco e sua operadora de máquinas de cartões Rede por retaliação, venda casada e subsídio cruzado, com objetivos predatórios no mercado."
  });
  console.log(resp.output[0]);
}

start();