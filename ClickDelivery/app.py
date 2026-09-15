import os

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

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))
        
        match opcao_escolhida:
            case 1:
                print('Cadastrar Restaurante')
            case 2:
                print('Listar Restaurantes')
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