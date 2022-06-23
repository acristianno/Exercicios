"""Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou
não bissexto."""


def ano_bissexto(ano_a_ser_analisado):
    resultado = f'O ano {ano_a_ser_analisado} não é bissexto'
    if ano_a_ser_analisado % 4 == 0:
        if ano_a_ser_analisado % 100 != 0:
            resultado = f'O ano {ano_a_ser_analisado} é bissexto'
        else:
            if ano_a_ser_analisado % 400 == 0:
                resultado = f'O ano {ano_a_ser_analisado} é bissexto'
    return resultado


while True:
    try:
        ano = int(input("Informe o ano a ser analisado: "))
        if 0 < ano:
            break
        print("Valores inválidos.")
    except ValueError:
        print("Valores inválidos.")

print(ano_bissexto(ano))
