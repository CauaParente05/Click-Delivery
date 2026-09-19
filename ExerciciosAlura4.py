# Dicionario com informações de uma Pessoa

# Pessoa = [{'nome': 'Tomas', 'idade': 31, 'cidade': 'Recife'}]

# Mundando os valores do dicionario criado

# for p in Pessoa:
#     p['idade'] = 32
    
# print(p['idade']) 

# for p in Pessoa:
#     p['emprego'] = 'TI'
    
# print(p)

# for p in Pessoa:
#     p.pop('emprego', None)
    
# print(p)

# Dicionario relacionando numeros de 1 a 5 aos seus respectivos quadrados

# quadrado_dos_numeros = {}

# for n in range(1, 6):
#     quadrado_dos_numeros[n] = n ** 2

# print(quadrado_dos_numeros)

# Verificando existencia de uma chave no dicionario
   
# Pessoa = [{'nome': 'Tomas', 'idade': 31, 'cidade': 'Recife'}]

# for p in Pessoa:
#     if 'nome'in Pessoa:
#         print("A chave 'nome' existe no dicionário.")
#     else:
#         print("A chave 'nome' não existe no dicionário.")

# frase = 'O tempo perguntou ao tempo quanto tempo o tempo tem mas o tempo disse ao tempo que o tempo tem o tempo que o tempo tem'

# contagem_palavras = {}

# palavras = frase.split()

# for palavra in palavras:
#     contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
# print(contagem_palavras)
