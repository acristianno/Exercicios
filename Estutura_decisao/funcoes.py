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


def calculo_combustiveis(litros, combustivel):
    alcool = 1.90
    gasolina = 2.50
    if combustivel.upper() == "G":
        valor = litros * gasolina
        if litros <= 20:
            valor_abastecido = valor - (valor * 0.04)
        else:
            valor_abastecido = valor - (valor * 0.06)
    else:
        valor = litros * alcool
        if litros <= 20:
            valor_abastecido = valor - (valor * 0.03)
        else:
            valor_abastecido = valor - (valor * 0.05)
    return valor_abastecido


def valor_maca(peso):
    if peso <= 5:
        valor = peso * 1.80
    else:
        valor = peso * 1.50
    return valor


def valor_morango(peso):
    if peso <= 5:
        valor = peso * 2.50
    else:
        valor = peso * 2.20
    return valor


class Compra:
    def __init__(self, tipo_carne, quantidade, metodo_pagamento):
        self.tipo_carne = tipo_carne.upper()
        self.quantidade = quantidade
        self.metodo_pagamento = metodo_pagamento.upper()

    def calculadora_de_carnes(self):
        valor, valor_kilo, desconto, valor_total = 0, 0, 0, 0
        if self.tipo_carne == "F":
            carne = "Filé Duplo"
            if self.quantidade <= 5:
                valor_kilo = 4.90
            elif self.quantidade > 5:
                valor_kilo = 5.80
        elif self.tipo_carne == "A":
            carne = "Alcatra"
            if self.quantidade <= 5:
                valor_kilo = 5.90
            elif self.quantidade > 5:
                valor_kilo = 6.80
        else:
            carne = "Picanha"
            if self.quantidade <= 5:
                valor_kilo = 6.90
            elif self.quantidade > 5:
                valor_kilo = 7.80
        valor = self.quantidade * valor_kilo
        if self.metodo_pagamento == "SIM":
            desconto = valor * 5 / 100
            valor_total = valor - desconto
        return f'- Produto = {carne}\n- Quantidade {self.quantidade} Kilos' \
               f'\n- Valor Kilo R${valor_kilo:.2f}\n- Valor R$ {valor:.2f}' \
               f'\n- Desconto R$ {desconto}\n- Valor final R$ {valor_total:.2f}'

    def __str__(self):
        return self.calculadora_de_carnes()
