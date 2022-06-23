# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

def conversortemperatura(fahren):
    celsius = 5 * ((fahren-32) / 9)
    return celsius


temp = int(input("Informe a temperatura em Fahrenheit: "))
print(f'{temp}º Fahrenheit, conrresponde a {conversortemperatura(temp):.2f}º Celsius.')
