# Podemos criar funções que trabalham o conceito de listas, nesse caso,
# vamos criar uma lista que ira dobrar os valores passados na lista


def dobra(lst):
    
    pos = 0 # posição inicial da lista
    # enquanto a posição da lista for menor que o tamanho da lista criada
    # ele ira multiplicar os valores da lista por 2 e adicionar mais 1
    # na posição, ou seja, ira aumentar o tamanho da lista até o seu 
    # tamanho ideal
    
    while pos < len(lst):
        
        lst[pos] *= 2
        
        pos = pos + 1

# Programa principal
valores = [6, 3, 9, 1, 0, 2]

dobra(valores)

print(valores)

