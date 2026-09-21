# Cração de listas

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# nomes = ["Luffy", "Zoro", "Sanji", "Nami"]

# ano = [2005, 2026]

# Criando lista e usando for loop para percorre-la

# i = 0 

# for n in numeros:
#     print(f"{i+1}° numero: {n}")
#     i += 1
    
# for loop para calcular a soma dos numeros impares de 1 a 10

# impar = 0

# for i in range(1, 11):
#     if i % 2 != 0:
#         impar += i
        
# print(impar)

# for loop imprimindo de 1 a 10 em ordem decrescente

# for i in range(10, 0, -1):
#     print(i, '\n')

# Tabuada de um numero via input do usuario

# n = int(input("Digite um numero: "))

# for i in range(1, 11):
#     r = i*n
#     print(f"{n} x {i} = {r}")

# Soma de numeros numa lista com for loop e tratamento de erro.

# try:
#     n = [1, 2, 3, None]

#     for num in n:
#         num += num
        
#     print(num)
# except TypeError as e:
#     print("Valor invalido na lista. Erro: {e}")
# except ValueError as e:
#     print("Valor invalido na lista. Erro: {e}")

# Calculando a media de valores numa lista e tratamento de erro para divisão por zero e para listas vazias

# n = [5, 10, 20, 40, 80]

# soma = 0

# try:
#     for num in n:
#         soma += num
        
#     media = int(soma / len(n))

#     print(media)
# except ZeroDivisionError as e:
#     print("Divisão por zero. Erro: {e}")
# except NameError as e:
#     print("Lista vazia. Erro: {e}")