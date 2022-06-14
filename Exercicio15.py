"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido."""


class Salario:

    def __init__(self, vhora, htrab):
        self.vhora = vhora
        self.htrab = htrab
        self.salariobruto = self.salbruto()
        self.impostorenda = self.descontos()[0]
        self.impostoinss = self.descontos()[1]
        self.sindicato = self.descontos()[2]
        self.salarioliquido = self.salliquido()

    def __str__(self):
        return f'+ Salario bruto : R$ {salario.salbruto():.2f}.\n- IR (11%) : R$ {salario.impostorenda:.2f}.' \
               f'\n- INSS(8%) : R$ {salario.impostoinss:.2f}.\n- Sindicato : R$ {salario.sindicato:.2f}.\n= ' \
               f'Salário liquido : R$ {salario.salarioliquido:.2f}.'

    def salbruto(self):
        salariobruto = self.htrab * self.vhora
        return salariobruto

    def descontos(self):
        impostorenda = self.salbruto() * 0.11
        inss = self.salbruto() * 0.08
        sindicato = self.salbruto() * 0.05
        impostos = [impostorenda, inss, sindicato]
        return impostos

    def salliquido(self):
        salarioliquido = self.salbruto() - sum(self.descontos())
        return salarioliquido


valorhora = float(input("Informe o valor recebido por hora: "))
horastrabalhadas = float(input("Informe a quantidade de horas trabalhadas: "))
salario = Salario(valorhora, horastrabalhadas)
print(salario)
