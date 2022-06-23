# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

periodo = input("Turnos:\nM - Matutino\nV - Vespertino\nN - Noturno\nInforme em que perido estuda (M,V ou N) : ").upper()
if periodo == "M":
    print("Bom dia")
elif periodo == "V":
    print("Boa tarde")
elif periodo == "N":
    print("Boa noite")
else:
    print("Valor inválido")