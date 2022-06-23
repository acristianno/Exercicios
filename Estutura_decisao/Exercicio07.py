# Faça um Programa que leia três números e mostre o maior e o menor deles.
from funcoes import encontra_o_maior_numero, encontra_o_menor_numero

numeros = []
for i in range(3):
    numeros.append(int(input("Informe um número: ")))
print(encontra_o_maior_numero(numeros))
print(encontra_o_menor_numero(numeros))
