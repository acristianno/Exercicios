"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
 Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
 São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
 João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
 Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que
 João deverá pagar. Imprima os dados do programa com as mensagens adequadas."""

kilos = float(input("Infome o total de Quilos de peixe: "))
if 50 >= kilos > 0:
    print("A quantidade informada está dentro do regulamento.")
elif kilos > 50:
    excesso = (kilos - 50)
    multa = float(excesso * 4)
    print(f'O peso exedeu o limite regulamentado em {excesso}kilos,\n'
          f'A multa a ser paga é de R$ {multa:.2f}.')
else:
    print(f'O peso {kilos} está errado.')
