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


def inteiro_ou_decimal(numero):
    if numero % 1 == 0:  # aqui utilizo o resto da divisão, pois se tiver sobra, o número sera sempre um float
        return f"O número {numero} é do tipo inteiro."
    else:
        return f"O número {numero} é do tipo decimal"


def par_ou_impar(numero):
    numero_testado = inteiro_ou_decimal(numero)  # testa se o número é inteiro ou decimal
    if "inteiro" in numero_testado:  # Se o número for inteiro é usado resto da divisão por 2
        if numero % 2 == 0:
            return f"O número {numero} é par"
        else:
            return f"O número {numero} é impar"
    else:
        resto = round(numero % 2)  # O número sendo decimal, pega o resto da divisão e faz um novo teste
        if resto % 0.02 == 0:
            return f"O número {numero} é par"
        else:
            return f"O número {numero} é impar"


def positivo_ou_negativo(numero):
    if numero >= 0:
        return f"O número {numero} é positivo."
    else:
        return f"O número {numero} é negativo"


def checador_de_perguntas(pergunta):
    resultado = False
    pergunta = pergunta.upper().strip()
    if pergunta == "NAO" or pergunta == "SIM":
        resultado = True
    return resultado


def checa_tipo_combustivel(tipo_combustivel):
    tipo_combustivel = tipo_combustivel.upper()
    if tipo_combustivel == "A" or tipo_combustivel == "G":
        return True
