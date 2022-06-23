"""Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada
por aluno e apresentar:
- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez."""
# função para calcular a média, optei por escrever o codigo e encontar maneiras de resolver o problema, sem usar as
# bibliotecas do python, nessa caso poderia ter utilizado (media = sum(notas) / len(notas))


def calcula_media(lista):
    media = 0
    cont = 0
    for valor in lista:
        media += valor
        cont += 1      # Utilização de contador para descobrir o tamanho do iteravel.
    media = media / cont
    if media == 10:
        return f'O aluno teve média {media:.2f} e foi aprovado com distinção.'
    elif 10 > media >= 7:
        return f'O aluno teve média {media:.2f} e foi aprovado.'
    else:
        return f'O aluno teve média {media:.2f} e foi reprovado.'


notas = []
for nota in range(1, 3):
    notas.append(float(input(f"Digita a {nota} nota do aluno: ")))
print(calcula_media(notas))
