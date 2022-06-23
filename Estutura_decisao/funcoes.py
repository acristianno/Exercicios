"""def encontra_o_maior_numero(valores):
    maior = valores[1]
    if valores[2] < valores[0] > maior:
        maior = valores[0]
    elif valores[0] < valores[2] > valores[1]:
        maior = valores[2]
    return f'\nO maior valor informado foi {maior}.'

def encontra_o_menor_numero(valores):
    menor = valores[1]
    if valores[2] > valores[0] < menor:
        menor = valores[0]
    elif valores[0] > valores[2] < menor:
        menor = valores[2]
    return f'\nO menor valor informado é {menor}.'"""


def encontra_o_maior_numero(numeros):
    for b in range(2):
        for a in range(2):
            if numeros[a] < numeros[a+1]:
                numeros[a], numeros[a+1] = numeros[a+1], numeros[a]
    return f'\nO maior número informado foi {numeros[0]}'


def encontra_o_menor_numero(numeros):
    for b in range(2):
        for a in range(2):
            if numeros[a] < numeros[a+1]:
                numeros[a], numeros[a+1] = numeros[a+1], numeros[a]
    return f'\nO maior número informado foi {numeros[2]}'


def ano_bissexto(ano_a_ser_analisado):
    resultado = False
    if ano_a_ser_analisado % 4 == 0:
        if ano_a_ser_analisado % 100 != 0:
            resultado = True
        else:
            if ano_a_ser_analisado % 400 == 0:
                resultado = True
    return resultado
