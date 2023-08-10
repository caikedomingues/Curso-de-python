# Crie um programa que leia vários numeros inteiros pelo teclado. No
# final da execução, mostre a média entre todos os valores e qual foi
# o maior e o menor valor lido. O programa deve perguntar ao usuário
# se ele quer ou não continuar a digitar valores


resp = 'sim'

soma = quant  = media = maior = menor = 0
while resp == 'sim':
    
    num = int(input('Digite um numero: '))
    soma = soma + num
    
    quant = quant + 1
    
    if quant == 1:
        maior = num
        menor = num
        
    else:
        if num > maior:
            maior = num
            
        if num < menor:
            menor = num
        
        
    resp = str(input('quer continuar? sim/não '))

media = soma / quant

print('Você digitou {} numeros e a media entre eles é {}'.format(quant, media))
print('Maior valor: {}'.format(maior))
print('Menor valor: {}'.format(menor))
