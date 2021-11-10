import numpy as np

# Funções de processamento de matrizes

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

boleano = np.array([True, False, True, False]) # True = 1, False = 0

res = np.where(boleano, arr1, arr2) # Se boleano = True, retorna arr1, se False, retorna arr2
print(res)

# np.where é uma excelente alternativa para o if/else, em relação as matrizes

# Declare 2 arrays of different types
arr1 = np.random.rand(7)
arr2 = np.array(['Cão', 'Gato', 'Formiga', 'Pit', 'Aguia', 'Baleia', 'Formiga'])

print("Array originaç")
print(arr1)

print("\nMédia dos elementos")
print(arr1.mean())

print("\nVariânça dos elementos")
print(arr1.var())

print("\nPadrão de desvio")
print(arr1.std())

print("\nSoma")
print(arr1.sum())

print("\nClassificador")
arr1.sort()
print(arr1)

print("\nArray Original")
print(arr2)

print("\nArray unico")
print(np.unique(arr2))

# Mais algumas funções de processamento de matrizes https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.math.html

# Salvar e carregar matrizes

arr1 = np.random.randn(7)

print("\nArray original")
print(arr1)

np.save("array", arr1) # Salvando o array, é salvo no formato .npy
arr2 = np.load("array.npy") # Carregango o array

print("\nCarrega matriz")
print(arr2)

