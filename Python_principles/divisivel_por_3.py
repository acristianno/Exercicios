"""Defina uma função nomeada div_3 que retorne True se seu único parâmetro inteiro for divisível por 3 e False caso
contrário.
Por exemplo div_3(6) é True porque não deixa nenhum resto. No entanto div_3(5) é False porque 5/3 sobra 2."""


def div_3(numero):
    if numero % 3 == 0:
        return True
    else:
        return False


n = int(input("Digite un número: "))
print(div_3(n))
