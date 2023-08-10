#criar uam variável que recebe valor do usuário
b=input('escreva algo')
#verificar o tipo
print('tipo ',type(b))
#verificar se possui apenas espaços
print('tem espaço ',b.isspace())
#conferir se é um dado numérico
print('È um numero ',b.isnumeric())
#conferir se é um dado alfabético
print('È alfabetico ',b.isalpha())
#conferir se é um alfanumérico
print('è alfa numerico ',b.isalnum())
#conferir se é um alfanumérico

#para verificar se é em maiusculo
print('è maiusculo ',b.isupper())
#para verificar se é minusculo
print ('è minusculo ',b.islower())
#verificar se esta capitalizada
print(' è capitalizada',b.istitle())