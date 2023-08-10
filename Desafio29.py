# Escreva um programa que leia a velocidade de um carro. Se ele 
# ultrapassar 80km. mostre uma mensagem dizendo que ele foi multado
#A multa vai custar 7,00 por cada km acima do limite

from time import sleep
velocidade = float(input('Qual a velocidade '))

if velocidade <= 80:
    
    print('Dirija com cuidado tenha um bom dia')
else:
    
    print('Você foi multado')
    print('Calculando a multa....')
    sleep(2)
    multa = (velocidade - 80) * 7
    print('Valor da multa: {:.2f}'.format(multa))
