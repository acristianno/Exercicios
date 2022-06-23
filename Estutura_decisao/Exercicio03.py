"""Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino,
M - Masculino, Sexo Inválido."""

sexo = input("Informe o sexo | M - Masculino ou F - Feminino | = ").upper()
if sexo == "M":
    print(f'O sexo informado foi {sexo} - Masculino.')
elif sexo == "F":
    print(f'O sexo informado foi {sexo} - Feminino.')
else:
    print("O sexo informado é inválido.")
