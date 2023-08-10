# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No
# final do programa. Mostra:
# A media de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos

somaidade = 0
media = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1,5):
    # O strip remove os espaços em branco
    nome = str(input('Nome da {}° pessoa: '.format(p))).strip()
    idade = int(input('Idade da {}°pessoa: '.format(p)))
    sexo = str(input('Sexo da {}° pessoa [M/F]: ').format(p)).strip()
    somaidade = somaidade + idade
    media = somaidade / 4
    
    if p == 1 and sexo in 'm':
        maioridadehomem = idade
        nomevelho = nome
        
    if sexo in 'm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    
    if sexo in 'f' and idade < 20:
        totmulher20 = totmulher20 + 1
    print('--------------------------------------------')

print('A media de idade do grupo é: {}'.format(media)) 
print('Homem mais velho {}'.format(maioridadehomem,nomevelho))
print('Mulheres que são menores de 20: {}'.format(totmulher20))