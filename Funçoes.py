# Vamos começar os estudos criando uma função que imprima linha entre as
# frases ou palavras
#  def significa definição da função

def mostraLinha():
    
    print('------------------------------------')
    
# Agora vamos testar a utilização de funções com parametros

def mensagem(msg):
    
    print(msg)

#Programa principal
print('Cadastro')
mostraLinha()
print('Resultado')
mostraLinha()


#Programa principal
mensagem('Ola mundo')
mensagem('Curso em video')
mensagem('Python é muito bom')

# Criação de uma função que realiza a soma de 2 numeros

def soma(a, b):
    
    s = a + b
    print(s)
    

#Programa principal

soma(4, 5)
soma(8, 9)
soma(2, 1)

# O coniceito de empacotamento no python implica que um método pode receber
# uma quantidade indeterminada de arumentos e é simbolizado por um *

def contador(* num):
    
    print(num)
    

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


