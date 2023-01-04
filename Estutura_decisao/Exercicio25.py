"""Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""
from funcoes import checador_de_perguntas

pergunta1 = "Telefonou para a vítima? "
pergunta2 = "Esteve no local do crime? "
pergunta3 = "Mora perto da Vítima? "
pergunta4 = "Devia para a vítima? "
pergunta5 = "Já trabalhou para a vítima? "
perguntas = {pergunta1, pergunta2, pergunta3, pergunta4, pergunta5}
clasificacao = ["Inocente", "Inocente", "Suspeito", "Cúmplice", "Cúmplice", "Assasino"]
sim = 0

for i in perguntas:
    while True:
        resposta = str(input(i))
        if checador_de_perguntas(resposta):
            if resposta.upper() == "SIM":
                sim = sim + 1
            break
        else:
            print("Responda com (sim) ou (não)")
print(clasificacao[sim])
