# Crie um programa que gerencie o aproveitamento de um jogador de futebol
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final
# tudo será guardado em um dicionário, incluindo o total de de gols
# feitos durante o campeonato

from time import sleep

nome = str(input('Nome do jogador: '))
quantPartidas = int(input('Quantidade de partidas {} jogou: '.format(nome)))

soma = 0

partidas = 0

for part in range(0, quantPartidas):
    
    partidas = int(input('Gols na partida {}: '.format(part + 1)))
    
    soma = soma + partidas

aproveitamento = {'Nome: ' : nome, 'Quant.partidas: ' : quantPartidas, 'Total de gols: ' : soma}

print(aproveitamento)
