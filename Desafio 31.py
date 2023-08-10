# Desenvolva um programa que pergunte a distância de uma viagem em km.

# Calcule o preço da passagem, cobrando 0,50 por km para viagens de até 

# 200 km e 0,45 para viagens mais longas
from time import sleep
distancia = float(input('informe a distância: '))

if distancia <= 200:
    passagem = distancia * 0.50
    print('Calculando passagem ...')
    sleep(2)
    print('valor da passagem: {:.2f}'.format(passagem))
else:
    passagem = distancia * 0.45
    print('Calculando passagem....')
    sleep(2)
    print('Valor da passagem: {:.2f}'.format(passagem))