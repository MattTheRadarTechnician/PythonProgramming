import random #para randomizar no randint()
import sys #bonus do nicolas para argv

def diceroller(dicelist):
    DiceRoll = []    #lista de resultados de cada roll do input
    DiceNumber = 0   #numero de jogadas de dado
    DiceSides = 0    #numero de faces de dado
    DiceSum = 0      #soma dos rolls 
    DiceResults = [] #resultado da soma dos rolls em forma de lista
    dicelist = dicelist.split() #transforma o argumento dado em lista
    for i, dicecall in enumerate(dicelist): #i eh index para que o enumerate possa enumerar os elementos da lista
        DiceNumber = 0
        DiceSides = 0
        DiceSum = 0
        #Splitando a lista dicelist[i] formada pela enumeraçao da lista dicelist
        dicelist[i] = dicelist[i].split('d')
        #Da camada dicelist[i] quero o elemento [x]
        DiceNumber = int(dicelist[i][0])
        DiceSides = int(dicelist[i][1])
        #Para cada numero em todas as jogadas de dado
        for number in range(DiceNumber):
            Rolls = random.randint(1, DiceSides) # Cada roll
            DiceSum += Rolls #Soma dos rolls
            DiceRoll.append(str(Rolls)) #lista de rolls
        DiceResults.append(str(DiceSum)) #lista de soma
        DiceResults = "".join(DiceResults) #transformando em string pura pq aparentemente A FUNCAO STR NAO TRANSFORMA EM STRING MAS EM UMA LISTA DE STRING ??????? VTNC 
        DiceRoll = " ".join(DiceRoll) #mesma coisa
        Bonus = [DiceResults, DiceRoll] #Dicionario pra retornar com join de ":" entre os elementos
    return ":".join(Bonus)
#print(diceroller("5d12 6d4 1d2 1d8 3d6 4d20 100d100")) sem o bonus do nicolas de fazer como system argument
#para todo argumento nos argumentos do sistema alem do primeiro:
for arg in sys.argv[1:]:
    print(diceroller(arg))
   






