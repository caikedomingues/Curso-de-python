# Crie um pequeno sistema modularizado que permite cadastrar pessoas pelo 
# seu nome e idade em um arquivo de texto simples. O sistema só vai ter
# 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas

# Na minha versão simplificada eu criei uma lista de escopo global 
clientes = []
# Crie um loop aleatório que tem a função de repetir o processo quantas vezes eu quiser
while True:

    # Nesse programa, eu trabalhei o conceito de tratamento de erros, então coloquei todo o código
    # dentro de um try, para podermos inspecionar todo o código
    try:
       #Criação do menu com as instruçoes para o usuário
        print('-' * 30)
        print('Cadastro de clientes'.center(30))
        print('-' * 30)
        print('Escolha uma opção'.center(30))
        print('1 - para cadastrar um novo cliente')
        print('2 - para apresentar a lista: ')
        print('3 - para sair do programa')
        print('-' * 30)
        
        # Leitor de opções
        opcao = int(input('Sua opção: '))
        
        
        # Estrutura condicional que verificara as opções escolhidas
        if opcao == 1:
            # se a opção for 1: Vamos pedir o nome e a idade  do usuário e 
            # adiciona-los na lista dentro de um try para verificar se os valores
            # passados são os corretos
            
            try:
               # Inserção dos dados na lista
               clientes.append(str(input('Nome do cliente: ')).strip())
               clientes.append(int(input('Idade do cliente: ')))
              #Except da opção 1 
            except(ValueError,TypeError):
                
                print('Por favor, insira os dados corretos')
        
        elif opcao == 2:
            # Se a opção for 2: ele ira mostrar todos os cadastros
            print('-' * 30)
            print('Confira os usuários cadastrados')
            print('-' * 30)
            #Impressão dos dados cadastrados
            print(clientes)
        
        elif opcao == 3:
            #SE a opção for 3: ele vai encerrar o programa
            print('Programa encerrado, volte sempre')
            break
        
        elif opcao > 4 or opcao < 1:
            # se a opção for maior que 3 ou menor que 1, ele apresentara
            # a mensagem de valor inválido
            print('Valor inválido')
            
    # except da opção
    except (ValueError, TypeError):
        
        print('Valor inválido, informe novamente')
    #except para encerramento duranye a execução do prog
    except KeyboardInterrupt:
        
        print('O usuário encerrou o programa durante a execução ')
        break
        
        
            



