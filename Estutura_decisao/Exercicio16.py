"""Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir
os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;"""
from math import sqrt


def equacao_segundo_grau(valora, valorb, valoc):
    delta = valorb * valorb - (4 * valora * valoc)
    if delta < 0:
        return "Delta menor que zero, as raizes são imaginarias"
    elif delta == 0:
        raiz = -valorb / (2 * valora)
        return f"Delta = 0, a raiz encontrada é {raiz}"
    else:
        raiz1 = (-valorb + sqrt(delta)) / (2 * valora)
        raiz2 = (-valorb - sqrt(delta)) / (2 * valora)
        return f"Delta positivo, as raizes encontradas são {raiz1:.4f} e {raiz2:.4f}"


a = float(input("Insira o valor de a: "))
if a == 0:
    print("A equação não é de segundo grau!")
else:
    b = float(input("Insira o valor de b: "))
    c = float(input("Insira o calor de c: "))
    equacao = equacao_segundo_grau(a, b, c)
    print(equacao)
