# Desenvolva um programa que leia quatro valores pelo teclado e guarde
# os em uma tupla. No final, mostre:
# Quantas vezes aparece o 9
# Em que posição foi digitado o primeiro 3
# quais foram os numeros pares

numeros = (int(input('Digite o 1° numero: ')), int(input('Digite o 2° numero: ')),
           int(input('Digite o 3° numero: ')), int(input('Digite o 4° numero: ')))

print('Você digitou os valores: {}'.format(numeros))

print('Quantidade de 9 na lista: {}'.format(numeros.count(9)))


if 3 in numeros:
    print('Posição inicial do 3: {}'.format(numeros.index(3) + 1))

else:
    
    print('O valor 3 não foi digitado')

for n in numeros:
    
    if n % 2 == 0:
        
        print('Valor par: {}'.format(n))





