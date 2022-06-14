# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

def areaquadrado(ladoa, ladob):
    area = ladoa * ladob
    dobroarea = area * 2
    return dobroarea


lados = []
for i in range(0, 2):
    lados.append(int(input("informe o valor do lado do quadrado: ")))

print(f'Os lados infomados foram {lados[0]} e {lados[1]}, o dobro de sua área é {areaquadrado(lados[0], lados[1])}')
