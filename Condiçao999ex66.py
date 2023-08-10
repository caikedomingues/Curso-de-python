# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que
# é a condição de parada. No final, mostre quantos numeros foram
# digitados e qual foi a soma entre eles (desconiderando o flag).


n = 0
cont = 0
soma = 0

while n != 999:
    n = int(input('Digite um numero (999 para parar): '))
    
    if n == 999:
        
        break
    soma = soma + n
    cont = cont + 1

print('Soma dos valores informados: {}'.format(soma))
print('Quantidade de valores informados: {}'.format(cont))
