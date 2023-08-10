 # Faça um programa que leia um ano qualquer e mostre se ele é bissexto
 
 # e caso o usuário aperte o programa ira analisar o ano atual
 
 
 # As regras que determinam um ano bissexto é: ocorrer de quatro em quatro
 
 # anos, e ser divisivel por quarto e não divisivel por 100 e ser divisivel
 
 # por 400

# para pegar o ano atual que esta configurado no computador, basta
# importamos a biblioteca datatime e usar a função date

from datetime import date
ano = int(input('Qual ano você quer analisar? '))

if ano == 0:
    
    ano = date.today().year
    
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    
    print('O ano {} é bissexto'.format(ano))
    
else:
    
    print('O ano {} não é bissexto'.format(ano))