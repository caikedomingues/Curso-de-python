#Faça um programa que peça 3 valores e informe o maior e o menor valor

num1 = int(input('Primeiro valor: '))

num2 = int(input('Segundo valor: '))

num3 = int(input('Terceiro valor: '))

if num1 > num2 and num1 > num3:
    print("Maior valor informado: {}".format(num1))

if num1 < num2 and num1 < num2:
    
    print('Menor valor informado: {}'.format(num1))
    
if num2 > num1 and num2 > num3:
    print('Maior valor informado: {}'.format(num2))
    
if num2 < num1 and num2 < num3:
    print('Menor valor informado: {}'.format(num2))
    
if num3 > num1 and num3 > num2:
    
    print('Maior valor informado: {}'.format(num3))
    
if num3 < num1 and num3 < num2:
    
    print('Menor valor informado: {}'.format(num3))
    
if num3 == num1 and num3 ==  num2:
    
    print('Os valores são iguais')