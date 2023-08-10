
# A função help tem como finalidade apresentar um manual do python e todos
# os seus metodos e parametros
#help(input('Informe a sua dúvida sobre o python: '))

# Podemos também coletar informações sobre o python através do comando
# doc


#print(input.__doc__)



# Vamos utilizar agora a função docstring que basicamente, serve para 
# apresentar o manual de uma função que foi criada pelo programador

def contador(i, f, p):
    # Basicamente, poderemos escrever o manual da função que queremos
    # criar
    
    """
    param i : inicio
    param f: fim
    param p : passo
    return: sem retorno
    """
    
    c = 1
    
    while c <= f:
        
        print('{}'.format(c))
        c = c + p

# Após a digitação do manual for concluida, basta executarmos o help,
# com o nosso método como parametro

help(contador)

# Paramtros opcionais: Serve para  atribuirmos um valor padrão a um dos
# parametros, ou seja, caso eu não coloque um valor no parametro ele já
# ira ter um valor padrão.

def somar(a, b, c = 0):
    
    s = a + b + c
    
    print('Soma: {}'.format(s))


somar(3,2)


# Basicamente a função return ira retornar a variável que iremos pedir
# e ira copiar a resposta que daremos para ela, ou seja, poderemos persona
# lizar as respostas colocando cada resultado em uma variável e imprimindo
# uma resposat diferente da outra
def som(a,b,c):
    
    s = a + b + c
    
    return s

r1 = som(3,2,5)
r2 = som(1,3,2)
r3 = som(2,4,2)

print('Meus cálculos deram: {}, {}, {}'.format(r1,r2,r3))
    