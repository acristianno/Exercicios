# Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.
from funcoes import inteiro_ou_decimal

print("---Analisador de número (inteiro / decimal)")
numero = float(input("Informe unnúmero: "))
print(inteiro_ou_decimal(numero))
