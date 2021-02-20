#Entrada 80 150 3 10 100 160 Saída 1
#Entrada 80 150 3 80 100 150 Saída 3
#Entrada 2 199 5 2 1 200 199 1 Saída 2

#alturas do corpo do maluco e transformando string em int e estabelecendo variavel para contar socos validos.
Entrada_C = int(input('C'))
Entrada_P = int(input('P'))
Entrada_S = int(input('S'))
Socos_validos = 0

#alturas dos socos e transformando string em lista
A = input('Altura dos socos.')
A = A.split()
#verificando se length de lista A eh igual ao numero de socos S
if len(A) != Entrada_S:
    A = input('Número de alturas não corresponde ao número de socos. Tente novamente!')
#verificando se altura colocada eh valida 
for altura in A:
    if int(altura) <= Entrada_P and int(altura) >= Entrada_C:
        Socos_validos += 1
#printando resultado  
print(Socos_validos)






