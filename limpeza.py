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
#Transformar em log para ver no grafico


#%%
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 5))

plt.hist(dados, edgecolor='black')
plt.title('Distribuição Original (Assimétrica)')
plt.xlabel('Preço')