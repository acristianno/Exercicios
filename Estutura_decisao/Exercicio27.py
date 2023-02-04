"""Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos
e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente."""
from funcoes import valor_maca, valor_morango

peso_maca = int(input("Insira a quantidade de Maça: "))
peso_morango = int(input("Insira a quantidade de Morango: "))
print("Total da compra")
print(f'{peso_maca} Kilos de Maça = R$ {valor_maca(peso_maca):.2f}')
print(f'{peso_morango} Kilos de Morando = R$ {valor_morango(peso_morango):.2f}')
valor_total = valor_morango(peso_morango) + valor_maca(peso_maca)
print(f'O valor total dos produtos é R$ {valor_total:.2f}')
if peso_morango + peso_maca > 8 or valor_total > 25:
    desconto = valor_total * 10 / 100
    print(f'O valor do desconto foi de R$ {desconto:.2f}')
    print(f'Valor final R$ {valor_total - desconto:.2f}')

