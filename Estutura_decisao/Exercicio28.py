"""O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente
receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade
de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne,
preço total, tipo de pagamento, valor do desconto e valor a pagar."""
from funcoes import Compra


while True:
    print("(F) - Filé / (A) - Alcatra / (P) - Picanha")
    tipo_carne = input("Informe o tipo de carne: ")
    carnes = ["F", "A", "P"]
    if tipo_carne.upper() in carnes:
        quantidade = float(input("Infome a quantidade desejada: "))
        pagamento = input("Pagamento com cartão Tabajara?: ")
        compra = Compra(tipo_carne, quantidade, pagamento)
        print(compra)
        break
    else:
        print("Escolha invalida!")
