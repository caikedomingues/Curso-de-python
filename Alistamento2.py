# Faça um programa que leia o ano de nascimento de um jovem e informe 
# de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
# se é hora de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou
# do prazo.

from datetime import date

anonascimento = int(input('Ano de nascimento: '))

calcidade = date.today().year - anonascimento

if calcidade < 18:
    
    alistamento = 18 - calcidade
    print("Você tem {} anos de idade, devera realizar o seu alistamento daqui há {} anos".format(calcidade, alistamento))
    print('Ano do alistamento: {}'.format(ano))
elif calcidade == 18:
    
    print('Você deve realizar o alistamento esse ano')

elif calcidade > 18:
    alistamento = calcidade - 18

    print('Você tem {} anos de idade, deveria ter realizado o alistamento há {} anos'.format(calcidade,alistamento))
    