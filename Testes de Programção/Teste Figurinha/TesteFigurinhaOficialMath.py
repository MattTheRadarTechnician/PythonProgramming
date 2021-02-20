# dividir as figurinhas de cada um em pilhas do mesmo tamanho, no maior tamanho que fosse possível para ambos.
#Por exemplo, se Ricardo e Vicente --> respectivamente 8 e 12 figuras, ambos dividiam todas as suas figuras em pilhas de 4 figuras (Ricardo teria 2 pilhas e Vicente teria 3 pilhas)
# primeira linha da entrada contém um único inteiro N (1 ≤ N ≤ 3000), indicando o número de casos de teste
#Cada caso de teste contém 2 inteiros F1 (1 ≤ F1 ≤ 1000) e F2 (1 ≤ F2 ≤ 1000) indicando, respectivamente, a quantidade de figurinhas que Ricardo e Vicente têm 
#Para cada caso de teste de entrada haverá um valor na saída, representando o tamanho máximo da pilha de figurinhas que poderia ser trocada entre dois jogadores.



import math #modulo de matematica para funcao gcd() --> Greater Common Divisor
R = [] #Estabelecendo lista de figurinhas do Ricardo
V = [] #Estabelecendo lista de figurinhas do Vicente
N = int(input("Numero de casos: ")) #Numero de casos 
cases = range(N) #Estabelecendo sequencia de numeros do tamanho do numero de casos para usar no for
for x in cases: #Para cada numero na sequencia de numeros N
    print("Caso", x, ":")
    elem = [] #Estabelecendo lista de elementos dados no input
    elem = input().split() #Splitando elementos para separa-los em duas listas diferentes
    R.append(int(elem[0])) #Adicionando elementos de elem para as listas novas
    V.append(int(elem[1])) #Adicionando elementos de elem para as listas novas
for i in range(len(R)): #Para cada numero index no range do tamanho de R 
    print("Pilhas do Caso", i, ":", math.gcd(R[i], V[i])) #Calcula o gdc() dos elementos das duas listas correspondentes ao index 
