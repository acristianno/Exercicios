"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
preço total."""
from math import ceil


def orcamento(metros_a_serem_pintaos):
    litros_a_serem_usados = metros_a_serem_pintaos / 3
    quantidade_de_latas = ceil(litros_a_serem_usados / 18)
    preco_lata = 80
    preco_total = preco_lata * quantidade_de_latas
    return quantidade_de_latas, preco_total


area_em_metros_quadrados = float(input("Informe a quantidade de metros quadrados: "))
cotacao_pintura = orcamento(area_em_metros_quadrados)
print(f'Para pintar {area_em_metros_quadrados} metros quadrados, é necessario {cotacao_pintura[0]} latas de tinta.\n'
      f'O preço total do pedido é R$ {cotacao_pintura[1]}')
