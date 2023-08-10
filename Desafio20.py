# O mesmo professor do desafio anterior quer sortear a ordem de apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome dos 4 alunos
# e mostre a ordem sorteada

import random

n1 = input('primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1, n2, n3, n4]
# Para embaralhar a ordem dos dados, usamos o método shuffle que significa
# embaralhar, para funcionar precisamos passar como parametro os valores 
# que devem ser embaralhados, no nosso caso, vamos passr um array com os
# nomes

random.shuffle(lista)

print('A nova ordem foi criada')
print(lista)
