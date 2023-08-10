
# Vamos criar nosso primeiro dicionario

pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':22}

print(pessoas)

# Também posso acessar um elemento especifico do dicionário, mas no caso
# do dicionario não trabalhamos com indices e sim co chaves literais

print(pessoas['nome'])


# podemos acessar apenas as chaves do dicionario usando o método
# keys()

print(pessoas.keys())

# podemos imprimir só os valores do dicionário com o método values()

print(pessoas.values())

# há a possibilidade de imprimir todos o itens e elementos do dicionário
# usando o método items()

print(pessoas.items())

# Há a possibilidade de utilizarmos os métodos anteriores em laços

# for para chaves

for k in pessoas.keys():
    
    print("Laço de chaves: {}".format(k))

# Laço de valores

for v in pessoas.values():
    
    print('Laço de valores: {}'.format(v))

# laço de itens

for i in pessoas.items():
    
    print('Laço de itens: {}'.format(i))
    

# precisamos agora usar o comando del para excluir uma das chave

del pessoas['sexo']

print(pessoas)

# Há a possibilidade de mudar o valor de uma determinada chave

pessoas['nome'] = 'leandro'

print(pessoas)

# podemos adicionar elementos no dicionário

pessoas['peso'] = 98.5

print(pessoas)