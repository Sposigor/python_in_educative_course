import numpy as np

# Transposição de matriz numpy
# Criação matriz 2-D

arr = np.arange(0, 50, 1).reshape(10, 5) # Criação matriz 2-D
print("Matriz Original")
print(arr)

print("\nA matriz transposta")
print(arr.T) # Transposição de matriz ou matriz inversa, é possivel usar o .transpose()

# O reshape a primeira condição é a quantidade de linhas e a segunda condição é a quantidade de colunas

# Mais funções do array numpy

print("\n", np.exp(arr/100)) # exponencial de cada elemento da matriz

print("\n", np.sqrt(arr)) # raiz quadrada de cada elemento da matriz

print("\n", np.log(arr)) # logaritmo natural de cada elemento da matriz

print("\n", np.sin(arr)) # seno de cada elemento da matriz

print("\n", np.cos(arr)) # cosseno de cada elemento da matriz

print("\n", np.tan(arr)) # tangente de cada elemento da matriz

print("\n", np.arcsin(arr)) # seno inverso de cada elemento da matriz

print("\n", np.arccos(arr)) # cosseno inverso de cada elemento da matriz

print("\n", np.arctan(arr)) # tangente inverso de cada elemento da matriz

print("\n", np.sinh(arr)) # seno hiperbólico de cada elemento da matriz

print("\n", np.cosh(arr)) # cosseno hiperbólico de cada elemento da matriz

print("\n", np.tanh(arr)) # tangente hiperbólica de cada elemento da matriz

print("\n", np.arcsinh(arr)) # seno hiperbólico inverso de cada elemento da matriz

print("\n", np.arccosh(arr)) # cosseno hiperbólico inverso de cada elemento da matriz

print("\n", np.arctanh(arr)) # tangente hiperbólica inverso de cada elemento da matriz

print("\n", np.cbrt(arr)) # raiz cúbica de cada elemento da matriz


# As funções add e sub podem ser usadas para somar e subtrair matrizes quando as mesmas possuem o mesmo número de linhas e colunas
arr1 = np.arange(0, 50, 1).reshape(10, 5) # Criação matriz 2-D
print("\n", np.add(arr, arr1)) # soma de cada elemento da matriz
print("\n", np.subtract(arr, arr1)) # subtração de cada elemento da matriz

# Link com mais funções do array numpy: https://docs.scipy.org/doc/numpy/reference/routines.math.html