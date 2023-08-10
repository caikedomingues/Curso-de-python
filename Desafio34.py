#Faça um programa que pergunte o salário de um funcionário e calcule o
# o valor do seu aumento. Para salarios superiores a 1.250, calcule um
# aumento de 10% para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Informe o salário '))

if salario <= 1250:
    
    novo = salario + (salario * 15 / 100)
    print('O funcionário que recebia {} passara a receber {}'.format(salario, novo))
else: 
    
    novo = salario + (salario * 10 / 100)
    print('O funcionário que recebia {} passara a receber {}'.format(salario, novo))