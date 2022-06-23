"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. Dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes;"""


def teste_triangulo(lado01, lado02, lado03):
    if lado01 + lado02 > lado03 and lado01 + lado03 > lado02 and lado02 + lado03 > lado01:
        if lado01 == lado02 == lado03:
            triangulo = "Triângulo equilátero"
        elif lado01 == lado02 or lado01 == lado03 or lado02 == lado03:
            triangulo = "Triângulo isóceles"
        else:
            triangulo = "Triângulo Escaleno"
    else:
        triangulo = "Os valores informados não formam um triângulo."
    return triangulo


while True:
    try:
        lado1 = int(input("Informe o primeiro lado do triângulo: "))
        lado2 = int(input("Informe o segundo lado do triângulo: "))
        lado3 = int(input("Informe o terceito lado do triângulo: "))
        if lado1 > 0 and lado2 > 0 and lado3 > 0:
            break
        print("Insira valores validos!!!")
    except ValueError:
        print("Apenas números são aceitos.")

print(teste_triangulo(lado1, lado2, lado3))
