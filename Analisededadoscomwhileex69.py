# crie um programa que leia a idade e o sexo de várias pessoas. A 
# cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final mostre: 
# quantas pessoas tem mais de 18 ANOS.
# quantos homens foram cadastrados.
# quantas mulheres tem menos de 20 anos.
tot18 = 0
tothomem = 0
totmulher = 0

while True:
   
   idade = int(input('Idade: '))
   sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
   resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

   if resp == 'N':
      
      break
   if idade < 18:
      tot18 = tot18 + 1
   
   if sexo == 'M':
      tothomem = tothomem + 1
      tot18 = tot18 + 1
   
   if sexo == 'F' and idade < 20:
      totmulher = totmulher + 1
      tot18 = tot18 + 1

print('Maiores de 18: {}'.format(tot18))
print('Homens cadastrados: {}'.format(tothomem))
print('Mulheres menores de 20 anos: {}'.format(totmulher))


