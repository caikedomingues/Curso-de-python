# Faça um programa que tenha uma função chamda ficha(), que receba dois 
# parametros opcionais o nome de um jogador e quantos gols ele marcou
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo
# que algum dado não tenha sido informado corretamente

def ficha(nome = '<Desconhecido>', gols = '0'):
    
    if nome == '':
        
        print('O jogador desconhecido fez {} gols'.format(gols))
    
    elif nome == '' and gols == '':
        
        print('O jogador desconhecido fez  0 gols' )
    
    elif gols == '':
        
        print('O jogador desconhecido fez 0 gols')
    
    else:
        
        print('O jogador {} fez {} gols'.format(nome,gols))

# Programa Principal

nome = str(input('Informe o nome do jogador: '))
gols = str(input('Quantidade de gols feitos pelo atleta: '))

ficha(nome,gols)