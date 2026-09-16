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
    
def voltar_ao_menu():
    input('\nDigite qualquer tecla para voltar ao menu principal: ')
    main()

def exibe_subtitulo(titulo):
    os.system('cls')
    print(titulo)
    print('\n')
   
def exibir_opcoes(): 
    print('1 - Cadastrar Restaurante')
    print('2 - Listar Restaurantes')
    print('3 - Ativar Restaurante')
    print('4 - Sair\n')

def opcao_invalida():
    print('Opcao invalida')
    voltar_ao_menu()
    
    
def cadastrar_novo_restaurante():
    exibe_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu()

def listar_restaurantes():
    exibe_subtitulo('Listando restaurantes: ')
    for restaurante in restaurantes:
        print(f'- {restaurante}')
        
    voltar_ao_menu()

def ativar_restaurante():
    exibe_subtitulo('Ativando Restaurante: ')
    voltar_ao_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))
        
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                ativar_restaurante()
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