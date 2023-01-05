"""Defina uma função chamada convert que receba uma lista de números como o seu único parâmetro
e retorne uma lista de cada número convertido em uma 'string'.

Por exemplo, a chamada deve retornar .convert([1, 2, 3])["1", "2", "3"]

O que torna isso complicado é que o corpo da função deve conter apenas uma única linha de código."""


def convert(lista):
    nova_lista = [str(i) for i in lista]
    return nova_lista


lis = [7, 2, 4]
print(convert(lis))
