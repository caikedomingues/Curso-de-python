# crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final mostre:

# Quantas pessoas foram cadastradas
# A média de idade do grupo
# uma lista com todas as mulheres
# uma lista com todas as pessoas com idade acima da média

cadastro = []
acimaMédia = []
mulheres = []
contPessoas = 0
totIdade = 0
media = 0

while True:
    
    pessoa = {'Nome: ': str(input('Nome: ')),
              'Sexo: ': str(input('Sexo: ')),
              'Idade: ': int(input('Sua idade: '))
              
              }
    cadastro.append(pessoa.copy())
    
    contPessoas = contPessoas + 1
    totIdade = totIdade + pessoa['Idade: ']
    media = totIdade / contPessoas
    
    resp = str(input('Quer cadastrar mais alguem? s/n: '))
    
    if resp in 'nN':
        break
   
    
    if pessoa['Sexo: '] == 'f':
        
        mulheres.append(pessoa['Nome: '])
        
    if pessoa['Idade: '] > media:
        
        acimaMédia.append(pessoa.copy())

    
    
print('-----------------------------------------------------')

    
    
print('Quantidade de pessoas cadastradas: {}'.format(contPessoas))

print('-----------------------------------------------------')    
    
print('Lista de mulheres: {}'.format(mulheres))

print('-----------------------------------------------------')    
    
print('Media de idade do grupo: {}'.format(media))

print('-----------------------------------------------------')    
    
print('Lista de pessoas com idade acima da média: {}'.format(acimaMédia))

print('-----------------------------------------------------')    

print('Pessoas cadastradas: {}'.format(cadastro))



    