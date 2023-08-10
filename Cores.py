
# Vamos trabalhar com cores no terminal

# Ja temos a tabela do padrão ansi compativel com python

# Como primeiro exercicio vamos tentar escrever olá mundo em vermelho com

# com fundo amarelo

print('\033[31;43mOlá mundo')

# Vamos criar mais um exercicio
a = 3
b = 5

print('Os valores são \033[33m {} e \033[32m{}'.format(a, b))

