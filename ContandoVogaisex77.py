# Crie um programa que tenha uma tupla com várias palavras (não usar 
# acentos). Depois disso você deve mostrar, para cada palavra, quais 
# são vogais

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')

for p in palavras:
    
    print('\n Na palavra {} temos  '.format(p.upper()))
    
    for letra in p:
        
        if letra.lower() in 'aeiou':
            
         print(letra, end = ' ')