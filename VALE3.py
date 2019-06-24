import main
import pandas as pd # processamento de dados, leitura de arquivos .csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

acaoEmpresa = 'VALE3'
nomesEmpresa = main.df_empresas[main.df_empresas.code == acaoEmpresa].names.max()

# filtrando indices para obtermos apenas o papel em questao e ordenando por data
df_bovespa = main.df_bovespa[main.df_bovespa.codneg.str.strip() == acaoEmpresa]
df_bovespa.sort_values('date')
# criando coluna de classificacao
df_bovespa['classification'] = df_bovespa.apply(lambda row: main.defineClass(row['open'], row['close']), axis=1)

# filtrando noticias contendo nomes associadas a acao, filtrando caracteres e ordenando por data
df_artigos = main.df_artigos[main.df_artigos.news.str.contains(nomesEmpresa)]
df_artigos['news'] = df_artigos.apply(lambda row: main.applyRegexp(row['news']), axis=1)
df_artigos.sort_values('date')
# criando coluna de data de efeito
df_artigos['effect_date'] = df_artigos.apply(lambda row: main.defineEffectDate(row['date']), axis=1)
# renomeando coluna de data para facilitar juncao de datasets
df_bovespa = df_bovespa.rename(columns={'date': 'effect_date'})

# juncao do dataset de noticias com dataset de indices; criacao do dataset
df = pd.merge(df_artigos, df_bovespa, on='effect_date', how='left')
train_unused_columns = ['date', 'effect_date', 'codneg', 'company', 'open', 'close']
df.drop(train_unused_columns, inplace=True, axis=1)

X_verbal = df.news.tolist()
Y = df.classification.tolist()

# transformando a contagem de palavras em features
cv = CountVectorizer(binary=True)
cv.fit(X_verbal)
X = cv.transform(X_verbal)

# dividindo dataset entre treino (75%) e teste (25%)
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, train_size = 0.75
)

# verificando melhor valor de C (hiperparametro de regularizacao)
for c in [0.01, 0.05, 0.25, 0.5, 1]:
    
    lr = LogisticRegression(C=c)
    lr.fit(X_train, Y_train)
    print ("Acur�cia para C=%s: %s" 
           % (c, accuracy_score(Y_test, lr.predict(X_test))))
    
# definicao do modelo final
modelo = LogisticRegression(C=0.5)
modelo.fit(X_train, Y_train)
print ("Acur�cia final: %s" 
       % accuracy_score(Y_test, modelo.predict(X_test)))