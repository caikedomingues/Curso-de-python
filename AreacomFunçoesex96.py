
# Faça um programa que tenha uma função chamada area(), que receba as
# dimensões de um terreno retangular (largura e comprimento) e mostre a
# area do terreno 

def area(l, c):
    
    area = a * c
    print('A area de um terreno {}x{} é de {}'.format(l,c,area))
    
#programa principal

largura = float(input('Informe a altura do terreno: '))
comprimento = float(input('Informe a largura do terreno: '))

area(largura, comprimento)