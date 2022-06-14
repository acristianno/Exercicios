# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

def calculosalario(horas, valor):
    salario = horas * valor
    return salario


nvalor = float(input("Informe o valor recebido por hora: "))
nhoras = int(input("Informa a quantidade de horas trabalhadas no mês: "))
print(f'\nVocê ganha R$ {nvalor} por hora, trabalhou {nhoras} horas nesse mês. '
      f'Seu salario sera de R$ {calculosalario(nhoras, nvalor)}')
