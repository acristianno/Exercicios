"""O objetivo deste desafio é analisar uma string binária consistindo apenas de zeros e uns.
Seu código deve encontrar o maior número de zeros consecutivos na string. Por exemplo, dada a string:

"1001101000110"
O maior número de zeros consecutivos é 3.

Defina uma função nomeada consecutive_zeros que receba um único parâmetro, que é a sequência de zeros e uns.
Sua função deve retornar o número descrito acima."""


def consecutive_zeros(numero_binario: str):
    cont = 0
    zeros = 0
    for i in numero_binario:
        if i == "0":
            cont += 1
        else:
            if cont >= zeros:
                zeros = cont
            cont = 0
    return zeros


print(consecutive_zeros("1001101000110"))
print((consecutive_zeros("101000101100100001001000")))
