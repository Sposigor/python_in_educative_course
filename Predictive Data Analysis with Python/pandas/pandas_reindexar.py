import pandas as pd
import numpy as np

# Reidexando em series
# Definir a series com valores e indices
srs = pd.Series([11.9, 36.0, 16.6, 21.8, 34.2], index = ['China', 'India', 'EUA', 'Brasil', 'Argentina'])


# Nomeando a series
srs.name = "Taxa de crescimento"

# Nomeando os indices
srs.index.name = "Pais"

# Usando a função reindex para adicionar paises
srs2 = srs.reindex(['China', 'India', 'Mexico', 'USA', 'Brasil', 'Argentina', 'Espanha'])
print("Nova Series indexada sem tratar NaN:\n",srs2)
# Usando a função reindex para adicionar paises com o fill_value para tratar NaN
srs3 = srs.reindex(['China', 'India', 'Mexico', 'USA', 'Brasil', 'Argentina', 'Espanha'], fill_value=0)
print("\nNova Series indexada com tratamento do NaN:\n",srs3)


# Reidexando em dataframes
# Definir o dataframe com valores e indices
arr2d = np.arange(16).reshape(4,4) # 4 linhas e 4 colunas

# Usando o arr2d para atribuir valores ao dataframe
df = pd.DataFrame(arr2d, index=['A', 'B', 'C', 'D'], columns=['a', 'b', 'c', 'd'])
print("\nDataframe:\n",df)

df2 = df.reindex(['A', 'B', 'C', 'D', 'E', 'F'])
print("\nDataframe indexado as linhas:\n", df2)

df2 = df.reindex(['A', 'B', 'C', 'D', 'E', 'F'], fill_value=0)
print("\nDataframe indexado as linhas com tratamento do NaN:\n", df2)

df2 = df.reindex(columns=['a', 'b', 'c', 'd', 'e', 'f'])
print("\nDataframe indexado as colunas:\n", df2)

df2 = df.reindex(columns=['a', 'b', 'c', 'd', 'e', 'f'], fill_value=0)
print("\nDataframe indexado as colunas com tratamento do NaN:\n", df2)

# Preenchimento com base nos valores existentes da tabela, vamos usar o ffill() 
# Criando o objeto series
srs1 = pd.Series([11.9, 36.0, 16.6, 21.8, 34.2], index = ['China', 'India', 'USA', 'Brasil', 'Mexico'])
srs1.name = "Taxa de Crescimento"
srs1.index.name = "Pais"
# Reindexando a series sem transformar os valores NaN
srs2 = srs1.reindex(['China', 'India', 'Malasia', 'USA', 'Brasil', 'Mexico', 'Espanha'])
print("Serries com valores NaN:\n",srs2)
# Reindexando a series com transformar os valores NaN com ffill()
print("\nSeries com novos valores:\n",srs2.ffill())

# Criando o objeto dataframe
# Usando o arr2d para atribuir valores ao dataframe
df = pd.DataFrame(arr2d, index=['A', 'B', 'C', 'D'], columns=['a', 'b', 'c', 'd'])
# Reindexando o dataframe sem transformar os valores NaN
df2 = df.reindex(['A', 'B', 'C', 'D', 'E', 'F'])
df2 = df.reindex(columns=['a', 'b', 'c', 'd', 'e', 'f'])
print("DataFrame com valores NaN:\n", df2)

# Usando ffill() para preencher os valores NaN nas linhas
print("\nDataframe com novos valores na linha:\n", df2.ffill(axis = 0)) # No dataframe é necessario parametrizar o eixo, no caso axis = 0

# Usando ffill() para preencher os valores NaN na coluna
print("\nDataframe com novos calores na coluna:\n", df2.ffill(axis = 1)) # No dataframe é necessario parametrizar o eixo, no caso axis = 1

# Selecionar e descartar entradas nas series e dataframes
# Series
srs = pd.Series(np.arange(0, 6, 1), index = ['ind0', 'ind1', 'ind2', 'ind3', 'ind4', 'ind5'])
srs.index.name = "Index"
print("Serie Original:\n", srs)

print("\nSeries indexada com ind3:")
print(srs['ind3']) # indice ind3

print("\nSeries indice 3:")
print(srs[3]) # busca o elemento 3 do indice

print("\nSeries multiplos elementos do indice:\n")
print(srs[['ind1', 'ind4']]) # busca os elementos ind1 e ind4

print("\nSeries seleção após o elemento 4:\n", srs[4: ]) # Busca elementos no indice a partir do elemento 4

print("\nSeries seleção com condição:\n", srs[srs >= 3]) # Busca elementos no indice com valor maior ou igual a 3

srs = srs.drop('ind3') # Remove indice ind3
print("\nSerie com indice ind3 removido:\n", srs)

# DataFrame
df = pd.DataFrame(np.arange(12).reshape(4, 3), index = ['ind0', 'ind1', 'ind2', 'ind3'], columns = ['col0', 'col1', 'col2'])
print("\nElementos com a condição:\n", df[df['col2'] > 6]) # Busca elementos com valor maior que 6 na coluna Col2
print("\nElementos do indice 3:\n", df.loc['ind3']) # Busca elementos com indice 3

print("\nElementos com descarte do indice ind2", df.drop('ind2')) # Remove indice ind2
print("\nElementos com descarte da coluna col1", df.drop('col1', axis = 1)) # Remove coluna col1