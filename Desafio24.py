# Crie um programa que leia o nome de uma cidade e diga se ela começa ou 
# não com o nome "Santo"

#Para realizar a contagem com mais precisão precisamos eliminar da 
# contagem os espaços em brancos

cid = str(input('Qual o nome da cidade '))

#Para evitar que o programa não entenda as diferentes formas(minusculas e
# maiusulas) de se escrever santo vamos convertertudo que for escrito em
# minusculo para maiusculo, Assim, ele conseguira comparar os valores e
# devolver um valor booleano(verdadeiro ou falso). Como a palavra santo
#possui 4 letras, vamos pedir para ele verificar os valores até o indice
# 5 assim, ao chegar no valor ele ira isolar e verificar apenas os outros 
# 4 valores

print(cid[:5].upper() == 'SANTO')
