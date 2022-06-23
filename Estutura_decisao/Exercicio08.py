"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato."""
#from funcoes import encontra_o_menor_numero


def encontra_o_menor_numero(valores):
    menor = valores[1][1]
    if valores[2][1] > valores[0][1] < menor:
        menor = valores[0]
    elif valores[0][1] > valores[2][1] < menor:
        menor = valores[2]
    else:
        menor = valores[1]
    return f'\nO poduto mais barato é {menor[0]} R${menor[1]:.2f}.'


numero_por_extenso = ['primeiro', 'segundo', 'terceiro']
produtos = []
for i in range(3):
    produto = input(f'Digite o nome do {numero_por_extenso[i]} produto: ')
    valor = float(input(f'Digite o valor do {produto}: '))
    produtos.append([produto, valor])
print(encontra_o_menor_numero(produtos))
