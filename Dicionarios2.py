# Nessa parte 2 vamos misturar dois conceitos, sendo eles a lista e o 
# dicionário, dito isso, vamos criar a nossa lista que será chamada de
# Brasil

brasil = []

# Criaçaõ dos dicionarios

estado1 = {'uf' : 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf' : 'São Paulo', 'sigla': 'SP'}

# Vamos adicionar na lista os 2 dicionários criados

brasil.append(estado1)
brasil.append(estado2)

# Vamos imprimir a lista

print(brasil)

# se quisermos podemos imprimir um dicionário especifico da lista

print(brasil[0]) # rio de janeiro
print(brasil[1]) # São Paulo 

# podemos imprimir apenas um valor especifico do dicionário que está
# dentro da lista

print(brasil[0]['uf']) # rio de janeiro

print(brasil[1]['uf']) # São Paulo

# Vamos realizar um pequeno exercicio usando for, será necessário usarmos
# o conceito de cópia nesse exercicio, pois, o dicionario substitui o
# valor se utilizarmos a mesma chave para atribuir outro valor

estado = {} # dicionário

brasil = [] # listas

for c in range(0,3):
    
    estado['uf: '] = str(input('Unidade federativa: '))
    estado['sigla: '] = str(input('Sigla: '))
    
    brasil.append(estado.copy()) # método copy: ira copiar os valores para
    #não perdemos eles futuramente

print(brasil)






