"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
- par ou ímpar;
- positivo ou negativo;
- inteiro ou decimal."""
from funcoes import inteiro_ou_decimal, par_ou_impar, positivo_ou_negativo

numero1 = float(input("Informe un número: "))
numero2 = float(input("Informe un número: "))
escolha = int(input("Escolha\n1 - Para saber se o número é par ou ímpar\n2 - "
                    "Para saber se o número é positivo ou negativo."
                    "\n3 - Para saber se o número é inteiro ou decimal: "))
if escolha == 1:
    print(par_ou_impar(numero1))
    print(par_ou_impar(numero2))
elif escolha == 2:
    print(positivo_ou_negativo(numero1))
    print(positivo_ou_negativo(numero2))
elif escolha == 3:
    print(inteiro_ou_decimal(numero1))
    print(inteiro_ou_decimal(numero2))
