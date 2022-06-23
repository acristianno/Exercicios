"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver
o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
-salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5%
Após o aumento ser realizado, informe na tela:
-o salário antes do reajuste;
-o percentual de aumento aplicado;
-o valor do aumento;
-o novo salário, após o aumento."""


def reajuste_salarial(salario):
    salario_com_reajuste = 0
    valor_do_aumento = 0
    percentual_de_aumento = ""
    if 0 < salario <= 280:
        valor_do_aumento = salario * 0.20
        salario_com_reajuste = salario + valor_do_aumento
        percentual_de_aumento = "20%"
    elif 280 < salario <= 700:
        valor_do_aumento = salario * 0.15
        salario_com_reajuste = salario + valor_do_aumento
        percentual_de_aumento = "15%"
    elif 700 < salario <= 1500:
        valor_do_aumento = salario * 0.10
        salario_com_reajuste = salario + valor_do_aumento
        percentual_de_aumento = "10%"
    elif 1500 < salario > 1500:
        valor_do_aumento = salario * 0.05
        salario_com_reajuste = salario + valor_do_aumento
        percentual_de_aumento = "5%"
    return f'O salário informado foi R$ {salario}\nEsse valor se enquadra em um aumento de {percentual_de_aumento}' \
           f'\nO valor de aumento é de R$ {valor_do_aumento}\nO novo salário após o aumento é de ' \
           f'R$ {salario_com_reajuste}'


while True:
    salario_inicial = float(input("Informe e salario R$: "))
    if salario_inicial > 0:
        break
print(reajuste_salarial(salario_inicial))
