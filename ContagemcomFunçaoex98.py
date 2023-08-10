# Faça um programa que tenha uma função chamada contador(), que receba 3 
# parametros: inicio, fim e passo e realize a contagem. Seu programa
# tem que realizar ters contagens através da função criada: 
# de 1 até 10, de 1 em 1
# de 10 até 0, de 2 em 2
# uma contagem personalizada


from time import sleep # método de intervalo de impressão

# Criação do método contador que não recebera nenhum parametro
def contador():
    # contador de 1 até 10
    print('Contagem de 1 até 10')
    for c in range(1,11):
        
        print(c)
        
        sleep(1)
    
    print('-' * 30)
    
    # contador de 10 até 0 de 2 em 2
    print('Contagem regressiva de 10 até 0 em passo 2')
    for d in range(10, 0 - 2, -2):
        
        print(d)
        sleep(1)
    
    print('-' * 30)
    
    # contador personalizado
    inicio = (int(input('Valor inicial: ')))
    
    fim = (int(input('Valor final: ')))
    
    passo = (int (input('Quantidade de passos: ')))
    
    print('Contagem de {} até {} de {} em {}'.format(inicio,fim,passo,passo))
    
    for p in range(inicio,fim + 1,passo):
        
        print(p)
        sleep(1)
    
    if inicio > fim:
    
        for p in range(inicio,fim , -passo):
            
            print(p)
            sleep(1)
        
    
    

# Programa principal / chamada do método
contador()
    
        