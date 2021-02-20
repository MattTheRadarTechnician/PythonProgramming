# dividir as figurinhas de cada um em pilhas do mesmo tamanho, no maior tamanho que fosse possível para ambos.
#Por exemplo, se Ricardo e Vicente --> respectivamente 8 e 12 figuras, ambos dividiam todas as suas figuras em pilhas de 4 figuras (Ricardo teria 2 pilhas e Vicente teria 3 pilhas)
# primeira linha da entrada contém um único inteiro N (1 ≤ N ≤ 3000), indicando o número de casos de teste
#Cada caso de teste contém 2 inteiros F1 (1 ≤ F1 ≤ 1000) e F2 (1 ≤ F2 ≤ 1000) indicando, respectivamente, a quantidade de figurinhas que Ricardo e Vicente têm 
#Para cada caso de teste de entrada haverá um valor na saída, representando o tamanho máximo da pilha de figurinhas que poderia ser trocada entre dois jogadores.

import math

#Entrada
N = int(input("Number of exchanges: "))#Numero de trocas

#Map function estabelece uma funcao para cada elemento de um iterable. Funcao Original: map(fun, iter)
R = list(map(int,input("Figurinhas do Ricardo : ").split()))[:N] #[:N] estabelece a length da lista. Comando original: x[0:len(x):1]   
#Formando listas pelo input 
V = list(map(int,input("Figurinhas do Vicente : ").split()))[:N] 
#Para todo numero index de uma lista gcd para o mesmo index da outra lista pelo decorrer da length de R
for i in range(len(R)):
    print(math.gcd(R[i], V[i]))


