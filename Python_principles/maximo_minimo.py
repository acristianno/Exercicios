"""Defina uma função nomeada largest_difference que tenha uma lista de números como seu único parâmetro.
Sua função deve calcular e retornar a diferença entre o maior e o menor número da lista.
Por exemplo, a chamada largest_difference([1, 2, 3]) deve retornar 2 porque 3 - 1 = 2
Você pode assumir que nenhum número é menor ou maior que -100 e 100."""


def largest_difference(lista_numeros):
    menor = lista_numeros[0]
    maior = lista_numeros[0]
    for numero in lista_numeros:
        if numero < menor:
            menor = numero
        elif numero > maior:
            maior = numero
    diferenca = maior - menor
    return f'O maior número informado foi {maior} o menor número informado foi {menor} a diferença entre os ' \
           f'números é {diferenca}'


lista = [-4, 5, 8, -7, 11, 2]
print(largest_difference(lista))
