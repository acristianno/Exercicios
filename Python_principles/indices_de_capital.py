"""Escreva uma função chamada capital_indexes. A função recebe um único parâmetro, que é uma string. Sua função deve
retornar uma lista de todos os índices na string que possuem letras maiúsculas.

Por exemplo, chamar deve retornar a lista .capital_indexes("HeLlO")[0, 2, 4]"""


def capital_indexes(texto):
    texto_formatado = texto.strip()
    letras_maiusculas = []
    for i in range(len(texto_formatado)):
        if texto_formatado[i].isupper():
            letras_maiusculas.append(i)
    return letras_maiusculas


entrada_texto = input("Escreva uma palavra/frase e retornarei onde está as letras maiusculas: ")
print(capital_indexes(entrada_texto))
