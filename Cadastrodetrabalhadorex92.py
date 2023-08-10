# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre - os (com idade ) em um dicionário se por acaso a ctps
# for diferente de zero, o dicionário receberá também o ano de 
# contratação e o salário.  Calcule e acrescente, além da idade, com
# quantos anos a pessoa vai se aposentar.

#primeiro vamos importar o metodo datetime para podermos pegar o ano
# atual que estamos

from datetime import datetime

# Agora, vamos criar um dicionário para guardar todos os valores

dados = dict()

dados [ 'nome: '] = str(input('Nome: '))

nasc = int(input('Ano de nasicimento: '))

# Cálculo da idade
idade = datetime.now().year - nasc

dados ['idade: '] = idade

dados ['CTPS: '] = int(input('Carteira de trabalho (caso não tenha  0): '))

#Agora vamos verificar se o valor informado na ctps é diferente de zero.
# Caso essa condição for verdadeira, vamos ler o ano de contratação,
# o salário e com quantos anos o funcionário irá se aposentar

if dados['CTPS: '] != 0:
    
    dados['contratação: '] = int(input('Ano de contratação: '))
    dados['Salário: '] = float(input('Salário: R$'))
    #Calculo da aposentadoria: para descobrirmos a idade que o funcionário
    # irá se aposentar basta, pegar a idade e somar com o resultado da 
    # soma entre o ano de contração e 35 (valor estabelecido como tempo 
    # de contribuição) menos o ano atual
    
    dados ['Aposentadoria: '] = dados['idade: '] + (dados['contratação: '] + 35) - datetime.now().year

print('--------------------------------------')
print('Dados cadastrados')
print('--------------------------------------')
print(dados)