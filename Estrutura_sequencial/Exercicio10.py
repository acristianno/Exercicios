# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

def conversortemp(celsius):
    fahren = (celsius * 9/5) + 32
    return fahren


temp = float(input("Informe a temperatura em graus celsius: "))
print(f'{temp}° Celsius, correnponde a {conversortemp(temp)}° Fahrenheit.')