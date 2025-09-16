#%%
import pandas as pd
dados = pd.read_csv('titanic.csv')
#%%
dados.columns = dados.columns.str.upper()
dados['AGE'] = dados['AGE'].fillna(dados['AGE'].median())
dados['AGE'] = dados['AGE'].astype(int)
#%%
dados_cabine = dados[dados['CABIN'].notna()] .copy()

#%%
dados.drop(['CABIN'], axis=1, inplace=True)
#%%
dados['FARE'] = dados['FARE'].fillna(dados['FARE'].median())
#%%
dados['FAMILY_SIZE'] = dados['SIBSP'] + dados['PARCH'] + 1 #Criando uma coluna com o tamanho da familia
dados['FARE_PER_PERSON'] = dados['FARE'] / dados['FAMILY_SIZE'] #criando uma coluna com a taxa por pessoa

#%%
#Analisar a variancia entre as taxas, qual a menor a maior e quanto varia
dados_taxa = dados[['FAMILY_SIZE','FARE_PER_PERSON']].copy()
#%%
dados[['NAME','SEX']] = dados[['NAME','SEX']].apply(lambda x: x.str.upper())

#%%
#proximos passos criar uma coluna de faixas para o Fare
#Os nulos da coluna Age, pegar a mediana do masculino e Feminino
dados['FAIXAS_FARE'] = pd.qcut(dados['FARE'], q=4, labels=['BAIXO','MÉDIO','ALTO','MUITO ALTO'])
dados.info()