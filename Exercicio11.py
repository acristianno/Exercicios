# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# (a) o produto do dobro do primeiro com metade do segundo .
# (b) a soma do triplo do primeiro com o terceiro.
# (c) o terceiro elevado ao cubo.

numint = []
for i in range(0, 2):
    numint.append(int(input("Informe um número inteiro: ")))

numreal = float(input("informe um número real: "))
exercicioa = (numint[0] * 2) * (numint[1] / 2)
exerciciob = (numint[0] * 3) + numreal
exercicioc = numreal ** 4
print(f'Exercicio (a), resultado: {exercicioa}')
print(f'Exercicio (b), resultado: {exerciciob}')
print(f'Exercicio (c), resultado: {exercicioc}')
print(numint[0])
