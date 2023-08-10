

idade = int(input('Qual a sua idade? '))

if idade < 18:
    
    print('Você ainda não pode se alistar')
    
    calcidade = 18 - idade
    
    print('Ainda faltam {} anos para você se alistar'.format(calcidade))
    
elif idade == 18:
    
    print('você tem que realizar o seu alistamento obrigatório')
    
else:
    calcidade = idade - 18
    print('o seu alistamento devia ter sido feito há {} anos'.format(calcidade))