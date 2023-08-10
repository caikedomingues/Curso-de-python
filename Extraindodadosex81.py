# Crie um  programa que vai ler varios numeros e colocar em uma lista.
# Depois disso, mostre:
# quantos numeros foram digitados
# a lista de valores, ordenada de forma decrescente
# se o valor 5 foi digitado e está na lista.

numeros = []

contNumeros = 0

while True:
    
    n = int(input('Informe um numero: '))
    
    contNumeros = contNumeros + 1
    
    numeros.append(n)
    
    resp = str(input('Você quer continuar? s/n: '))
    
    if resp == 'n':
        break
    

numeros.sort(reverse=True)
print('Valores digitados em ordem decrescente: {}'.format(numeros))
print('Quantidade de valores digitados: {}'.format(contNumeros))

if 5 in numeros:
    
    print('O valor 5 esta na lista')
    
else:
    print('O valor 5 não está na lista')
    