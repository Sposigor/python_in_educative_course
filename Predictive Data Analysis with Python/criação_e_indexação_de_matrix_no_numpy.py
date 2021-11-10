
# Importando a biblioteca numpy
import numpy as np
from numpy import array

# Criando array 1-dimensional (1D)
n_array = np.array([1, 2, 3, 4, 5])
print(n_array)
print("\n")

# Criando array 2-dimensional (2D)
n_array2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(n_array2)
print("\n")

# Lista de funções para criações de matrizes numpy
np.empty(int(2)) # Gera uma matriz 1-D vazia de tamanho dependendo do parâmetro n.
print(np.empty(int(2)))
print("\n")

np.ones(2) # Gera uma matriz 1-D de 1's de tamanho dependendo do parâmetro n.
print(np.ones(2))
print("\n")

np.zeros(2) # Gera uma matriz 1-D de 0's de tamanho dependendo do parâmetro n.
print(np.zeros(2))
print("\n")

np.eye(2) # Gera uma matriz identidade de tamanho dependendo do parâmetro n.
print(np.eye(2))
print("\n")

np.arange(1, 50, 2) # Gera um array de números inteiros de 1 até 10 com passo de 2.
print(np.arange(1, 50, 2))
print("\n")

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
arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # Criar matriz 2-D
print("Array 2-D")
print(arr3)

print("\n Elemento da linha 0 e coluna 1")
print(arr3[0][1]) # Elemento da linha 0 e coluna 1

print("\n Elementos em um intervalo das ultimas duas linhas e colunas")
print(arr3 [1:3, 1:3]) # Elementos em um intervalo das ultimas duas linhas e colunas

novo_arr3 = arr3[1:3, 1:3] # Seleciona um intervalo da matriz
print("\n Novo array 2-D")
print(novo_arr3)

# Nova matriz 2-D
arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Array")
print(arr4)

print("\nNovo corte da matriz")
print(arr4[1:3, 0:2])

print("\nSomente a coluna")
print(arr4[:, 1:2])

# Problema com a memoria do numpy (cache)

arr5 = np.arange(0, 100, 1)
print("\nArray 1-D")
print(arr5)

nova_arr5 = arr5[1:22]
print("\n Nova matriz fatiada")
print(nova_arr5)

nova_arr5[:] = 55
print("\n A Matriz original")
print(arr5) # A matriz original foi alterada

# Para resolver esse problema usamos a função copy()

arr6 = np.arange(0,10,1)
print("\nArray 1-D")
print(arr6)

new_arr6 = arr6[1:7].copy()
print("\nCorte da matriz original")
print(new_arr6)

new_arr6[:] = 20
print("\nMatriz Original")
print(arr6)

