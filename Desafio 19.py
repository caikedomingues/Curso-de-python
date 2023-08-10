# Um professor quer sortear um dos seus quatro alunos para apagar o
# o quadro. Faça um programa que ajude ele, lendo o nome deles e
# escrevendo o nome do escolhido.

# Import do metodo random que tem como função gerar valores aleatórios
# dentro de um intewrvalo
import random

n1 = input('Primeiro aluno: ')

n2 = input('Segundo aluno: ')

n3 = input('Terceiro aluno: ')

n4 = input('Quarto aluno: ')

#Array com os nomes informados
lista = [n1, n2, n3, n4]
# a variável escolhido ira receber o random.choice que significa algo como
# "uma escolha dentro de algo", no nosso caso, uma escolha dentro da lista
# Observação: o metodo choice faz parte da classe random
escolhido = random.choice(lista)

#Impressão do reesultado
print('O aluno escolhido foi: {}'.format(escolhido))