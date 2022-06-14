# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

from math import pi


def areacirculo(raio):
    area = pi*(raio**2)
    return area


num = float(input("Informe o raio de um círculo: "))
print(f'O raio informado foi {num}, sua área é {areacirculo(num):.2f}')
