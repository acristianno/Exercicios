# Faça um Programa que converta metros para centímetros.

def metroemcm(medida):
    cm = int(medida * 100)
    return cm


metro = float(input("Informa o valor em metros: "))
print(f'O valor {metro} metros é equivalente a {metroemcm(metro)} centimetros.')
