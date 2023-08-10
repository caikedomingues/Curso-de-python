#Crie um programa que faça o computador jogar jokenpo com você


#Para começar será necessário importar a biblioteca random
from time import sleep 
from random import randint

itens = ('pedra', 'papel','tesoura')

#O computador ira gerar valores aleatórios entre 0 e 2

computador = randint(0, 2)

#Agora vamos trabalhar as opções do jogador

print('''     Suas opções 
        
        0 - pedra
        
        1 - papel
        
        2 - tesoura
          
      
      ''')

jogador = int(input('Qual a sua jogada? '))

print('jo')
sleep(1)
print('ken')
sleep(1)
print('po!')

print('O jogador jogou {}'.format(itens[jogador]))

if computador == 0: #Computador jogou pedra
    
    if jogador == 0:
        print('Empate')
    
    elif jogador == 1:
        print("Jogador ganhou")
        
    elif jogador == 2:
        print("Computador ganhou")

elif computador == 1: #Computador jogou papel
    
    if jogador == 0:
        print('Computador ganhou')
        
    elif jogador == 1:
        print('Empate')
    
    elif jogador == 2:
        print('Jogador ganhou')

elif computador == 2: #Compuatdor jogou tesoura
    
    if jogador == 0:
        print('Jogador ganhou')
    
    elif jogador == 1: 
        print('computador ganhou')
    
    elif jogador == 2:
        print('Empate')

else:
    print('Jogada inválida')
        
    
print('O computador escolheu {}'.format(itens[computador]))
        
    
    







