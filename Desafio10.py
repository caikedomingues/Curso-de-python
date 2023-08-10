#Considerando que 1 dolar é 3,27

valorReais = float(input("Qual o valor em reais? "))

dolar = 3.27

conversao = valorReais / dolar

print('O valor {:.2f} em reais convertido em dolar é {:.2f} '.format(valorReais, conversao))