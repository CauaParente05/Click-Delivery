# Determina se um número é par ou impar

n = int(input('Numero:'))

if n % 2 == 0:
    print('Par\n')
else:
    print('impar')
    
# Classificando idade do usuário com if/else

idade = int(input('Digite sua idade: '))

if idade <= 12:
    print('Criança')
elif idade >= 13 and idade < 18:
    print('Adolescente')
else:
    print('Adulto')

# Verificando usuario e senha com if/else

usuario = input('Digite seu usuário: ')
senha = int(input('Digite sua senha: '))

if usuario == 'Cauã' and senha == 12345:
    print('Usuário e senha corretos')
else:
    print('Senha ou usuário incorretos')

# Coordenadas num plano cartesiano, determinando os quadrantes com if/else

x = float(input('X: '))
y = float(input('Y: '))

if x > 0 and y > 0: 
    print('Primeiro Quadrante')
elif x < 0 and y > 0:
    print('Segundo Quadrante')
elif x < 0 and y < 0:
    print('Terceiro Quadrante')
elif x > 0 and y < 0:
    print('Quarto Quadrante')
else:
    print('O ponto esta localizado no eixo ou origem')