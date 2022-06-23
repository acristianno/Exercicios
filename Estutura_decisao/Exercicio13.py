# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.

def dia_da_semana(dia_semana):
    if dia_semana == 1:
        dia_extenso = "Domingo"
    elif dia_semana == 2:
        dia_extenso = "Segunda"
    elif dia_semana == 3:
        dia_extenso = "Terça"
    elif dia_semana == 4:
        dia_extenso = "Quarta"
    elif dia_semana == 5:
        dia_extenso = "Quinta"
    elif dia_semana == 6:
        dia_extenso = "Sexta"
    else:
        dia_extenso = "Sábado"
    return dia_extenso


while True:
    try:
        dia = int(input("Informe o número correspondente ao dia da semana: "))
        if dia <= 7:
            break
        print("\nInforme um número entre 1 e 7!!!")
    except ValueError:
        print("Apenas números são aceitaveis.")
print(dia_da_semana(dia))
