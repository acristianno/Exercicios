"""Defina uma função, random_number, que não receba parâmetros. A função deve gerar um inteiro aleatório entre 1 e 100,
ambos inclusive, e devolvê-lo.
Chamar a função várias vezes deve (geralmente) retornar números diferentes.
Por exemplo, chamar random_number()algumas vezes pode primeiro retornar 42, depois 63, depois 1."""
import time
from math import floor, pi


def random_number():
    tempo_monotico = time.monotonic()
    tempo_arredondado = floor(tempo_monotico)
    numero_aleatorio = floor((tempo_monotico - tempo_arredondado) * 100 * pi)
    numeros = []
    for i in range(1, 101):
        numeros.append(i)
    cont = 0
    numero_randomico = 0
    for i in range(numero_aleatorio):
        numero_randomico = numeros[cont]
        cont += 1
        if i % 100 == 0:
            cont = 0
    return numero_randomico


print(random_number())
