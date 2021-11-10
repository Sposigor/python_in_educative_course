
# Importando a biblioteca numpy
import numpy as np
from numpy import array

# Criando array 1-dimensional (1D)
n_array = np.array([1, 2, 3, 4, 5])
print(n_array)

# Criando array 2-dimensional (2D)
n_array2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(n_array2)

# Lista de funções para criações de matrizes numpy
np.empty(int(2)) # Gera uma matriz 1-D vazia de tamanho dependendo do parâmetro n.
print(np.empty(int(2)))

np.ones(2) # Gera uma matriz 1-D de 1's de tamanho dependendo do parâmetro n.
print(np.ones(2))

np.zeros(2) # Gera uma matriz 1-D de 0's de tamanho dependendo do parâmetro n.
print(np.zeros(2))

np.eye(2) # Gera uma matriz identidade de tamanho dependendo do parâmetro n.
print(np.eye(2))

np.arange(1, 50, 2) # Gera um array de números inteiros de 1 até 10 com passo de 2.
print(np.arange(1, 50, 2))

# Indexando para uma matriz 1-D
ar = np.arange(0,10,1) # Gerar o array de 0 até 10 com passo de 1.
print("O Array")
print(ar)

print("\n Indice 5 do array") # Indice 5 do array
print(ar[5]) 

print("\n Intervalo de 0 a 6") # Intervalo de 0 a 6
print(ar[0:6]) # Busca elementos em um intervalo

ar[0:6] = 100 # Substitui elementos em um intervalo pelo valor definido
print("\n Array com elementos substituidos")
print(ar)

# Fatianção de matrizes
ar1 = np.arange(0, 25, 3) # Gerar o array de 0 até 25 com passo de 3.
print("Array 1-D")
print(ar1)

nova_ar1 = ar1[1:12] # Seleciona um intervalo da matriz
print("\n Novo array 1-D")
print(nova_ar1)

nova_ar2 = ar1[:] # Seleciona todos os elementos da matriz
print("\nA nova matriz com todos os elementos")
print(nova_ar2)

# Indexianção de matrizes 2-D
