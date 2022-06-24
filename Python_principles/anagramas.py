"""Duas cordas são anagramas se você puder fazer uma a partir da outra reorganizando as letras.
Escreva uma função chamada is_anagram que receba duas strings como seus parâmetros. Sua função deve retornar True se as
strings forem anagramas e False caso contrário.
Por exemplo, a chamada is_anagram("typhoon", "opython") deve retornar True enquanto a chamada is_anagram("Alice", "Bob")
deve retornar False."""


def is_anagram(texto1, texto2):
    anagrama = []
    for letra in texto1:
        if letra in texto2:
            anagrama.append(letra)
    if len(anagrama) == len(texto2):
        return True
    else:
        return False


palavra1 = input("Digite uma palavra: ")
palavra2 = input("Digite outra palavra: ")
print(is_anagram(palavra1, palavra2))
