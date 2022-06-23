"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
-Salário Bruto até 900 (inclusive) - isento
-Salário Bruto até 1500 (inclusive) - desconto de 5%
-Salário Bruto até 2500 (inclusive) - desconto de 10%
-Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00"""


class Salario:
    def __init__(self, pagamento_hora, horas_trabalhadas):
        self.salario_bruto = pagamento_hora * horas_trabalhadas
        self.valor_desc_ir = self.imposto_renda()[1]
        self.porc_desc_ir = self.imposto_renda()[0]
        self.sindicato = self.salario_bruto * 0.03
        self.fgts = self.salario_bruto * 0.11
        self.salario_liquido = self.salario_bruto - self.total_descontos

    def __str__(self):
        return f'\nSalário Bruto:        :R$ {self.salario_bruto:.2f}' \
               f'\n(-) IR ({self.porc_desc_ir})          :R$ {self.valor_desc_ir:.2f}' \
               f'\n(-) Sindicato (3%)    :R$ {self.sindicato:.2f}' \
               f'\n(-) FGTS (11%)        :R$ {self.fgts:.2f}' \
               f'\nTotal de descontos    :R$ {self.total_descontos:.2f}' \
               f'\nSalário Liquido       :R$ {self.salario_liquido:.2f}'

    def imposto_renda(self):
        porcentagem_desc_ir = "0%"
        valor_desc_ir = 0
        if 900 < self.salario_bruto <= 1500:
            porcentagem_desc_ir = "5%"
            valor_desc_ir = self.salario_bruto * 0.05
        elif 1500 < self.salario_bruto <= 2500:
            porcentagem_desc_ir = "10%"
            valor_desc_ir = self.salario_bruto * 0.10
        elif self.salario_bruto > 2500:
            porcentagem_desc_ir = "20%"
            valor_desc_ir = self.salario_bruto * 0.20

        return porcentagem_desc_ir, valor_desc_ir

    @property
    def total_descontos(self):
        total_descontos = self.valor_desc_ir + self.sindicato
        return total_descontos


while True:
    try:
        valor_hora = float(input("Informe o valor recebido por hora R$: "))
        quantidade_de_horas = int(input("Informe a quantidade de horas trabalhadas no mês: "))
        if valor_hora > 0 and quantidade_de_horas > 0:
            break
    except ValueError:
        print("Apenas números são aceitos!!!")
folha_de_pagamento = Salario(valor_hora, quantidade_de_horas)
print(folha_de_pagamento)
