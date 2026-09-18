import os

restaurantes = [{'nome': 'Teste', 'categoria': 'Teste', 'ativo':        False}, 
                {'nome': 'Burgos Pizza', 'categoria': 'Pizza', 'ativo': True}]

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
    linha = '-' * len(titulo)
    print(linha)
    print(f'{titulo}')
    print(f'linha\n')
    
def exibir_opcoes(): 
    print('1 - Cadastrar Restaurante')
    print('2 - Listar Restaurantes')
    print('3 - Alterar Estado do Restaurante')
    print('4 - Sair\n')

def opcao_invalida():
    print('Opcao invalida')
    voltar_ao_menu()
    
    
def cadastrar_novo_restaurante():
    exibe_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_restaurante, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu()

def listar_restaurantes():
    exibe_subtitulo('Listando restaurantes: ')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        status_restaurante = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante} | {categoria_restaurante} | {status_restaurante}')      
    voltar_ao_menu()

def ativar_restaurante():
    exibe_subtitulo(f'Alterar estado do Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar ou desativar: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'Restaurante: {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'Restaurante: {nome_restaurante} foi desativado com sucesso!'
    print(f'mensagem\n')
    if not restaurante_encontrado:
        print('Restaurante não encontrado\n')
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