import pandas as pd

# Pandas DataFrame
# Leitura em csv com separação por virgula
df = pd.read_csv(r"C:\Users\IgorD\Desktop\python_educative\python_educative\Predictive Data Analysis with Python\pandas\cancer_stats.csv", sep=",")
print(df.head()) # Exibe as 5 primeiras linhas
print(df.tail()) # Exibe as 5 últimas linhas

# Colunas

print(df.columns) # Exibe as colunas
print("\nPrimeira coluna") 
print(df['Sex'].head()) # Exibe as 5 primeiras linhas da coluna Sex
print("\n Tipo da coluna é:" + str(type(df['Sex'])) + "\n") # Quando separamos o DataFrame por colunas ela se torna objetos series

print("\nSegunda Coluna")
print(df['Under 1'].head()) # Exibe as 5 primeiras linha da coluna Under 1
print("\n Tipo da coluna é:" + str(type(df['Under 1'])) + "\n") # Quando separamos o DataFrame por colunas ela se torna objetos series

print("\nUltima Coluna do DF")
print(df['40-44'].head()) # Exibe as 5 primeiras linha da coluna 40-44
print("\n Tipo da coluna é:" + str(type(df['40-44'])) + "\n")


# Novo DataFrame
df2 = pd.read_csv(r"C:\Users\IgorD\Desktop\python_educative\python_educative\Predictive Data Analysis with Python\pandas\test.csv", sep=",")
print(df2.columns) # Exibe as colunas
print(df2.head()) # Exibe as 5 primeiras linhas

# Gerando um DataFrame com a seleção de colunas
novo_df2 = pd.DataFrame(df2, columns=['Sex', 'Under 1', '40-44'])
print(novo_df2.head())

# Usando a função loc[n] para buscar dados de linha no indice n, lembrando que por padrão o indice do DataFrame começa com 0
print("\nO valores da linha de indice 0")
print(df.loc[0])

print("\nO valores da linha de indice 1")
print(df.loc[1])

print("\nO valores da linha de indice 15")
print(df.loc[15])

# Lidando com valores nulos "NaN"
novo_df2 = pd.DataFrame(df2, columns=['Sex', 'Under 1', '40-44', 'Disease']) # Adicionei uma coluna doença no dataframe original, gerando assim os valores "NaN"
print("\n Dataframe sem o tratamento do NaN")
print(novo_df2.head())

# Para corrigir isso vou atribuir um string para a coluna nova
novo_df2['Disease'] = "Linfoma" # Atribuição de valores para a coluna
print("\n Dataframe com o tratamento do NaN")
print(novo_df2.head())

# Vamos fazer com outro exemplo
novo_df3 = pd.DataFrame(df2, columns=['Sex', 'Under 1', '40-44', 'ID'])
# Vou importar o numpy para usar a função de geração randomica
import numpy as np
novo_df3['ID'] = np.arange(novo_df3.shape[0])
print("\n Novo Dataframe")
print(novo_df3.head())

# Para mais conteudo sobre o DataFrame, acesse o link: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html



