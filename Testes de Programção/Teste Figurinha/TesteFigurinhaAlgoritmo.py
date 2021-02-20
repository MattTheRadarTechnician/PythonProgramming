
def gcd(x, y): #Funcao de recursao para calcular maior divisor comum usando Euclidian Algorithm
    if x == 0:
        return y
    return gcd(y%x,x) #Funciona de forma que um dos numeros sempre seja divido pelo outro ate que o restante seja 0

R = [] 
V = [] 
N = int(input("Numero de casos: "))  
cases = range(N)
for t in cases:
    print("Caso", t, ":")
    elem = [] 
    elem = input().split() 
    R.append(int(elem[0])) 
    V.append(int(elem[1]))

for i in range(len(R)):
    a = R[i]
    b = V[i]
    print("pilhas do caso", i, ":", gcd(a,b))


