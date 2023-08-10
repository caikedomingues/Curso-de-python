#Crie um programa que leia um número real qualquer pelo teclado e mostre

#na tela a sua porção inteira

#Vamos importar a biblioteca math e usar a função trunc: que serve para

#'truncar' o valor, ou seja, quebrar ou arredontar. Para funcionar é

#necessário passar como parametro o valor que deve ser arredondado


import math

numero = float(input('Informe um numero: '))

print('O valor {} possui como porção inteira o valor: {}'.format(numero, math.trunc(numero)))


#Agora vamos tentar fazer o mesmo exercicio só que sem utilizar os
#métodos da biblioteca math, para isso, basta, trocar o tipo do valor
#na hora da impressão.

num = float(input('Informe o segundo valor: '))

print('valor inteiro do segundo numero: {}'.format(int(num)))