
#Programa que permite o cadastro de quantos veiculos o usuário quiser. após o cadastro o programa verifica se a uma multa a ser cobrada
# e o valor do aluguel

# ira guardar a quantidade de veiculos que devem ser cadastrados
quantCadastro = int(input('Quantos veiculos você quer cadastrar? '))

#Estrutura de repetição que ira executar o processo de cadastro quantas vezes for necessário
for cont in range(0, quantCadastro):
    # Coleta dos dados
    print('----------------------------------')
    codigo = int(input('Código do veiculo: '))
    nome = str(input('Dono do veiculo: '))
    marca = str(input('Marca do veiculo: '))
    modelo = str(input('Modelo do veiculo: '))
    preco = float(input('Valor do veiculo: '))
    valorLoc = float(input('Valor da locação '))
    diasLoc = int(input('Dias de locação: '))
    print('----------------------------------')
    
    # Calculo da multa
    # se a quantidade de dias de locação for maior que o valor da locação 
    if diasLoc > valorLoc:
        #  devemos calcular a diferença e atribuir 15% por cento ao valor
        sub = diasLoc - valorLoc
        div = sub / 100
        multa = div + sub
        # Impressão do resultado
        print('valor da multa')
    else:
        print('Não ha nada a ser cobrado')
    
    #calculo do aluguel
    # Calculo da multa explicado anteriormente
    sub = diasLoc - valorLoc
    div = sub / 100
    multa = div + sub
    #Resultado final do aluguel
    aluguel = (diasLoc * valorLoc) + multa
    #Impressão dos resultados finais
    print('Código do veiculo: {}'.format(codigo))
    print('Dono do veiculo: {}'.format(nome))
    print('Marca: {}'.format(marca))
    print('Modelo: {}'.format(modelo))
    print('valor do veiculo: {}'.format(preco))
    print('valor da locação: {}'.format(valorLoc))
    print('Dias de locação: {}'.format(diasLoc))
    print('Valor do aluguel: {}'.format(aluguel))
    
    