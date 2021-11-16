import numpy as np


# Desafio 1 - Numero de maneiras de representar N dolares
# Recursão Simples
print("Desafio 1 - Recursão Simples")
def contagem_(tipos, quantidade, maximo):
    if quantidade == 0: # caso base 1
        return 1
    ways = 0
    # interação
    for tipo in tipos:    
        # Seleção dos tipos
        if tipo <= maximo and quantidade - tipo >= 0:  
        # contagem dos tipos maximos    
            ways += contagem_(tipos, quantidade-tipo, tipo)  
    return ways

def contagem(tipos, quantidade):
    return contagem_(tipos, quantidade, max(tipos))

print(contagem([1,2,5], 5))

# Recursão Simples com outro ponto de vista
print("\nDesafio 1 - Recursão Simples com outro ponto de vista")
def contagem2_(tipos, quantidade, index):
    if quantidade == 0: # caso base 1
        return 1
    if quantidade < 0 or index >= len(tipos): # caso base 2
        return 0
    # contagem dos tipos maximos
    return contagem2_(tipos, quantidade - tipos[index], index) + contagem2_(tipos, quantidade, index+1)

def contagem2(tipos, quantidade):
    return contagem2_(tipos, quantidade, 0)

print(contagem2([1,2,5], 5))


# Recursão com Memoization
print("\nDesafio 1 - Recursão com Memoization")
def contagem3_(tipos, quantidade, maximo, memo):
    if quantidade == 0: # caso base 1
        return 1
    if quantidade < 0: # caso base 2
        return 0
    if (quantidade, maximo) in memo: # Verifica se já possui o resultado
        return memo[(quantidade, maximo)]
    ways = 0
    for tipo in tipos: # Interação
        # Seleção dos tipos
        if tipo <= maximo:     
        # contagem dos tipos maximos
            ways += contagem3_(tipos, quantidade-tipo, tipo, memo)  
    memo[(quantidade, maximo)] = ways # armazenamento dos resultados
    return ways

def contagem3(tipos, quantidade):
    memo = {}
    return contagem3_(tipos, quantidade, max(tipos), memo)

print(contagem3([1,2,5], 5))


# Recursão bottom-up
print("\nDesafio 1 - Recursão bottom-up")
def contagem4_(tipos, quantidade):
    if quantidade <= 0:
        return 0
    dp = [[1 for _ in range(len(tipos))] for _ in range(quantidade + 1)]
    for quan in range(1, quantidade+1):
        for j in range(len(tipos)):
            tipo = tipos[j]
        if quan - tipo >= 0:
            x = dp[quan - tipo][j]
        else:
            x = 0
        if j >= 1:
            y = dp[quan][j-1]
        else:
            y = 0
        dp[quan][j] = x + y
    return dp[quantidade][len(tipos) - 1]

print(contagem4_([1,2,5], 5))


# Recursão bottom-up com otimização
print("\nDesafio 1 - Recursão bottom-up com otimização")
def countways(tipos, quantidade):
    if quantidade <= 0:
        return 0
    dp = [1 for _ in range(quantidade + 1)]
    for j in range(len(tipos)):
        cont = [1 for _ in range(quantidade + 1)]
        for quant in range(1,quantidade + 1):
            tipo = tipos[j]
        if quant - tipo >= 0:
            x = cont[quant - tipo]
        else:
            x = 0
        if j >= 1:
            y = dp[quant]
        else:
            y = 0
        cont[quant] = x + y
    dp = cont
    return dp[quantidade]

print(countways([1,2,5], 5))


# Desafio 2: Corte da haste
print("\nDesafio 2: Corte da haste")
# Recursão Simples
print("\nDesafio 2 - Recursão Simples")
def corteH(n, preços):
    if n<0:
        return 0
    max_corte = 0
    for i in range(1,n+1):
        max_corte = max(max_corte, preços[i-1] + corteH(n - i, preços))
    return max_corte

print(corteH(3, [3,7,8]))


# Recursão Memoization
print("\nDesafio 2 - Recursão Memoization")
def corteH2(n, preços, memo):
    if n<0:
        return 0
    if n in memo:
        return memo[n]
    max_corte = 0
    for i in range(1,n+1):
        max_corte = max(max_corte, preços[i-1] + corteH2(n - i, preços, memo))
    memo[n] = max_corte
    return memo[n]

def corteH2_(n, preços):
    memo = {}
    return corteH2(n, preços, memo)

print(corteH2_(3, [3,7,8]))



# Recursão bottom-up
print("\nDesafio 2 - Recursão bottom-up")
def corteH3(n, preços):
    dp = [0 for _ in range(n+1)]
    for i in range(1,n+1):
        max_corte = 0
        for j in range(1,i+1):
            max_corte = max(max_corte, preços[j-1] + dp[i-j])
        dp[i] = max_corte
    return dp[n]

print(corteH3(3, [3,7,8]))


# Desafio 3: Problema com a programação ponderada
print("\nDesafio 3: Problema com a programação ponderada")
# Recursão Simples
print("\nDesafio 3 - Recursão Simples")
def ultimo_confl(index, modulo, eSorte = False):
    if not eSorte:
        modulo = sorted(modulo, key=lambda tup: tup[1])
    for i in range(index, -1, -1):
        if modulo[index][0] >= modulo[i][1]:
            return i
    return None

def RecursãoR(modulo, n):
    if n == None or n < 0:  # base case of conflict with the first event
        return 0
    if n == 0:              # base case of no conflict with the first event
        return modulo[n][2]
    
    # find max of keeping the n-th event or not keeping it
    return max(modulo[n][2] + RecursãoR(modulo, ultimo_confl(n, modulo, eSorte= True)), 
            RecursãoR(modulo, n-1))

def PesoModulo(modulo):
    
    modulo = sorted(modulo, key=lambda tup: tup[1])
    return RecursãoR(modulo, len(modulo)-1)

print(PesoModulo([(0, 2, 25), (1, 6, 40), (6, 9, 170), (3, 8, 220)]))


# Recursão Memoization
print("\nDesafio 3 - Recursão Memoization")
def ultimo_confl2(index, modulo, eSorte = False):
    if not eSorte:
        modulo = sorted(modulo, key=lambda tup: tup[1])
    for i in range(index, -1, -1):
        if modulo[index][0] >= modulo[i][1]:
            return i
    return None

def RecursãoR2(modulo, n, memo):
    if n == None or n < 0:
        return 0
    if n == 0:
        return modulo[n][2]
    if n in memo:
        return memo[n]
    memo[n] = max(modulo[n][2] + RecursãoR2(modulo, ultimo_confl2(n, modulo, eSorte= True), memo), 
            RecursãoR2(modulo, n-1, memo))
    return memo[n]

def peso_modulo2(modulo):
    modulo = sorted(modulo, key=lambda tup: tup[1])
    memo = {}
    return RecursãoR2(modulo, len(modulo)-1, memo)

print(peso_modulo2([(0, 2, 25), (1, 5, 40), (6, 8, 170), (3, 7, 220)]))
modulo = [(i,i+2,10) for i in range(100)]
print(peso_modulo2(modulo))


# Recursão bottom-up
def ultimo_confl3(index, modulo, eSorte = False):
    if not eSorte:
        modulo = sorted(modulo, key=lambda tup: tup[1])
    for i in range(index, -1, -1):
        if modulo[index][0] >= modulo[i][1]:
            return i
    return None

def peso_modulo3(modulo):
    modulo = sorted(modulo, key=lambda tup: tup[1])
    dp = [0 for _ in range(len(modulo)+1)]

    for i in range(1, len(modulo)+1):
        index_LC = ultimo_confl3(i-1, modulo, eSorte=True)
        if index_LC == None:
            index_LC = -1
        dp[i] = max(dp[i-1], dp[index_LC+1]+modulo[i-1][2])
    return dp[len(modulo)]

print(peso_modulo3([(0, 2, 25), (1, 5, 40), (6, 8, 170), (3, 7, 220)]))
modulo = [(i,i+2,10) for i in range(100)]
print(peso_modulo3(modulo))


# Desafio 4: Multiplicação da matriz
# Recursão Simples
print("\nDesafio 4: Multiplicação da matriz")
def minMultlipicador(foco):
    if len(foco) <= 2:
        return 0
    minimo = np.inf
    for i in range(1,len(foco)-1):
        minimo = min(minimo, minMultlipicador(foco[0:i+1]) + minMultlipicador(foco[i:]) +
                    foco[0] * foco[-1] * foco[i])
    return minimo

print(minMultlipicador([3, 3, 2, 1, 2]))


# Recursão simples com otimização de tempo
print("\nDesafio 4: Multiplicação da matriz - Recursão simples com otimização de tempo")
def minMultiplicador2(foco, i, j):
    if j-i <= 2:
        return 0
    minimo = np.inf
    for k in range(i+1, j-1):
        minimo = min(minimo, minMultiplicador2(foco, i, k+1) + minMultiplicador2(foco, k, j) +
                    foco[i]*foco[j-1]*foco[k])
    return minimo

def minMulti(foco):
    return minMultiplicador2(foco, 0, len(foco))

print(minMulti([3, 3, 2, 1, 2]))


# Recursão com memoization
print("\nDesafio 4: Multiplicação da matriz - Recursão com memoization")
def minMulti_(foco, i, j, memo):
    if j-i <= 2:
        return 0
    if (i,j) in memo:
        return memo[(i,j)]
    minimo = np.inf
    for k in range(i+1, j-1):
        minimo = min(minimo, minMulti_(foco, i, k+1, memo) + minMulti_(foco, k, j, memo) +
                    foco[i]*foco[j-1]*foco[k])
    memo[(i,j)] = minimo
    return minimo

def minMulti2(foco):
    memo = {}
    return minMulti_(foco, 0, len(foco), memo)

print(minMulti2([3, 3, 2, 1, 2]))


# Recursão bottom-up
print("\nDesafio 4: Multiplicação da matriz - Recursão bottom-up")
def min_Multi(foco):
    dp = [[0 for _ in range(len(foco))] for _ in range(len(foco))]
    for l in range(2,len(foco)):
        for i in range(1,len(foco)-l+1):
            j = i+l-1
            dp[i][j] = np.inf
            for k in range(i, j):
                temp = dp[i][k]+ dp[k+1][j] + foco[i-1]*foco[k]*foco[j]
                if temp < dp[i][j]:
                    dp[i][j] = temp
    return dp[1][-1]
print(min_Multi([3, 3, 2, 1, 2]))


# Desafio 5: O problema do viajante
print("\nDesafio 5: O problema do viajante")
# recursão simples
print("\nRecursão simples")
def Trajeto_M(Distancia, Verifica, index, Inicio):
    minimo = np.inf
    for i in range(len(Distancia)):
        if i != index and i != Inicio and i not in Verifica:
            Verifica[i] = 1
            minimo = min(minimo, Distancia[index][i]+Trajeto_M(Distancia, Verifica, i, Inicio))
            del Verifica[i]
    if minimo == np.inf:
        return Distancia[index][Inicio]
    return minimo

def Trajeto(Distancia):
    Verifica = {}
    minimo = np.inf
    for i in range(len(Distancia)):
        minimo = min(minimo, Trajeto_M(Distancia, Verifica, i, i))
    return minimo

print(Trajeto([
        [0, 10, 20],
        [12, 0, 10],
        [19, 11, 0],
]))