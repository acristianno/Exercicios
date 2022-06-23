# Faça um Programa que leia três números e mostre-os em ordem decrescente.

numeros = []
for i in range(3):
    numeros.append(int(input("Informe um número: ")))

for b in range(2):
    for a in range(2):
        if numeros[a] < numeros[a+1]:
            numeros[a], numeros[a+1] = numeros[a+1], numeros[a]
print(numeros)
