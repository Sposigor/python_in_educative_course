# Vamos falar sobre recursão e como otimizar o processo de recursão.

# Codigo para verificação
# Recursão direta

def func(str , n):
    if n > 0:
        print(f'Chamadas da função: {n}', '\n')
        func("func", n-1)

def main():
    func("main" , 7)

main()

# Recursão indereta
def func1(str, n):
    if n > 0:
        print (f'Chamadas da função: {n}', '\n')
        func2("func1", n-1)

def func2(str, n):
    if n > 0:
        print (f'Chamadas da função2: {n}', '\n')
        func1("func2", n-2)

def main():
    func1("main", 7)

main()

# Um exercicio de codificação 1:

str = "abacabada"
char = "a"

def countChar(str, char):
    if str == "":
        return 0
    elif str[0] == char:
        return 1 + countChar(str[1:], char)
    else:
        return countChar(str[1:], char)

print(countChar(str, char)) 


# Um exercicio de codificação 2:
# Sobre Fibonacci, sua formula é fib(n) = fib(n-1) + fib(n-2)

n = 5 # Quero saber o resultado do termo 5 da seQuencia de Fibonacci

def fib(n):
    if n == 0: # Se n for 0, retorna 0
        return 0
    elif n == 1: # Se n for 1, retorna 1
        return 1
    else:
        return fib(n-1) + fib(n-2) # Se n for maior Que 1, retorna a soma dos termos anteriores

print(fib(n))

# Apesar da simplicidade de resolução do problema é preciso lembrar Que a recursão é uma forma de otimização de processos.
# Porém nosso algoritmo pode sofrer com o custo de processamento.

# Um exercicio de codificação 3:
# Permutação de uma string

str = "abc"

def permutation(str):
    if str == "": # Se a string for vazia, retorna uma lista vazia
        return [""]
    permutes = []
    for char in str:
        subpermutes = permutation((str.replace(char, "", 1)))
        for each in subpermutes:
            permutes.append(char+each)
    return permutes

def main():
    print(permutation(("abc")))

main()

# Tabuleiro de xadrez
# Entrada
n = 4
Tabuleiro = ["----", 
        "----",
        "----",
        "----"
]


def isSafe(i, j, Tabuleiro):
    for c in range(len(Tabuleiro)):
        for r in range(len(Tabuleiro)):
            if Tabuleiro[c][r] == 'Q' and i==c and j!=r:
                return False
            elif Tabuleiro[c][r] == 'Q' and j==r and i!=c:
                return False
            elif (i+j == c+r or i-j == c-r) and Tabuleiro[c][r] == 'Q':
                return False
    return True

def nRainha(r, n, Tabuleiro):
    # base do case
    if r == n:
        return True, Tabuleiro
    # Verica linha por linha a posição da rainha
    for i in range(n):
        if isSafe(r, i, Tabuleiro):
        # Verifica se a posição da rainha é válida
            Tabuleiro[r][i] = 'Q'
            Avançar, novoTabuleiro = nRainha(r+1, n, Tabuleiro)
        # Se a posição da rainha for válida, continua a verificação
            if Avançar:
                return True, novoTabuleiro
        # Se a posição da rainha não for válida, retorna a posição anterior
        Tabuleiro[r][i] = '-'
    return False, Tabuleiro

def inserirRainha(n, Tabuleiro):
    return nRainha(0, n, Tabuleiro)[1]

def main():
    n = 4
    Tabuleiro = [["-" for _ in range(n)] for _ in range(n)]
    QTabuleiro = inserirRainha(n, Tabuleiro)
    QTabuleiro =  "\n".join(["".join(x) for x in QTabuleiro])
    print (QTabuleiro)
main()

