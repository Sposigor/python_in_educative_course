import numpy as np

array = np.array([[-3, 0, 5, -6], [7, 2, -1, 9], [12, -4, 3, 1]])

def getMinMax(arr):
    
    res = []
    
    for i in range(arr.shape[0]): # Anda por cada linha
        res.append(arr[i].min()) # Armazena o menor valor da linha
        res.append(arr[i].max()) # Armazena o maior valor da linha
    
    return res

# Teste do codigo
arr = np.random.randint(1,100, size=(5,5))

print("Array Original:")
print(arr)

res_arr = getMinMax(arr)

print("\nResultado dos valores minimos e maximos:")
print(res_arr)
