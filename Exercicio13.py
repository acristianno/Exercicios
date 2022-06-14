# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

from Funcoes import pesoideal


def pesoidealmulher(altura):
    ideal = (62.1 * altura) - 44.7
    return ideal


alt = float(input("Informe a sua altura: "))
sexo = input("Informe seu sexo, M ou F: ").upper()
if sexo == 'M':
    print(f'Para a altura de {alt} metros, o peso ideal é {pesoideal(alt):.2f}kgs.')
elif sexo == 'F':
    print(f'Para a altura de {alt} metros, o peso ideal é {pesoidealmulher(alt):.2f}kgs.')
else:
    print(f'O sexo informado {sexo}, é invalido.')
