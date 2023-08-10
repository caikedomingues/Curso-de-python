# Crie um programa que tenha uma função fatorial() que receba dois
# parametros: o primeiro que indique o numero a calcular e o outro chamado
# show, que será o valor lógico(opcional) indicando se será mostrado
# ou não na tela o processo de calculo fatorial

def fatorial(num, show = False):
    """
    Calcula o fatorial de um numero
    param num: o numero que deve ser calculado
    return: f, que será o valor do cálculo do fatorial
    """
    f = 1
    c = 1
    for c in range(num, 0, -1):
        
        if show:
            print(c,end=' ')
            if c > 1:
                print(' x ',end = ' ')
            else:
                print(' = ', end = ' ')
        f = f * c
        
    return f

n = int(input('Digite um número: '))


print('O fatorial de {} é igual a {}'.format(n, fatorial(n, show=True)))

help(fatorial)