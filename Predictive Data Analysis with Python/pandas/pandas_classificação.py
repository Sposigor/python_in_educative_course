import pandas as pd
import numpy as np

# Vamos classificar o objeto series, usando o sort_index() e sort_values()
srs = pd.Series(np.random.randn(10)*100, index=np.arange(0, 10, 1))
print(srs.sort_index())
print(srs.sort_index(ascending=False))
print(srs.sort_values())
print(srs.sort_values(ascending=False))
# A classificação funciona em indices numericos, alfabetico e alfanumerico
# Numericos:
print("\nValores numericos aleatorios")
srs1 = pd.Series(np.random.randn(5))
print(srs1.sort_values())
print(srs1.sort_index())

# Alfabetico:
print("\nAlfabeticos")
srs2 = pd.Series(['D', 'A', 'E', 'C', 'B'])
print(srs2.sort_values())
print(srs2.sort_index())

# Alfanumerico:
print("\nAlfanumericos")
srs3 = pd.Series(['D', 'A', 'E', 'C', 'B'], index=['3', 'G', '4', '2', '1'])
print(srs3.sort_values())
print(srs3.sort_index())

# Usando função rank()
srs = pd.Series(np.random.randn(5))
print("\n Series")
print(srs)
# Usando o rank() para classificar os valores
print("\n rank antes da classificação")
print(srs.rank())
# Classificando os valores
srs = srs.sort_values()
# Usando o rank() para classificar os valores
print("\n rank depois da classificação")
print(srs.rank())
