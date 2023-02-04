"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo
cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90."""
from funcoes import checa_tipo_combustivel, calculo_combustiveis

while True:
    tipo_combustivel = input("Informe o tipo de combustivel a ser abastecido: (A) Alcool - (G) Gasolina: ")
    if checa_tipo_combustivel(tipo_combustivel):
        try:
            litragem = float(input("Informe a quantidade de litros a ser abastecido: "))
            if litragem > 0:
                print(calculo_combustiveis(litragem, tipo_combustivel))
                break
            else:
                print("Insira uma litragem valida!")
        except ValueError:
            print("Insira um litragem valida!")
    else:
        print("Insira um tipo de combustivel válido")
