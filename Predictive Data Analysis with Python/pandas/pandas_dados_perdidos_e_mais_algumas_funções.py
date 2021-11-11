import pandas as pd
import numpy as np

# Dados ausentes, vamos usar dropna() para resolver o problema

null_val = np.nan

# Declarando objetos series com valores nulos
srs = pd.Series([1, 2, null_val, 4, null_val, 6]) # Series com dados ausentes
print("Series com valores nulos")
print(srs.isnull()) # verifica se os valores são nulos

# Declarando objetos DataFrame com valores nulos
df = pd.DataFrame([[1, 2, null_val], [null_val, 4, 5], [6, null_val, 8]])
print("\nDataFrame com valores nulos")
print(df.isnull()) # verifica se os valores são nulos

# Usando dropna para remover os dados ausentes
print("\nUsando dropna para remover os dados ausentes")
print(df.dropna()) # remover os dados ausentes

print("\nO dropna how = all:")
print(df.dropna(how='all')) # excluir as linhas aondes todos os valores são nulos

print("\nO dropna how = any:")
print(df.dropna(how='any')) # excluir as linhas aondes algum valor é nulo

print("\nO dropna thresh = n:")
print(df.dropna(thresh=2)) # excluir as linhas aondes mais de n valores são nulos

print("\nO dropna axis:")
print(df.dropna(axis=1)) # excluir as colunas aondes todos os valores são nulos
print(df.dropna(axis=1, how='all')) # excluir as colunas aondes todos os valores são nulos
print(df.dropna(axis=1, how='any')) # excluir as colunas aondes algum valor é nulo
print(df.dropna(axis=1, thresh=2)) # excluir as colunas aondes mais de n valores são nulos
print(df.dropna(axis=1, thresh=2, how='all')) # excluir as colunas aondes mais de n valores são nulos
print(df.dropna(axis=1, thresh=2, how='any')) # excluir as colunas aondes mais de n valores são nulos
print(df.dropna(axis=0, thresh=2, how='any')) # excluir as linhas aondes mais de n valores são nulos

# Usando fillna para preencher os dados ausentes
print("\nUsando fillna para preencher os dados ausentes")
print(df.fillna(0)) # preencher os dados ausentes com 0

# Mais algumas funções do pandas
# declarando o objeto dataframe
df = pd.DataFrame(np.arange(9).reshape(3,3), index=['A', 'B', 'C'], columns=['A', 'B', 'C'])

print("\nDataFrame")
print(df)

# Soma de cada coluna
print("\nSoma de cada coluna")
print(df.sum(axis=0))

# Soma de cada linha
print("\nSoma de cada linha")
print(df.sum(axis=1))

# Média de cada coluna
print("\nMédia de cada coluna")
print(df.mean(axis=0))

# Média de cada linha
print("\nMédia de cada linha")
print(df.mean(axis=1))

# Minimo de cada coluna
print("\nMinimo de cada coluna")
print(df.min(axis=0))

# Minimo de cada linha
print("\nMinimo de cada linha")
print(df.min(axis=1))

# Valor minimo em cada coluna está em qual linha
print("\nValor minimo em cada coluna está em qual linha")
print(df.idxmin(axis=0))

# Valor minimo em cada linha está em qual linha
print("\nValor minimo em cada linha está em qual linha")
print(df.idxmin(axis=1))

