# Outlier mais conhecido como dados discrepantes, ou seja, qualquer coisa que esteja fora da distribuição normal.

# Vamos usar o metodo de intervalo interquartil para identificar os valores discrepantes (IQR).

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(900, 3))

quartis = (df.quantile([0.25, 0.75]))

print("O primeiro e terceiro quartil de todas as colunas:")
print(quartis, "\n")

Q1 = quartis[0][0.25]
Q3 = quartis[0][0.75]

IQR = Q3 - Q1

valor_inferior = (Q1 - (IQR * 1.5))
valor_superior = (Q3 + (IQR * 1.5))

print("Valor inferior:")
print(valor_inferior, "\n")

print("Valor superior:")
print(valor_superior, "\n")

out = df[0]

print("Valores fora do intervalo:")
print(out[(out < valor_inferior) | (out > valor_superior)])

print("\n")
print("Valores dentro do intervalo:")
print(out[(out >= valor_inferior) & (out <= valor_superior)])

print("\n")
print("Valores acima do intervalo:")
print(out[out > valor_superior])

print("\n")
print("Valores abaixo do intervalo:")
print(out[out < valor_inferior])

# Lidando com os valores discrepantes

out[(out < valor_inferior)] = valor_inferior
out[(out > valor_superior)] = valor_superior

print("\n")
print("Após o ajuste dos dados")
print("\n")
print("Valores acima do intervalo:")
print(out[out > valor_superior])

print("\n")
print("Valores abaixo do intervalo:")
print(out[out < valor_inferior])


