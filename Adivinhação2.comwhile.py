
# Melhore o jogo do desafio 28 onde o computador vai 'pensar' um numero
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar
# mostrando no final quantos palpites foram necessários para vencer

from random import randint

computador = randint(1,10)

contTentativas = 0

print('Pensei em um valor de 1 a 10. sera que você consegue adivinhar? ')
print("--------------------------------------------------------------")
usuario = int(input('Qual o seu palpite? '))


while usuario != computador:
    
    contTentativas = contTentativas + 1
    
    if usuario < computador:
        print('Pensei em um valor maior')
    else:
        print('pensei em um valor menor')
    print("--------------------------------------------------------------")
    usuario =  int(input('Qual o seu palpite? '))
    print("--------------------------------------------------------------")
print('você acertou, pensei no numero {}'.format(computador))
print('para chegar no resultado foram necessárias {} tentativas'.format(contTentativas))