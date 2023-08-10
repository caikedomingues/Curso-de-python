#Conversor de medidas

medida = float(input("Qual a distância em metros? "))

cm = medida * 100
mm = medida * 1000

print('A distância {:.2f} em centimetros é {:.2f}'.format(medida,cm))
print( 'A distância {:.2f} em milimetros é: {:.2f}'.format(medida,mm))
