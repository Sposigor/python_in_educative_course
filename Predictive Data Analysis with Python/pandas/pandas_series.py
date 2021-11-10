import pandas as pd

# Criando series com dados aleatórios
srs = pd.Series([1, 2, 3, 4, 5])

# Impressão dos valores da series
print("Valores da series pandas:") # Impressão dos valores da series
print(srs.values)

# Impressão dos indices da series
print("\nOs valores indices são:")
print(srs.index.values) 


# Definir a series com valores e indices
srs = pd.Series([11.9, 36.0, 16.6, 21.8, 34.2], index = ['China', 'India', 'EUA', 'Brasil', 'Argentina'])

# Nomeando a series
srs.name = "Taxa de crescimento"

# Nomeando os indices
srs.index.name = "Pais"

# Monstrando os valores e indices da series
print("Os valores das series indexadas são:")
print(srs)


# Definindo duas series objeto
srs1 = pd.Series([11.9, 36.0, 16.6, 21.8, 34.2, 62.4], index = ['China', 'India', 'EUA', 'Brasil', 'Argentina', 'Nigeria'])
srs2 = pd.Series([2.33, 11.9, 36.0, 16.6, 21.8, 34.2], index = ['Afghanistan', 'China', 'India', 'EUA', 'Brasil', 'Argentina'])

# Dividindo uma series por outra
srs = srs1 / srs2

# Nome da series
srs.name = "Resultado"

# Nome do index
srs.index.name = "Pais"

# Resultado dos valores
print("Resultado:") # Alguns valores da series ficaram com valores nulos, por não ter correspondência com os indices da outra series
print(srs) # Os valores 1.0 são por ter encontrado a correspondecia dos valores da primeira series com os indices da segunda series

print("\nOs indices Verdadeiros são nulos?")
print(pd.isnull(srs))

print("\nOs indices Verdadeiros não são nulos?")
print(pd.notnull(srs))

print("\nOs indices que são == 1.0:")
print(srs[srs == 1.0])

print("\nOs indices que são != 1.0:")
print(srs[srs != 1.0])