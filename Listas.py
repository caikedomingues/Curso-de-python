# Vamos começar o estudo de listas criando uma (é obvio), e vamos usar 
# o método append para adicionar um valor a mais na lista

num = [2,5,9,1]
# Vamos adicionar o 7

num.append(7)

#Vamos ordenar os valores da lista

num.sort()

# Vamos imprimir a lista
print(num)

#Vamos ordenar de maneira inversa

num.sort(reverse = True)

print(num)

#Vamos verificar o tamanho da lista
print('Tamanho da lista: {}'.format(len(num)))

#Há a possibilidade de adicionarmos um valor em qualquer posição, para 
# isso, basta usar o método insert que recebe como parametro a posição
# do valor que vai ser adicionado e o valor.

num.insert(2, 0)
print(num)

# É possivel eliminar valores da lista utilizando o pop, caso ele não 
# receba nenhum parametro, ele ira excluir o ultimo valor da lista.
# Mas, podemos passar como parametro a posição que queremos excluir

num.pop(2)

print(num)

# Outra forma de excluir valores é através do método remove que recebe como 
# parametro o valor que você quer excluir
num.remove(9)
print(num)

print('------------------------------')
print('Segunda Lista')
print('------------------------------')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

#Podemos percorrer uma lista utilizando o for

for c, v in enumerate(valores):
    
    print('Na posição {} encontrei o valor {}!'.format(c, v))

print('Cheguei no final da lista')


print('------------------------------')
print('Terceira Lista')
print('------------------------------')

#Podemos igualar as listas por exemplo:

a = [2,3,4,7]
# Se fizermos b receber a, o python ira duplicar a lista, ou seja, ao 
# manipular a lista, eu consigo manipular automaticamente a lista b
b = a

print('Lista a: {}'.format(a))
print('Lista b: {}'.format(b))

b[2] = 8

print('Lista a: {}'.format(a))
print('Lista b: {}'.format(b))







