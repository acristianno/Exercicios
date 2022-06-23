# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

from Funcoes import pesoideal


alt = float(input("Informe a sua altura: "))
print(f'Para a altura de {alt} metros, o peso ideal é {pesoideal(alt):.2f}kgs.')
