# Vamos iniciar os exercicios realizando o calculo de fatorial usando
# funçoes

# criação da função fatorial com paramtro opcional de valor 1
def fatorial(num = 1):
    #Valor inicial da variável f
    f = 1
    
    # for que ira realizar a contagem e a multiplicação dos valores
    
    for c in range(num,0,-1):
        #Calculo do fatorial
        f = f * c
        # retorno do resultado do calculo
        return f


n = int(input('Digite um numero: '))
fatorial(n)
print('O fatorial do numero {} é igual a  {}'.format(n, fatorial(n)))

    
    