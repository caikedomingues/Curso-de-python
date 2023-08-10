# Vamos criar um programa que encerre o pedido de valores quando o 
# usuário digita 0, porem, o programa ira contar os valores pares
# e impares

par = 0
impar = 0

n = 1

while n != 0:
    
    n = int(input('Informe um numero: '))
    
    if n % 2 == 0:
        
        par = par + 1
    else:
        impar = impar + 1

print('Quantidade de valores pares: {}'.format(par))
print('Quantidade de valores impares: {}'.format(impar))