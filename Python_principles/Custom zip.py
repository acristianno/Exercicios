"""A zip função interna compacta duas listas. Escreva a sua própria implementação dessa função.

Defina uma função chamada zap. A função recebe dois parâmetros a e b. Estas são listas.

A sua função deve retornar uma lista de tuplas. Cada tupla deve conter um item da lista a e um de b.

Se você não entender, pense num zíper.

Por exemplo:

    zap(
    [0, 1, 2, 3],
    [5, 6, 7, 8]
)
Should return:

[(0, 5),
 (1, 6),
 (2, 7),
 (3, 8)"""


def zap(lista1, lista2):
    zipado = []
    for i in range(3):
        zipado.append((lista1[i], lista2[i]))
    return zipado


lis1 = [2, 5, 6]
lis2 = [1, 4, 8]
print(zap(lis1, lis2))
