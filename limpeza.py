#%%
import pandas as pd
import numpy as np

dados = pd.read_csv('titanic.csv')
#%%
dados['Age'].isnull().sum()
dados['Age'] = dados['Age'].fillna(27)
dados.Age.unique()
dados['Age'] = dados['Age'].astype(int)

#%%
dados_cabine = dados[dados['Cabin'].notna()] .copy()
dados_cabine
#%%
dados.drop(['Cabin'], axis=1, inplace=True)
#%%
import numpy as np
dados['tamanho_familia'] = dados['SibSp'] + dados['Parch'] + 1 #Criando uma coluna com o tamanho da familia
dados['Fare_por_pessoa'] = dados['Fare'] / dados['tamanho_famailia'] #criando uma coluna com a taxa por pessoa

#%%
#Analisar a variancia entre as taxas, qual a menor a maior e quanto varia
dados_taxa = dados[['tamanho_familia','Fare_por_pessoa']].copy()
#%%
dados[['Name','Sex']] = dados[['Name','Sex']].apply(lambda x: x.str.upper())
dados.columns = dados.columns.str.upper()
dados
