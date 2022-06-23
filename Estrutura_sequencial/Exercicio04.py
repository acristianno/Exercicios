# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas = []
for i in range(0, 4):
    notas.append(int(input('Informe uma nota: ')))
print(f'A média das notas informadas é: {sum(notas)/4}')
