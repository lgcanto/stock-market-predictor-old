import numpy as np # algébra linear
import pandas as pd # processamento de dados, leitura de arquivos .csv

## Extração de Dados
df_empresas = pd.read_csv('datasets/company-codes.csv')
df_bovespa = pd.read_csv('datasets/kaggle/bovespa.csv')
df_artigos = pd.read_csv('datasets/kaggle/articles.csv')

## Funções

# denifição de estado de fechamento diário do papel
def defineClass (open, close):
    if close > open:
        return 1 # ocorreu valorização
    if open > close:
        return -1 # ocorreu desvalorização
    else:
        return 0 # não houve mudança de preço
    
# definição de data de efeito da notícia (próxima data de funcionamento da B3 após o lançamento da notícia)
def defineEffectDate (date):
    effectDate = date
    while (df_bovespa[df_bovespa.date == effectDate].size < 1):
        effectDate = effectDate + 1
    return effectDate

## Processamento de Dados

# removendo colunas desnecessárias do dataset de notícias
artigos_unused_columns = ['text', 'category', 'subcategory', 'link']
df_artigos.drop(artigos_unused_columns, inplace=True, axis=1)
# formatando coluna de data da mesma forma que o dataset de índices
df_artigos['date'] = df_artigos.apply(lambda row: np.int64(row['date'].replace('-', '')), axis=1)

# removendo colunas desnecessárias do dataset de índices
bovespa_unused_columns = ['TypeReg', 'BDICode', 'MarketType', 'Spec', 'Prazot', 'Currency', 'Max', 'Min', 'Med', 'Preofc', 'Preofv', 'Totneg', 'Quatot']
df_bovespa.drop(bovespa_unused_columns, inplace=True, axis=1)
df_bovespa.columns = map(str.lower, df_bovespa.columns)
# filtrando índices para obtermos apenas índices de empresas do índice Bovespa
df_bovespa = df_bovespa[df_bovespa.codneg.str.strip().isin(df_empresas.code)]
# removendo janela de tempo inferior que não existe no dataset de notícias
df_bovespa = df_bovespa[df_bovespa.date >= df_artigos.date.min()]

# criando coluna de data de efeito
#df_artigos['effect_date'] = df_artigos.apply(lambda row: defineEffectDate(row), axis=1)