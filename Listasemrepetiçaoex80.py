#Crie um programa onde o usuário possa digitar 5 valores numéricos e
# cadastre -os em uma lista, já na posição correta de inserção sem usar 
# o sort. No final mostre a lista ordenada na tela


# Priemiro temos que criar a lista que irá receber os valores

lista = []
# Criação do for que ira pedir 5 valores
for c in range(0,6):
    #Variável que ira receber os valores informados
    n = int(input('Informe o {}° valor: '.format(c + 1)))
    
    #Vamos criar um if para verificar a posição do valor digitado
    
    # se a 1° posição for iguai a 0, vamos apenas adicionar o primeiro
    # valor informado na primeira posição
    
    if c == 0:
        lista.append(n)
        
    #Agora vamos verificar se o próximo valor é maior que o primeiro valor
    # informado. Para isso, basta verificar se o n é maior que o tamanho
    # da lista menos 1, usamos -1 para comparar com o ultimo valor 
    # informado, também podemos colocar apenas lista[-1]
    
    elif n > lista[len(lista) - 1]:
        
        lista.append(n)   
    
    else:
        
        # nesse caso, a vamos criar uma variável pos = 0 que é a 1° 
        # posição e percorrer a lista com while  da primeira posição até a 
        # última posição, sendo assim enquanto pos for menor que o
        # tamanho da lista ele ira verificar se n é menor ou igual a 
        # a lista na posição 0.
        
        pos = 0
        while pos < len(lista):
            # Se essa condição for verdadeira iremos usar o método insert
            # para colocar o valor na posição pos o valor n e parar o 
            # a condição
            if n <= lista[pos]:
                lista.insert(pos,n)
                break
        pos = pos + 1
print('Os valores digitados em ordem crescente foram: {}'.format(lista))
            
            
         
    
    
    
    