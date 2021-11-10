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

