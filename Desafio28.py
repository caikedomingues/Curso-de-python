#Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador. O programa devera escrever na tela se o
# usuário venceu ou perdeu

from random import randint

from time import sleep

aleatorio = randint(0, 5)
numero = int(input('Informe um numero ')) 

print('processando')
sleep(3)
if numero == aleatorio:
    print('Você acertou, eu pensei no número {}'.format(aleatorio))
else:
    print('Você errou eu pensei no número {}'.format(aleatorio))