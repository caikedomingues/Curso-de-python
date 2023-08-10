# crie um programa que simule o funcionamento de um caixa eletrônico
# no inicio, pergunte ao usuário qual será o valor a ser sacado(numero
# inteiro) e o programa vai informar quantas cédulas de cada valor
# serão entregues

# obs: considere que o caixa possui cedulas de 50, 20, 10 e 1

valor = int(input('Informe o valor a ser sacado: '))
total = valor #total do saque
ced = 50 #Valor inicial: a cédula mais alta
totced = 0 # total de cedulas

# Vamos iniciar um while infinito
while True:
    
    if total >= ced:
        total = total - ced
        totced = totced + 1
    else:
        
        if totced > 0:
          print('Total de {} cédulas de R${}'.format(totced, ced))
        
        if ced == 50:
            ced = 20
            
        elif ced == 20:
            ced = 10
        
        elif ced == 10:
            ced = 1
            
        totced = 0
        
        if total == 0:
            break 
    print('Programa encerrado')
        




