"""Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1."""

valor = int(input("Informe o valor a ser sacado: "))
if 10 < valor < 600:  # Validar se o valor está dentro do limite minimo e maximo de saque
    nota100 = valor // 100  # Identificar o número de cada cédula a ser utilizado
    valor -= nota100 * 100
    nota50 = valor // 50
    valor -= nota50 * 50
    nota10 = valor // 10
    valor -= nota10 * 10
    nota5 = valor // 5
    valor -= nota5 * 5
    nota1 = valor
    notas_sacadas = [[nota100, "100 Reais"], [nota50, "50 Reais"], [nota10, "10 Reais"], [nota5, "5 Reais"],
                     [nota1, "1 Real"]]  # lista contendo uma tupla da quantidade de cédulas e descrição do valor.
    for notas in notas_sacadas:
        if notas[0]:  # Verifica apenas as celudas utilizadas e as imprime
            cedulas = 'nota'
            if notas[0] > 1:  # Se for mais de uma nota mota a excrita para o plural
                cedulas = 'notas'
            print(f"{notas[0]} {cedulas} de {notas[1]}")
else:
    print("O valor minimo de saque é de R$ 10,00, o valor maximo é R$ 600\n"
          "Informe um valor valido.")




