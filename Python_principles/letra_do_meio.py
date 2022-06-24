#Escreva uma função chamada mid receba uma string como parâmetro. Sua função deve extrair e retornar a letra do meio.
#Se não houver uma letra do meio, sua função deve retornar a string vazia.
#Por exemplo, deve retornar e deve retornar .mid("abc")"b"mid("aaaa")""
from math import trunc


def mid(parametro):
    if len(parametro) % 2 == 0:
        return ""
    indice = trunc(len(parametro) / 2)
    parametro_retorno = parametro[indice]
    return parametro_retorno


frase = input("Digite um texto e vou retornar a letra do meio: ").strip()
print(mid(frase))
