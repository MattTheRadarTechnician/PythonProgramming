

def gcd(a, b): #Estabelecendo funcao
    if a == 0:
        return b
    return gcd(b%a,a)

gcd(10,5) #Primeira chamada
    if 10 == 0
        return 5
    return gcd(5%10, 10)

gcd(5,10) #Segunda chamada
    if 5 == 0
        return
    return gcd(10%5,5)

gcd(0,5) #Terceira chamada
    if 0 == 0
        return 5