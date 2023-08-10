#Vamos criar um exercicio que verifique o tipo do dado infromado
a = input("Digite a algo: ")
#Na hora da impressão deveos utilizar o metodo type que recebe como parametr
# a variável que deve ser analisada
print("O tipo primitivo desse valor é: ", type(a))

#Vamos testar se o valor informado possui só espaços, para isso,
#utlizamos o método isspace que retorna um valor booleano

print("Só tem espaços? " , a.isspace())

#para conferir se é um dado numérico, usamos o, método isNumeric
print("É um numero? ", a.isnumeric())

#para conferir se é alfabético usamos o método isAlpha

print("É alfabético? " , a.isalpha()) 

#para conferir se é alfanumérico usamos o método isalnum

print("É alfanumérico? ", a.isalnum())

#para verificar se o valor informado esta em maiusculo usamos o isupper
print('Está em maiusculas? ', a.isupper())

#para verificar se o valor informado está minusculo usamos o islower
print("Está em minusculas? ", a.islower())

#para verificar se está capitalizada
print("Está capitalizada ", a.istitle())

