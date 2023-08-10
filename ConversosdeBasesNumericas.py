# Escreva um programa que leia um numero inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão: 

# 1 para binário, 2 para octal, 3 para hexadecimal

# o python possui métodos automáticos para converter os valores

from time import sleep
num = int(input('Digite um numero '))
print('''
      1 - para binário
      2- para octal
      3 - hexadecimal
      ''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('Convertendo')
    sleep(2)
    #Na formatação faremos o fatiiamento da resposta, para não aparecer
    # as 2 primeiras letras de indicação que o python coloca
    print('O valor {} convertido em binário é: {}'.format(num, bin(num) [2:]))

elif opcao == 2:
    print('Convertendo')
    sleep(2)
    print('O valor {} convertido em octal é: {}'.format(num, oct(num) [2:]))

elif opcao == 3:
    print('Convertendo')
    sleep(2)
    print('O valor {} convertido em hexadecimal é: {}'.format(num, hex(num) [2:]))

else:
    
    print('Opção inválida')
    
    
