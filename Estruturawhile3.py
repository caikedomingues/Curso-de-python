# Vamos tentar realizar outro exemplo, só q agora vamos perguntar se 
# o usuário quer informar mais um número

r = 'sim'

while r == 'sim':
    
    num = int(input('Informe um valor: '))
    r = str(input('Você quer informar mais um numero? sim/não '))
    