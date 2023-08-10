# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do

# do seno, cosseno e tangente desse ângulo


import math

angulo = float(input('Digite o ângulo que você deseja: '))

#Classe math possui metodos que calculam seno, cosseno e tangente, porém,

# o valor não vem radianos e quando trabalhamos com ângulos, preicisamos
# desse formato, sendo assim, devemos tambem utilizar o metodo radians
# para converter o resultado em radiano

seno = math.sin(math.radians(angulo))

cosseno = math.cos(math.radians(angulo))

tangente = math.tan(math.radians(angulo))

print('Seno: {:.2f}'.format(seno))

print('Cosseno: {:.2f}'.format(cosseno))

print('Tangente: {:.2f}'.format(tangente ))
