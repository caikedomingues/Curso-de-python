# Crie um programa que leia nome, sexo e a idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre: 

# quantas pessoas cadastradas
# a media de idade
# uma lista com idade acima da média


# primeiro vamos criar o dicionário que ira armazenar os dados do usuário

pessoa = dict() # ira armazenar os dados
cadastro = [] # ira receber o dicionário
acimadamedia = []
contPessoas = 0 #Contagem de cadastros
somaidade = 0 # irá realizar a soma de idades
media = 0 # Ira calcular a média das idades


while True:
    
# Vamos pedir um nome
    pessoa['Nome: '] = str(input('Nome: '))

    # Agora vamos fazer uma validação para o pedido do sexo, onde vamos 
    # verificar se o usuário digitou M ou F, caso contrário o programa
    # ira aprsentar uma mensagem de erro e pedir novamente

    while True:
        # Vamos converter o valor para maiusculo e considerar só a 
        # primeira letra
        pessoa['Sexo: '] = str(input('Sexo [M/F]: ')).upper()[0]
        
        if pessoa['Sexo: '] in 'MF':
            
            break
        
        print('ERRO! por favor, digite apenas M ou F')

    pessoa['Idade: '] = int(input('Idade: '))
    somaidade = somaidade + pessoa['Idade: ']
    cadastro.append(pessoa.copy())
    contPessoas = contPessoas + 1
    media = somaidade / contPessoas
    
    if pessoa['Idade: '] >= media:
        
        acimadamedia.append(pessoa['Nome: '])
    
    while True:
        
          resp = str(input('Você quer continuar? S/N: ')).upper()[0]
          
          if resp in 'SN':
              
               break
           
          else:
              
              print('Responda apenas S ou N')
              
    if resp == 'N':
        
        break


print(cadastro)
print('Quantidade de cadastro: {}'.format(contPessoas))
print('Médias das idades cadastradas: {}'.format(media))

