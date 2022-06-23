"""Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e
unidades do mesmo. Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades -  12 = 1 dezena e 2 unidades Testar com:
326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16"""


def impressao_numerica(numeral):
    un = 0
    dez = 0
    cen = 0
    for i in range(numeral):
        un += 1
        if un > 9:
            dez += 1
            un = 0
        if dez > 9:
            cen += 1
            dez = 0
            un = 0
    if un == 0:
        valorun = ""
    elif un == 1:
        valorun = "unidade"
    else:
        valorun = "unidades"
    if dez == 0:
        valordez = ""
    elif dez == 1:
        valordez = "dezena"
    else:
        valordez = "dezenas"
    if cen == 0:
        valorcen = ""
    elif cen == 1:
        valorcen = "centena"
    else:
        valorcen = "centenas"
    if valorcen and valordez and valorun:
        return f'{cen} {valorcen}, {dez} {valordez} e {un} {valorun}'
    elif ((valorcen and not valordez) or (not valorcen and valordez)) and valorun:
        return f'{cen or dez} {valorcen or valordez} e {un} {valorun}'
    elif valorcen and ((valordez and not valorun) or (not valordez and valorun)):
        return f'{cen} {valorcen} e {dez or un} {valordez or valorun}'
    else:
        return f'{cen or dez or un} {valorcen or valordez or valorun}'


"""while True:
    try:
        numero = int(input("Informe um número entre 1 e 1000: "))
        if 0 < numero < 1000:
            break
    except ValueError:
        print("Informe o valor corretamente!")"""
lista = [326, 300, 100, 320, 310, 305, 301, 311, 25, 20, 10, 21, 11, 1, 7, 16]
for numero in lista:
    print(impressao_numerica(numero))
