
#Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Apesar do python ter o metodo factorial da biblioteca math, reaalize
# os cálculos usando o while

valor = int(input('Digite um numero para calcular seu fatorial: '))

# nesse caso o contador deve começar no valor e ir diminuindo

cont = valor
fat = 1
while cont > 0:
     print('{} x '.format(cont), end = ' ')
     print(' x ' if cont > 1 else ' = ', end = ' ')
     fat = fat * cont
     cont = cont - 1    
print(fat)
                                                                                                 