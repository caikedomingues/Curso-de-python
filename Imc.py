# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
# seu imc e mostre seu status de acordo com a tabela abaixo:
# abaixo de 18.5: abaixo do peso
# entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
# 30 até 40: obesidade
# acima de 40: obesidade mórbida

peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))

imc =  peso / (altura ** 2) 

if imc < 18.5:
    print('abaixo do peso')

elif imc >= 18.5 and imc <= 25:
    print('Peso ideal')

elif imc > 25 and imc <= 30:
    print('sobrepeso')

elif imc > 30 and imc <= 40:
    print('Obesidade')

else:
    print('Obesidade mórbida')