"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for
A, B ou C ou “REPROVADO” se o conceito for D ou E."""


def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media <= 4:
        conceito = "E"
    elif media <= 6:
        conceito = "D"
    elif media <= 7.5:
        conceito = "C"
    elif media <= 9:
        conceito = "B"
    else:
        conceito = "A"
    return conceito, media


def conceito_impresso(nota1, nota2, conceito):
    if conceito[0] in "ABC":
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    return f'\nAs notas informadas foram:' \
           f'\nNota 01 = {nota1}' \
           f'\nnota 02 = {nota2}' \
           f'\nA média ficou em {conceito[1]}' \
           f'\nO conceito é {conceito[0]}' \
           f'\nResultado final: {resultado}'


while True:
    try:
        nota01 = float(input("Informe a primeira parcial: "))
        nota02 = float(input("Informe a segunda parcial: "))
        if 0 <= nota01 <= 10 and 0 <= nota02 <= 10:
            break
        print("O valor aceito é de zero a 10.")
    except ValueError:
        print("Você não pode colocar letras ou caracteres especiais!!!")
media_parcial = calcular_media(nota01, nota02)
boletim_impresso = conceito_impresso(nota01, nota02, media_parcial)
print(boletim_impresso)
