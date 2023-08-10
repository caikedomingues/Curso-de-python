nome = str(input('Qual o seu nome? '))

if nome == 'caike':
    print('seu nome é bem bonito')

elif nome == 'pedro' or nome == 'paulo' or nome == 'maria':
    print('Seu nome é bem popular no brasil')
    
elif nome == 'Ana' or nome == 'claudia' or nome == 'jéssica' or nome == 'juliana':
   print('Que belo nome feminino') 
    
else:
    
    print('Seu nome é bem normal')

print('Tenha um bom dia {}'.format(nome))