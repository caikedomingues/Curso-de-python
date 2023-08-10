# faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um triângulo retângulo, calcule e mostre o comprimento
# da hipotenusa

#usando a classe math

import math

co = float(input('Comprimento do cateto oposto '))
ca = float(input('C omprimento do cateto adjacente '))
#Vamos usar  o metodo hypot da classe math que tem como finalidade calcular
#a hipotenusa dos valores, para funcionar basta passar 2 parametros, o
#cateto oposto e o adjascente

hi = math.hypot(co,ca)

print('a hipotenusa vai medir: {:.2f}'.format(hi))