# Crie um programa onde 4 jogadores joguem um dado e tenham resultados 
# aleatórios. Guarde esses resultados em um dicionário. No final,
# coloque esse dicionário ordem, sabendo que o vencedor tirou o
# maior numero no dado.
from random import randint
from time import sleep

jogador1 = randint(1,6)

jogador2 = randint(1,6)

jogador3 = randint(1,6)

jogador4 = randint(1,6)


numeros = {'Jogador1: ': jogador1, 'Jogador2: ':jogador2, 
           'Jogador3: ': jogador3, 'Jogador4: ':jogador4 }


# Vamos verificar o vencedor, que vai ser aquele que tirou o maior
# numero

if jogador1 > jogador2 and jogador1 > jogador3 and jogador1 > jogador4:
    
    numeros['Vencedor: '] = 'O jogador 1 venceu'

elif jogador2 > jogador1 and jogador2 > jogador3 and jogador2 > jogador4:
    
    numeros['Vencedor: '] = 'O jogador 2 venceu'

elif jogador3 > jogador1 and jogador3 > jogador2 and jogador3 > jogador4:
    
    numeros['Vencedor: '] = 'O jogador 3 venceu' 

elif jogador4 > jogador1 and jogador4 > jogador2 and jogador4 > jogador3:
    
    numeros['Vencedor: '] = 'O jogador 4 venceu'
    
else:
    
    numeros ['Vencedor: '] = 'nenhum jogador venceu'
    



print('Valor do jogador 1: {}'.format(numeros['Jogador1: ']))
sleep(1)
print('Valor do jogador 2: {}'.format(numeros['Jogador2: ']))
sleep(1)
print('Valor do jogador 3: {}'.format(numeros['Jogador3: ']))
sleep(1)
print('Valor do jogador 4: {}'.format(numeros['Jogador4: ']))
sleep(1)


print(numeros['Vencedor: '])