#Qualidades das bebidas são Comum, Rara e Lendária
#Bebidas lendárias --> 2% de serem ganhas
#10 primeiras tentativas --> gratuitas
#Mais tentativas --> 5 cruzados cada
#A cada 10 tentativas --> uma tentativa a mais de graça
#A cada 31 tentativas --> bebida Lendária garantida.

#Dada o número de tentativas que o jogador consegue comprar, quanto ele gastou no jogo e quantas bebidas lendárias no mínimo ele conseguiu?
    #Número inteiro T representando a quantidade de tentativas que o jogador comprou (10<=T<=10000).
    #Primeira linha da saída é o valor C em cruzados que o jogador gastou no jogo (0<=C<=50000). A segunda linha da saída é o valor L representando a quantidade mínima de bebidas Lendárias obtidas (0<=L<=10000).
import math

T = int(input("Tentativas:")) #Quantidade de Tentativas pagas
Totais = (T + 10) + (T + 10)/10 #Quantidade de tentativas totais
C = T*5 #Quantidade Paga
L = math.floor(Totais/31) #Quantidade de tentativas com Lendaria garantida. L = minimo de lendarias. Drop rate nao entra ja que eh o caso de nao ter dropado nada alem do garantido
#PL = int((Totais - Tent_Lend)*2/100) --> probabilidade de lendaria

print(str(C), str(L))


