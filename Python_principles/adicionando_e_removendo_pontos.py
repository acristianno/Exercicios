"""Escreva uma função chamada add_dots que recebe uma string e adiciona "." entre cada letra. Por exemplo, chamar
add_dots("test") deve retornar a string "t.e.s.t" Então, abaixo da add_dots função, escreva outra função chamada
remove_dots que remova todos os pontos de uma string. Por exemplo, chamar remove_dots("t.e.s.t") deve retornar "test".
Se ambas as funções estiverem corretas, a chamada remove_dots(add_dots(string))deve retornar o original string para
qualquer string. (Você pode assumir que a entrada para add_dots não contém pontos.)"""


def add_dots(palavra):
    dot_palavra = ""
    for letra in palavra:
        dot_palavra += letra + "."
    return dot_palavra[:-1]


def remove_dots(palavra_dot):
    palavra = ""
    for letra in palavra_dot:
        if letra != ".":
            palavra += letra
    return palavra


palavra_add_ponto = add_dots("nicola tesla")
palavra_remove_ponto = remove_dots(palavra_add_ponto)
print(palavra_add_ponto)
print(palavra_remove_ponto)
