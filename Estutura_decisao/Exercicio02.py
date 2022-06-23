# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = int(input("Informe um número: "))
if valor < 0:
    print(f'O número {valor} é negativo.')
elif valor > 0:
    print(f'O número {valor} é positivo.')
else:
    print(f'O número {valor} é neutro.')
