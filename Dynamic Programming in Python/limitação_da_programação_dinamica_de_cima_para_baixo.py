# Como já foi abordado o problema de memoria nas soluções de recursão usando as soluções de programação dinâmica e memorização.
# A memoria continua sendo um recurso que devemos preserva.

# Tabulação um metodo de baixo para cima

# Recursão simples:
print(f'Rercusão Simples')
def Fatorial(n):
    if n == 0:  # caso 1
        return 1
    return n * Fatorial(n-1) # recursão
print(Fatorial(30))


# Usando tabulação para resolver o problema:
print(f"\n", 'Rercusão com Tabulação')
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
print(f"\n", 'Rercusão com Tabulação')
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
print(f"\n", 'Rercusão com Tabulação Otimizada')
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
print(f"\n", 'Rercusão Simples')
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
print(f"\n", 'Rercusão com Memorização')
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
print(f"\n", 'Rercusão com Tabulação')
def catalãoT(n):
    tabela = [None] * (n+1)
    tabela[0] = 1
    for i in range(1,n+1):
        tabela[i] = 0
        for j in range(i):    
            tabela[i] += (tabela[j] * tabela[i-j-1])
    return tabela[n]         
print(catalãoT(1000))


# Desafio substring mais longa
import random
import string

# Recursão simples:
print(f"\n", 'Rercusão Simples')
def procura(str1, str2, i, j, contagem):
    # base 1
    if i >= len(str1) or j >= len(str2):  
        return contagem
    # Interação
    if str1[i] == str2[j]:     
        contagem = procura(str1, str2, i+1, j+1, contagem+1)
    # Comparação do tamanho da substring mais longa
    return max(contagem, procura(str1, str2, i+1, j, 0), procura(str1, str2, i, j+1, 0))

def procura1(str1, str2):
    return procura(str1, str2, 0, 0, 0)

st1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
st2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
print(procura1(st1, st2+st1))


# Memorização:
print(f"\n", 'Rercusão com Memorização')
def procura_M(str1, str2, i, j, contagem, memo):
    # base 1
    if i >= len(str1) or j >= len(str2):  
        return contagem
    # Validação da memorização
    if (i, j, contagem) in memo:       
        return memo[(i, j, contagem)]
    c = contagem
    # Interação
    if str1[i] == str2[j]:     
        c = procura_M(str1, str2, i+1, j+1, contagem+1, memo)
    # Compara o resultado
    # Memoriza o resultado
    memo[(i,j,contagem)] = max(c, procura_M(str1, str2, i+1, j, 0, memo), procura_M(str1, str2, i, j+1, 0, memo))
    # Retorna o resultado
    return memo[(i,j,contagem)]

def procura_M2(str1, str2):
    memo = {}
    return procura_M(str1, str2, 0, 0, 0, memo)

st1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(15))
st2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(20))
print(procura_M2(st1, st2+st1))

# Tabulação:
print(f"\n", 'Rercusão com Tabulação')
def procura_T(str1, str2):
    n = len(str1)   # tamnho da string 1
    m = len(str2)   # tamnho da string 2

    tabela = [[0 for j in range(m+1)] for i in range(n+1)]  # tabulação
    maiorTamanho = 0   # maior string encontrada

    for i in range(1, n+1): # interação
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]: # procura o elemento
                tabela[i][j] = tabela[i-1][j-1] + 1 # adicionar elementos na tabela
                maiorTamanho = max(maiorTamanho, tabela[i][j])  # Procura e substiuir o maior valor
            else:
                tabela[i][j] = 0 # Se não encontrar o elemento, zera a tabela
    return maiorTamanho

st1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(40))
st2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(50))
print(procura_T(st1, st2+st1))


# Tabulação Otimizada:
print(f"\n", 'Rercusão com Tabulação Otimizada')
def procura_T_O(str1, str2):
    n = len(str1)   # tamnho da string 1
    m = len(str2)   # tamnho da string 2

    dp = [0 for i in range(n+1)]  # tabulação
    MaiorTamanho = 0   # maior string encontrada

    for j in range(1, m+1): # interação
        essaLinha = [0 for i in range(n+1)] 
        for i in range(1, n+1):
            if str1[i-1] == str2[j-1]: 
                essaLinha[i] = dp[i-1] + 1 
                MaiorTamanho = max(MaiorTamanho, essaLinha[i]) 
            else:
                essaLinha[i] = 0
        dp = essaLinha 
    return MaiorTamanho

st1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(400))
st2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(600))
print(procura_T_O(st1, st2+st1))