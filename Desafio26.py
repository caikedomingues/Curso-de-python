# faça um programa que leia uma frase pelo teclado e mostre:

#  quantas vezes aparece a letra 'A'

# em que posição ela aparece a primeira vez

# em que posição ela aparece a última vez

nome = str(input('Informe o nome: ')).upper().strip()

print('A letra A aparece {} vezes'.format(nome.count('A')))

print('Aparece pela primeira vez: {}'.format(nome.find('A') + 1))

#Agora para achar a ultima ação devemos usar o rfind que significa busacr pela
# direita
print('Aparece pela ultima vez: {}'.format(nome.rfind('A') + 1))
