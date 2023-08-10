#Faça um programa que leia o nome completo de uma pessoa. Mostrando
# em seguida o primeiro e o último nome separadamente.
# ex: ana maria de souza
# primeiro = ana
# último = souza

nome = str(input('Informe o seu nome completo: ')).strip()
#Serve para dividir as palavras separando por espaços
n = nome.split()

print('primeiro nome: {}'.format(n[0]))

#No caso do ultimo temos que indicar no indice que queremos
# pegar o tamanho do nome e subtrair 1 do comprimento assim, ele, 
#  imprimira a ultima palavra do nome
print('ultimo nome: {}'.format(n[len(n) - 1]))