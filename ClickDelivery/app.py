import os

restaurantes = ['Pizza', 'Sushi']

def exibir_nome_do_app():
    print("""
░█████╗░██╗░░░░░██╗░█████╗░██╗░░██╗  ██████╗░███████╗██╗░░░░░██╗██╗░░░██╗███████╗██████╗░██╗░░░██╗
██╔══██╗██║░░░░░██║██╔══██╗██║░██╔╝  ██╔══██╗██╔════╝██║░░░░░██║██║░░░██║██╔════╝██╔══██╗╚██╗░██╔╝
██║░░╚═╝██║░░░░░██║██║░░╚═╝█████═╝░  ██║░░██║█████╗░░██║░░░░░██║╚██╗░██╔╝█████╗░░██████╔╝░╚████╔╝░
██║░░██╗██║░░░░░██║██║░░██╗██╔═██╗░  ██║░░██║██╔══╝░░██║░░░░░██║░╚████╔╝░██╔══╝░░██╔══██╗░░╚██╔╝░░
╚█████╔╝███████╗██║╚█████╔╝██║░╚██╗  ██████╔╝███████╗███████╗██║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░
░╚════╝░╚══════╝╚═╝░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚══════╝╚══════╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░
""")
    
def finalizar_app():
    os.system('cls')
    print('Encerrando app...')
    
def exibir_opcoes(): 
    print('1 - Cadastrar Restaurante')
    print('2 - Listar Restaurantes')
    print('3 - Ativar Restaurante')
    print('4 - Sair\n')

def opcao_invalida():
    print('Opcao invalida')
    input('Digite qualquer tecla para voltar ao menu principal: ')
    main()
    
def cadastrar_novo_restaurante():
    os.system('cls')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    input('Digite qualquer tecla para voltar ao menu principal: ')
    print('\n')
    main()

def listar_restaurantes():
    os.system('cls')
    print('Listando restaurantes:\n')
    for i in restaurantes:
        print(f'- {i}')
    input('Digite qualquer tecla para voltar ao menu principal: ')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))
        
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar Restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


    
def main():
    exibir_nome_do_app()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()