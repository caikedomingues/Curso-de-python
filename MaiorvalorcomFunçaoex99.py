# Faça um programa que tenha uma função chamada maior(), que
# receba varios parametros de valores inteiros. Seu programa 
# tem que analisar todos os valores e dizer qual deles é o
# maior.
# Seu programa tem que analisar todos os valores e dizer qual deles é o
# maior


def maior():
    
    maior = 0
        
    cont = 0
    
    while True:
         
        valor = int(input('Informe um valor: '))
        
        cont = cont + 1
        
        
        if valor > maior:
            
            maior = valor
        
        while True: 
            
            resp = str(input('Você quer continuar? S/N ')).upper()[0]
            
            if resp in 'SN':
                
                break
            print('Erro, digite apenas S ou N ')
            
        if resp == 'N':
            
            break
        
    print('Maior valor: {}'.format(maior))
    print('Você infomou {} valores'.format(cont))
    
    


# Programa principal

maior()
        
        
        