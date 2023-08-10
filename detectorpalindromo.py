
# Crie um programa que leia uma frase qualquer diga se ela é um
# desconsiderando os espaços

# exemplos para teste
# apos a sopa
# a sacada da sopa
# a torre da derrota
# o lobo ama o bolo
# anotaram a data da maratona

#Primeiro vamos ler uma frase e excluir os espaços em brancos e converter
# para maiusculo

frase = str(input('Digite uma frase: ')).strip().upper()

#Agora vamos separar as palavras por espaço
palavra = frase.split()

#Agora vamos juntar as palavras
junto = ''.join(palavra)

inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    
    inverso = inverso + junto[letra]

print(junto, inverso)

if inverso == junto:
    print('Temou um palindromo')
else:
    print('Não temos um palindromo')