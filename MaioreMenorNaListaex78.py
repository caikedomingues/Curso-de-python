# Faça um programa que leia valores e guarde-os em uma lista.
# No final, mostre qual foi o maior valor digitado e suas respectivas
# posições na lista.

listanum = []
mai = 0
men = 0

for c in range(0,5):
    
    listanum.append(int(input('Digite um valor para a posição {}: '.format(c))))
    
    if c == 0:
        mai = listanum[c]
        men = listanum[c]
    
    else:
        if listanum[c] > mai:
            
            mai = listanum[c]
        
        if listanum[c] < men:
            
            men = listanum[c]

print('Valores informados: {}'.format(listanum))
print('O maior valor informado foi o {}'.format(mai, end=' '))

for i, v in enumerate(listanum):
    
    if v == mai:
        print('Posição que o maior valor aparece: {} '.format(i, end = ' '))

print('O menor valor informado foi o {}'.format(men))
for i, v, in enumerate(listanum):
    
    if v == men:
        print('Posição que o menor valor aparece: {}'.format(i, end = ' '))
