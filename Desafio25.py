# crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva"
# no nome, lembre-se o in não é um método é um operador do python

nome = str(input('Qual o seu nome? ')).upper()

print('Seu nome tem Silva? {}'.format('SILVA' in nome))
