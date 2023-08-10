

# Crie um programa que vai ler vários numeros e colocar em uma lista.
# Depois disso, crie duas listas extras que vão contar apenas os valores 
# pares e os valores impares digitados, respectivamente. Ao final, mostre
# o conteúdo das 3 listas geradas.


completa = []
par = []
impar = []


while True:
    
    n = int(input('Informe um numero: '))
    
    completa.append(n)
    
    resp = str(input('Quer continuar? s/n: '))
    
    if n % 2 == 0:
        
        par.append(n)
    
    else:
        
        impar.append(n)
    
    if resp == 'n':
        break

print('Lista completa: {}'.format(completa))
print('Lista par: {}'.format(par))
print('Lista impar: {}'.format(impar))