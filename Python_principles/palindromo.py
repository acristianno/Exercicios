"""Uma string é um palíndromo quando é a mesma quando lida de trás para frente.
Por exemplo, a string "bob"é um palíndromo. Assim como é "abba". Mas a string "abcd" não é um palíndromo,
porque "abcd" != "dcba"
Escreva uma função chamada palindrome que receba uma única string como parâmetro.
Sua função deve retornar True se a string for um palíndromo e False caso contrário."""


def palindrome(palavra):
    tamanho = len(palavra) - 1
    palindromo = ""
    for i in range(tamanho, -1, -1):
        palindromo += palavra[i]
    if palavra == palindromo:
        return True
    else:
        return False


print(palindrome("abba"))
