# faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um triângulo retângulo, calcule e mostre o comprimento
# da hipotenusa

#Formula matemática

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))

hi = (co ** 2 + ca**2) ** (1/2)

print('A hipotenusa vai medir: {:.2f}'.format(hi))