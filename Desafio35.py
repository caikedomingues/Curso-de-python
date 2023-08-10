# Desenvolva um programa que leia o comprimento de três retas e diga ao

# usuário se elas podem ou não formar um triângulo, vale lembrar que:

# para formar um triângulo é necessario que  as retas tenham um

# comprimento menor que a soma das outras 2 retas

reta1 = float(input("Primeira reta: "))

reta2 = float(input('Segunda reta: '))

reta3 = float(input('Terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    
    print('é possivel criar um triângulo')

else:
    print('Não é possivel criar um triângulo')
