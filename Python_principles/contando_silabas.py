"""Defina uma função chamada count que recebe um único parâmetro. O parâmetro é uma string. A string conterá uma única
palavra dividida em sílabas por hífens, como estes:
"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"

Sua função deve contar o número de sílabas e devolvê-lo.Por exemplo, a chamada count("ho-tel") deve retornar 2"""


def count(palavra):
    contador = 1
    for letra in palavra:
        if letra == "-":
            contador += 1
    return contador


print(count("ho-tel"))
