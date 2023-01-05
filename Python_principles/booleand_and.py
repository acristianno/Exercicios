"""Defina uma função chamada triple_and que receba três parâmetros e
retorne True somente se forem todos True e False caso contrário."""


def triple_and(parametro1, parametro2, parametro3):
    if parametro1 and parametro2 and parametro3:
        return True
    else:
        return False


one = True
two = True
three = False
print(triple_and(one, two, three))
