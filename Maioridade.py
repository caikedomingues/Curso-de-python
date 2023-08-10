

from datetime import date

anoatual = date.today().year

idade = 0

contMaiores = 0

contMenores = 0

for c in range(1,8):
    
    ano = int(input('Informe o ano da {}° pessoa: '.format(c)))
   
    idade = anoatual - ano 
    
    if idade >= 18:
        contMaiores = contMaiores + 1
         
    else:
        contMenores = contMenores + 1
    
print('Quantidade de maiores: {}'.format(contMaiores))
print('Quantidade de menores: {}'.format(contMenores))