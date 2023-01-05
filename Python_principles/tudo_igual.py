"""Defina uma função chamada all_equal que recebe uma lista e
verifica se todos os elementos da lista são iguais.

Por exemplo, a chamada deve retornar .all_equal([1, 1, 1])True"""


def all_equal(lista):
    comparador = lista[0]
    for i in lista:
        if comparador != i:
            return False
    return True


lis = [2, 2, 2, 1, 1, 1]
print(all_equal(lis))
