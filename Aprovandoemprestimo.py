# Escreva um programa para aprovar o empréstimo bancário para a compra de
# uma casa. Pergunte o valor da casa, o salário do comprador e em quantos
# anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo
# será negado

casa = float(input('Valor da casa: '))
salario = float(input('salário do comprador '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos*12)

porcentagem = salario * 30 / 100

if prestacao > porcentagem:
    print('Empréstimo negado')
    print('como você recebe {:.2f} R$, você não pode pagar {:.2f} R$ mensais'.format(salario, prestacao))

else:
    print('empréstimo aprovado')
    print('você ira pagar {:.2f}R$ mensais'.format(prestacao))
    
    