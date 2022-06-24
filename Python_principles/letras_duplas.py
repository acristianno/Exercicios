"""O objetivo deste desafio é analisar uma string para verificar se ela contém duas letras iguais seguidas. Por exemplo,
a string "hello" tem l duas vezes seguidas, enquanto a string "nono" não tem duas letras idênticas seguidas.
Defina uma função chamada double_letters que recebe um único parâmetro. O parâmetro é uma string. Sua função deve
retornar True se houver duas letras idênticas em uma linha na string e False caso contrário."""


def double_letters(parametro):
    for i in range(len(parametro)):
        if i > 0:
            if parametro[i] == parametro[i-1]:
                return True
    return False


print(double_letters("bolsonaro"))
