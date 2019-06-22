import main
import pandas as pd # processamento de dados, leitura de arquivos .csv

acaoEmpresa = 'VALE3'
nomesEmpresa = main.df_empresas[main.df_empresas.code == acaoEmpresa].names.max()

# filtrando índices para obtermos apenas o papel em questão e ordenando por data
df_bovespa = main.df_bovespa[main.df_bovespa.codneg.str.strip() == acaoEmpresa]
df_bovespa.sort_values('date')
# criando coluna de classificação
df_bovespa['class'] = df_bovespa.apply(lambda row: main.defineClass(row['open'], row['close']), axis=1)

# filtrando notícias contendo nomes associadas à ação e ordenando por data
df_artigos = main.df_artigos[main.df_artigos.title.str.contains(nomesEmpresa)]
df_artigos.sort_values('date')
# criando coluna de data de efeito
df_artigos['effect_date'] = df_artigos.apply(lambda row: main.defineEffectDate(row['date']), axis=1)
# renomeando coluna de data para facilitar junção de datasets
df_bovespa = df_bovespa.rename(columns={'date': 'effect_date'})

df = pd.merge(df_artigos, df_bovespa, on='effect_date', how='left')