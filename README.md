# Stock Market Predictor

### Propose of a stock market predictor guided by market news.
- First attempt: extract news from Uol Market News (pt-BR) API (http://rss.uol.com.br/feed/economia.xml) and use DeepAI API (https://deepai.org/api-docs/?javascript#sentiment-analysis) to process and give the desired output

### Current guidelines:

- Install packages: 
```console
npm install
```

- Run extractor to get today's news: 
```console
node extractor.js
```

- Run analyser to process news and create output file: 
```console
node analyser.js
```

### TODO List (still updating):
- [ ] Identify company names/codes
- [ ] Replace DeepAI processing with local machine learning code