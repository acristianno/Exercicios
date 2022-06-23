#Faça um Programa que peça dois números e imprima o maior deles.

numeros = []
for i in range(0, 2):
    numeros.append(int(input("Digite um número: ")))
if numeros[0] >= numeros[1]:
    print(f"O maior número informado foi {numeros[0]}.")
else:
    print(f'O maior número informado foi {numeros[1]}.')
