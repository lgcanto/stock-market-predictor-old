import re
import numpy as np # algebra linear
import pandas as pd # processamento de dados, leitura de arquivos .csv
from unicodedata import normalize

# expressoes regulares
REGEXP_ESPACO = re.compile("[.;:!\'?,\"()\[\]]")
REGEXP_VAZIO = re.compile("(\-)|(\/)")

## Extracao de Dados
df_empresas = pd.read_csv('datasets/company-codes.csv')
df_bovespa = pd.read_csv('datasets/kaggle/bovespa.csv')
df_artigos = pd.read_csv('datasets/kaggle/articles.csv')

## Funcoes

# definicao de estado de fechamento diario do papel
def defineClass (open, close):
    if close > open:
        return 1 # ocorreu valorizacao
    if open > close:
        return -1 # ocorreu desvalorizacao
    else:
        return 0 # nao houve mudanca de preco
    
# definicao de data de efeito da noticia (proxima data de funcionamento da B3 aos o lancamento da noti�cia)
def defineEffectDate (date):
    effectDate = date
    while (df_bovespa[df_bovespa.date == effectDate].size < 1):
        effectDate = effectDate + 1
    return effectDate

# remocao de caracteres desnecessarios do texto a ser processado
def applyRegexp (text):
    finalText = text
    finalText = REGEXP_ESPACO.sub(" ", finalText.lower().strip())
    finalText = REGEXP_VAZIO.sub("", finalText)
    finalText = normalize('NFKD', finalText).encode('ASCII', 'ignore').decode('ASCII')
    return finalText

## Processamento de Dados

# removendo colunas desnecessarias do dataset de noti�cias
artigos_unused_columns = ['text', 'category', 'subcategory', 'link']
df_artigos.drop(artigos_unused_columns, inplace=True, axis=1)
# renomeando coluna com do atributo escolhido como o texto a ser analisado
df_artigos.rename(columns={'title': 'news'}, inplace=True)
# formatando coluna de data da mesma forma que o dataset de i�ndices
df_artigos['date'] = df_artigos.apply(lambda row: np.int64(row['date'].replace('-', '')), axis=1)

# removendo colunas desnecessarias do dataset de i�ndices
bovespa_unused_columns = ['TypeReg', 'BDICode', 'MarketType', 'Spec', 'Prazot', 'Currency', 'Max', 'Min', 'Med', 'Preofc', 'Preofv', 'Totneg', 'Quatot']
df_bovespa.drop(bovespa_unused_columns, inplace=True, axis=1)
df_bovespa.columns = map(str.lower, df_bovespa.columns)
# filtrando indices para obtermos apenas indices de empresas do i�ndice Bovespa
df_bovespa = df_bovespa[df_bovespa.codneg.str.strip().isin(df_empresas.code)]
# removendo janela de tempo inferior que nao existe no dataset de noti�cias
df_bovespa = df_bovespa[df_bovespa.date >= df_artigos.date.min()]

# criando coluna de data de efeito
#df_artigos['effect_date'] = df_artigos.apply(lambda row: defineEffectDate(row), axis=1)