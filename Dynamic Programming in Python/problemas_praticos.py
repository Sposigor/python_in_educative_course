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
