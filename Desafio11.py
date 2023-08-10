#Faça um programa que leia a largura e a altura de uma parede em metros,
#Calcule a sua área ea quantidade de tinta necessária para pinta-la,
#sabendo que cada litro de tinta, pinta uma área de 2m quadradoss

larg = float(input("Largura da parede: "))

alt = float(input("Altura da parede: "))

area = larg * alt

print('Sua parede tem dimensão {:.2f} x {:.2f} e sua área é de {:.2f}'.format(larg,alt, area))

tinta = area / 2

print('Para pintar essa parede você ira precisar de {} litros de tintas'.format(tinta))