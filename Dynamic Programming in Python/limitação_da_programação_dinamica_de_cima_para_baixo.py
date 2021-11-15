# Como já foi abordado o problema de memoria nas soluções de recursão usando as soluções de programação dinâmica e memorização.
# A memoria continua sendo um recurso que devemos preserva.

# Tabulação um metodo de baixo para cima

# Recursão simples:
def Fatorial(n):
    if n == 0:  # caso 1
        return 1
    return n * Fatorial(n-1) # recursão

print(Fatorial(30))

# Usando tabulação para resolver o problema:
def Fatorial2(n):
    # Tabela de fatorial de tamanho n +1
    tabela = [0] * (n+1)
    # caso base de 0! = 1
    tabela [0] = 1
    # interagi até n
    for i in range(1, n+1):
        # Usando a resposta da tabela para calcular o fatorial de i
        tabela[i] = tabela[i-1] * i
    return tabela[n]

print(Fatorial2(30))

# Bom já vimos fibonacci em recursão simples, memorização, programação dinâmica e agoras iremos resolver em tabulação.

def fib(n):
    
    # base do fibonacci
    if n == 0: # caso base 1
        return 0
    if n == 1: # caso base 2
        return 1
    
    # Tabela
    tabela = [None] * (n+1) 
    tabela[0] = 0 # caso base do fibonacci 1
    tabela[1] = 1 # caso base do fibonacci 2
    
    # Interagindo até n
    for i in range(2, n+1):  
        # Encontrando os resultados e armazenando
        tabela[i] = tabela[i-1] + tabela[i-2]  
    # retornando o resultado procurado
    return tabela[n]    

print(fib(5))

# Vamos verificar uma solução da tabulação mais otimizada para o caso:
def fib2(n):
    if n == 0: # caso base 1
        return 0
    if n == 1: # caso base 2
        return 1
    
    # armazenando os resultados
    penultimo = 0 # penultimo elemento
    ultimo = 1 # ultimo elemento
    atual = None # elemento inicial
    
    # Interagindo até n
    for i in range(2, n+1):
        # Encontrando os resultados e armazenando
        atual = penultimo + ultimo
        penultimo = ultimo
        ultimo = atual
    # retornando o resultado procurado
    return atual

print(fib2(5))


# Desafio o numeros catalões
# Recursão simples:
def catalão(n):
    if n == 0: # base 1
        return 1
    soma = 0
    # Interação até n
    for i in range(n):  
      soma += (catalão(i) * catalão(n-1-i))  # C(i)*C(n-1-i)
    return soma
print(catalão(4))

# Memorização:
def catalão_memo(n, memo):
    if n == 0: # base 1
        return 1
    elif n in memo:
        return memo[n]
    soma = 0
    for i in range(n):
        soma += (catalão_memo(i, memo) * catalão_memo(n-1-i, memo)) # C(i)*C(n-1-i)
    memo[n] = soma
    return memo[n]

def catalão2(n):
    memo = {}
    return catalão_memo(n, memo)
print(catalão2(400))

# Tabulação:
def catalãoT(n):
    tabela = [None] * (n+1)
    tabela[0] = 1
    for i in range(1,n+1):
        tabela[i] = 0
        for j in range(i):    
            tabela[i] += (tabela[j] * tabela[i-j-1])
    return tabela[n]         

print(catalãoT(1000))