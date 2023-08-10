

# criação da primeira lista e atribuição de valores
teste = list()
teste.append('Gustavo')
teste.append(40)

# Criação da segunda lista que ira armazenar a primeira, para podermos
# futuramente adicionar valores na primeira lista e na segunda, devemos
# criar cópias com o sinal [:] na hora de atribuir a primeira dentro da
# segunda.

galera = list()
galera.append(teste[:])

# Adicionando mais valores

teste[0] = 'Maria'
teste[1] = 22

galera.append(teste[:])

print(galera)

# Também é possivel criar várias listas internas dentro de uma lista

pessoas = [['João', 19], ['Maria', 22], ['Joaquim', 13], ['Ana', 33]]

print(pessoas)

# Dentro das listas internas eu também posso imprimir um valor especifico
# por exemplo, vamos imprimir os valores do indice 0

print(pessoas[0])

#Posso também pegar um valor especifico do indice da lista interna, por
# exemplo:

print(pessoas[0][0])

#Voltando la prá cima, podemos percorrer os valores da lista com um for

for p in galera:
    
    print(p)

# Nesses casos, podemos imprimir só os nomes ou só as idades

for p in galera:
    
    print(p[0])

for p in galera:
    
    print(p[1])



