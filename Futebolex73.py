#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do
# campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:

# apenas os 5 primeiros colocados da tabela 

# os 4 ultimos colocados da tabela

# uma lista com os times em ordem alfabética 

# em que posição da tabela está o time da chapecoense


times = ('Botafogo', 'Flamengo', 'Gremio', ' São Paulo', 'Fluminense', 
         'Palmeiras', 'Bragantino', 'Athletico - PR', 'Fortaleza', 
         'Cruzeiro', 'Internacional', 'Atlético - MG', 'Cuiaba', 'Santos',
         'Corinthians', 'Bahia', 'Goias', 'Coritiba', 'Vasco da gama',
         'América-mg')

print('Tamanho da tupla: {}'.format(len(times)))

print('------------------------------------------------')

print('Os 5 primeiros colocados da tabela: {}'.format(times[0:5]))

print('------------------------------------------------')

print('Os 4 ultimos colocados da tabela: {}'.format(times[16:20]))

print('------------------------------------------------')

print('lista dos times em ordem alfabética: {}'.format(sorted(times)))

print('------------------------------------------------')
print( 'Posição do Gremio: {}'.format(times.index('Gremio') + 1 ))






