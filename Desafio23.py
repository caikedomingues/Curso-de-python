# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um
# dos digitos separados

# Ex: Digite um número: 1834
# unidade: 4 dezena: 3 centena: 8 milhar: 1
# Vamos realizar esse exercicio através de módulo

num = int(input("Informe um numero: "))
#Para descobrir a unidade devemos realizar a divisão inteira 
# do valor informado por 1 e tirar o seu módulo, ou seja, se pegarmos 
# o resto da divisão teremos o  ultimo numero do valor informado 
# ( a unidade ).


u = num // 1 % 10 #Unidade

#Para descobrir a dezena devemos realizar a divisão inteira d
# o valor informado por 10 e tirar o seu módulo, ou seja, se pegarmos 
# o resto da divisão teremos o  penultimo numero do valor informado 
# ( a dezena ).

d = num // 10 % 10 #Dezena


#Para descobrir a centena devemos realizar a divisão inteira 
# do valor informado por 100 e tirar o seu módulo, ou seja, se pegarmos 
# o resto da divisão teremos o  segundo numero do valor informado 
# ( a centena ).

c = num // 100 % 10 #Centena

#Para descobrir a dezena devemos realizar a divisão inteira 
# do valor informado por 1000 e tirar o seu módulo, ou seja, se pegarmos 
# o resto da divisão teremos o  primeiro numero do valor informado 
# ( a milhar ).

m = num // 1000 % 10 #Milhar

#impressão dos resultados
print('Analisando o numero {}'.format(num))

print('Unidade: {}'.format(u))

print('Dezena: {}'.format(d))

print('Centena: {}'.format(c))

print('Milhar: {}'.format(m))



