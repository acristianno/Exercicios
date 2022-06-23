"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas
de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de
tintas a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde
os valores para cima, isto é, considere latas cheias."""
from math import ceil, floor


class Orcamento:

    def __init__(self, area_a_ser_pintada):
        self.area_com_folga = area_a_ser_pintada * 1.1
        self.litros_a_serem_usados = self.area_com_folga / 6
        self.preco_latas = 80
        self.preco_galao = 25

    def __str__(self):
        return f'{self.orcamento_latas()}\n{self.orcamento_galoes()}\n{self.orcamento_otimizado()}'

    def orcamento_latas(self):
        latas = ceil(self.litros_a_serem_usados / 18)
        orcamento_latas = self.preco_latas * latas
        return f'Usando apenas Latas de 18 litros - Precisará de {latas} latas e ficará no valor de ' \
               f'R$ {orcamento_latas}.'

    def orcamento_galoes(self):
        galoes = ceil(self.litros_a_serem_usados / 3.6)
        orcamento_galoes = self.preco_galao * galoes
        return f'Usando apenas Galôes de 3.6 litros - Precisara de {galoes} galoes e ficará no valor de ' \
               f'R$ {orcamento_galoes}.'

    def orcamento_otimizado(self):
        latas_otimizado = floor(self.litros_a_serem_usados / 18)
        galoes_otimizado = ceil((self.litros_a_serem_usados % 18) / 3.6)
        orcamento_latas = self.preco_latas * latas_otimizado
        orcamento_galoes = self.preco_galao * galoes_otimizado
        valor_final = orcamento_galoes + orcamento_latas
        return f'Usando {latas_otimizado} latas e {galoes_otimizado} galões o valor final ficará R$ {valor_final}.'


area_em_metros_quadrado = float(input("Informe a quantidade de metros quadrados: "))
orcamemto = Orcamento(area_em_metros_quadrado)
print(f'Lata de 18 litros : R$ 80,00. - Galão de 3,6 litros : R$ 25,00')
print(orcamemto)
