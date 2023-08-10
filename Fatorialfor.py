
valor = int(input('Informe o valor: '))
fat = 1
for c in range(valor, 1,-1):
    
    fat = fat * c
print('O fatorial de {} é igual a {}'.format(valor, fat))