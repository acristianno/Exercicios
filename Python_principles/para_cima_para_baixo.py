"""Para cima e para baixo
Defina uma função nomeada up_down que receba um único número como parâmetro. Sua função retorna uma tupla
contendo dois números; o primeiro deve ser um inferior ao parâmetro, e o segundo deve ser um superior.
Por exemplo, chamar up_down(5) deve retornar (4, 6)"""


def up_down(numero: int):
    maior = numero + 1
    menor = numero - 1
    return menor, maior


print(up_down(5))
