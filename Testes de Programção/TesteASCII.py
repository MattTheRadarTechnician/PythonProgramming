#Este programa deve possibilitar enviar mensagens codificadas sem que alguém consiga lê-las.
#Caracteres que sejam letras minúsculas e maiúsculas devem ser deslocadas 3 posições para a direita, segundo a tabela ASCII
#A linha deverá ser invertida
#Todo e qualquer caractere a partir da metade em diante (truncada) devem ser deslocados uma posição para a esquerda na tabela ASCII

codigos = [] #Lista de entrada para codigos
N = int(input("Casos de teste: ")) #Numero de codigos que serao inseridos
casos = range(N) #Transformando em sequencia

#for para inputs correspondentes a numero de casos e adicionar `a lista de codigos
for c in casos: 
    word = input("Caso {} : ".format(c))
    codigos.append(word)

#for para que cada codigo inserido passe pelo processo de codificacao
for elem in codigos:
    A = []
    for x in elem:
        if x.isalpha(): #se x for do alfabeto
            value = ord(x) #value = valor numerico ASCII correspondente ao caracter
            trans = chr(value + 3) #trans = caracter ASCII correspondente a value 3 posicoes a frente na tabela ASCII
            A.append(trans) 
        else:
            A.append(x)

    A = A[::-1] #inverte a lista por meio de slicing syntax A[start:stop:step]
    L = len(A)
    #usa slicing syntax para dividir a lista A em duas listas respectivas as duas metades de A
    HalfA = A[0:L//2] #exemplo -> L = 9 --> [0:4] (// operador de floor)
    HalfAb = A[L//2:L] #exemplo -> L = 9 --> [4:9]

    for i, y in enumerate(HalfAb): #para cada elemento indexado da lista HalfAb
        valuey = ord(y)
        transy = chr(valuey - 1)
        HalfAb[i] = transy #o elemento de tal index eh substituido pelo valor de transy respectivo

    A = HalfA + HalfAb 
    Astring = ''.join(map(str,A)) #junta os elementos por meio do .join e os transforma em string por meio do map()
    print(Astring)