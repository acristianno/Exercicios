# Faça um Programa que leia três números e mostre o maior deles.
from funcoes import encontra_o_maior_numero

numeros = []
for i in range(3):
    numeros.append(int(input("Informe um número: ")))
print(encontra_o_maior_numero(numeros))
