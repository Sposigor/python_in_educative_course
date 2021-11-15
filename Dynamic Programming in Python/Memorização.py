# Memorizaçãorização ou Memorizaçãoization, sem o r mesmo é basicamente armazenar informações para que não ocorra a mesma operação repetida.
# The act of storing results of costly function call, and retrieving them from the store when needed again to avoid re-evaluation.

# O caminho do Memorizaçãoization é através de hash table, que é uma estrutura de dados que armazena chave e valor.
# Exemplos:
# Dicionarios para armazenar chave e valor
Dicionario = {}

Chave = 1
Valor = "abcd"

# Adicionar a chave e valor ao dicionario
Dicionario[Chave] = Valor
Dicionario[2] = "abc"

# È possível acessar o valor através da chave ou de classes especificas
Dicionario["hello"] = "hi"
Dicionario[1.1] = 1

# Classe especifica para armazenar chave e valor
class Dummy:
    def __init__(self, val):
        self.val = val

# Objeto da classe especifica
ObjetoClasse = Dummy(5)
Dicionario[ObjetoClasse] = 5

# E vamos interagir com o dicionario
for k, v in Dicionario.items():
    print (k,":",v)


# Usando o metodo de Memorização para otimizar o calculo do fibonacci
Memorização = {} # Dicionario de Memorização

def fib(n):
    
    if n == 0: # caso 1
        return 0
    if n == 1: # caso 2
        return 1
    elif n in Memorização: # Validando o resultado da chave
        return Memorização[n] # Retorna o valor da chave se já possuir
    else: # Passo recursivo
        Memorização[n] = fib(n-1) + fib(n-2) # armazena o valor no dicionario
    return Memorização[n] # retorna o valor procurado

print (fib(5))

# O problema da escada
# Temos que subir a escada de N pares de pés, e cada par de pés tem um peso de 1.
# Usando recursão simples para resolução do problema
def staircase(n, m):
    # caso 1
    if n == 0:    
        return 1
    ways = 0
    # Etapas de interação
    for i in range(1,m+1):  
        # Procurando o menor passo para subir a escada
        if i <= n:  
        # Passo recursivo           
            ways += staircase(n-i, m) 
    return ways

print(staircase(4,2))

# Usando memorização para otimizar o calculo do problema

def nthStair(n, m, memo):
    # caso 1
    if n == 0:    
        return 1
    # Memorização para evitar calculos repetidos
    if n in memo: 
        return memo[n]
    ways = 0
    # Etapas de interação
    for i in range(1,m+1):    
        # Procurando o menor passo para subir a escada
        if i <= n:           
            # Passo recursivo   
            ways += nthStair(n-i, m, memo) 
    # Memorizando o resultado antes da proxima etapa
    memo[n] = ways   
    return ways

def staircase2(n, m):
    memo = {}
    # Auxiliar a função para memorizar o passos
    return nthStair(n, m, memo) 

print(staircase2(100, 6))