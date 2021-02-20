a = int(input("First Number. "))  #input de primeiro numero
b = int(input("Second Number. ")) #input de segundo numero
r=a%b #modulus ou restante da divisao de a e b
while r: #enquanto r nao for zero
    a=b #o valor de a se torna o de b
    b=r #o valor de b se torna o de r
    r=a%b #modulus ou restante da divisao de reestabelecidos a e b
print('GCD is:', b) #quando r == 0:

#Simulacao
a = 5
b = 10
r=a%b --> r = 5
while r:
    a=10
    b=5
    r=a%b --> r = 0
print('GCD is:', b)