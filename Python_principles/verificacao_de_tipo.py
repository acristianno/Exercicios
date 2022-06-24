"""Escreva uma função chamada only_ints que receba dois parâmetros. Sua função deve retornar True se ambos os parâmetros
forem inteiros e False caso contrário.
Por exemplo, chamar only_ints(1, 2) deve retornar True, enquanto chamar only_ints("a", 1) deve retornar False"""


def only_ints(parametro1, parametro2):
    try:
        int1 = int(parametro1)
        int2 = int(parametro2)
        if type(int1) and type(int2) == int:
            return True
    except ValueError:
        return False


inteiros = only_ints(1, 1)
print(inteiros)
