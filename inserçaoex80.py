# Crie um programa onde o usuário possa digitar 5 valores numericos e
# e cadastre - os em uma lista já na posição correta de inserção

num1 = int(input('Informe o 1° valor: '))
num2 = int(input('Informe o 2° valor: '))
num3 = int(input('Informe o 3° valor: '))
num4 = int(input('Informe o 4° valor: '))
num5 = int(input('Informe o 5° valor: '))

numeros = [num1, num2, num3, num4, num5]

if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
    
    print('Valor adicionado na posição 0')
    numeros.insert(0, num1)

elif num2 > num1 and num2 < num3 and num2 < num4 and num2 < num5:
    
    print('Valor adicionado na posição 1')
    numeros.insert(1, num2)

elif num3 > num1 and num3 > num2 and num3 < num4 and num3 < num5:
    
    print('Valor adicionado na posição 2')
    numeros.insert(2, num3)
    

print(numeros)