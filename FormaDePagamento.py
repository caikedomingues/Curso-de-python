# Elabore um programa que calcule o valor a pago por um produto considerando
# o seu preço normal e condição de pagamento 

# a vista dinheiro/cheque: 10% de desconto
# a vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

preco = float(input('Qual o preço do produto? '))
print('-----------------------------------------')
print('        Qual a forma de pagamento? ')
print('1 - A vista com dinheiro ou cheque: 10% de desconto')
print('2 - A vista no cartão: 5% de desconto')
print('3 - em até 2x no cartão: preço normal')
print('4 -3x no cartão: juros de 20%')

forma = int(input("Escolha a forma de pagamento: "))

if forma == 1:
    
    calcdesc = preco - (preco *10/100)
    print('O produto que custa {:.2f} passara a valer {:.2f} por conta dos 10% de desconto'.format(preco, calcdesc))

elif forma == 2:
    
    calcdesc = preco - (preco * 5 / 100)
    print('O produto que custa {:.2f} passara a valer {:.2f} por conta dos 5% de desconto'.format(preco, calcdesc))

elif forma == 3:
    calcdesc = preco / 2
    print("O produto custara o seu preço normal, ou seja, {:.2f} reais, que parcelado em 2x ficara {:.2f}".format(preco, calcdesc))
    
elif forma == 4:
    
    calcjuros = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = calcjuros / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros '.format(totparc,parcela))
    print('Sua compra de R${} vai custar R${} no final'.format(preco, calcjuros))

else:
    print('Forma de pagamento inválida')