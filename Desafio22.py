# Crie um programa que leia o nome completo de uma pessoa e mostre:

#O nome com todas as letras maiusculas 

# O nome com todas as letras minusculas

#Quantas letras ao todo (sem considerar espaços)

#Quantas letras tem o primeiro nome

nome = str(input('Qual o seu nome completo? '))

print('Nome com todas as letras maiusculas: {}'.format(nome.upper()))


print('Nome com todas as letras maiusculas: {}'.format(nome.lower()))

#nesse caso temos que subtrair da contagem a quantidade de espaços do
# texto, sendo assim, imprimos o nome menos o count de espaços
print('Quant. letras sem considerar os espaços: {}'.format(len(nome) - nome.count(' ')))

#Lembra que anteriormente comentamos que o find significa encontrar?
# Então basta encontrar ou pesquisar o primeiro espaço em branco que
#o programa ira contar as letras anteriores e imprimir na tela

print('Seu primeiro nome possui {} letras'.format(nome.find(' ')))

#Outra alternativa de resolução
#Como o split separa as partes do nome levando em consideração os espaços
#é so pedirmos para imprimir o tamanho do indice 0, ou seja o 1° espaço
separa = nome.split()

print('Contagem do primeiro nome com split: {}'.format(len(separa[0])))

