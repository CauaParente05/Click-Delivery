# Click-Delivery

Aplicativo de linha de comando (CLI) em Python para gerenciamento de restaurantes cadastrados em uma plataforma de delivery. O usuário interage por um menu no terminal, podendo cadastrar novos restaurantes, listar os já cadastrados e alternar seu status entre ativo/inativo.

Este é um projeto de estudo, atualmente em uma versão procedural. Uma nova versão orientada a objetos está planejada.

## Funcionalidades

- **Cadastrar Restaurante**: registra um novo restaurante informando nome e categoria (o restaurante entra desativado por padrão).
- **Listar Restaurantes**: exibe uma tabela com nome, categoria e status (ativado/desativado) de todos os restaurantes cadastrados.
- **Alterar Estado do Restaurante**: busca um restaurante pelo nome e alterna seu status entre ativado e desativado.
- **Sair**: encerra a execução do programa.

## Estrutura do projeto

```
ClickDelivery/
└── app.py   # Ponto de entrada e toda a lógica do menu/CLI
```

## Requisitos

- Python 3.10 ou superior (o projeto usa `match/case`, disponível a partir do Python 3.10)

## Como executar

```bash
python ClickDelivery/app.py
```

Ao iniciar, o menu principal é exibido com as opções disponíveis:

```
1 - Cadastrar Restaurante
2 - Listar Restaurantes
3 - Alterar Estado do Restaurante
4 - Sair
```

Basta digitar o número da opção desejada e seguir as instruções exibidas no terminal.

## Observações

- Os dados dos restaurantes são armazenados em memória (lista Python), ou seja, são perdidos ao encerrar o programa.
- O comando de limpeza de tela (`os.system('cls')`) é específico do Windows; em Linux/macOS, substitua por `clear` caso necessário.
