# Podemos utilizar um break para interromper laços
# Vamos novamente Fazer o exercicio de parar a execução
# ao digitar 999

n = 0
soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    
    
    soma = soma + n

print('Soma dos valores informados: {}'.format(soma))
 