"""Escreva uma função que pegue uma lista de listas e a nivele em uma lista unidimensional.
Dê um nome à sua função flatten. Ele deve receber um único parâmetro e retornar uma lista.

Por exemplo, chamando:

flatten([[1, 2], [3, 4]])
Deve retornar a lista:
[1, 2, 3, 4]"""


def flaten(lista):
    nova_lista = []
    for i in lista:
        for j in i:
            nova_lista.append(j)
    return nova_lista


teste = [[1, 2], [3, 4]]
print(flaten(teste))
