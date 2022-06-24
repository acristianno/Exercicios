"""O objetivo deste desafio é, dado um dicionário de status online das pessoas, contar o número de pessoas que estão
online.
Por exemplo, considere o seguinte dicionário:

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

Nesse caso, o número de pessoas online é 2.
Escreva uma função chamada online_count que recebe um parâmetro. O parâmetro é um dicionário que mapeia de strings de
nomes para a string "online"ou "offline", como visto acima.
Sua função deve retornar o número de pessoas que estão online."""

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


def online_count(lista_usuarios):
    usuarios_online = 0
    for users in lista_usuarios.values():
        if "online" in users:
            usuarios_online += 1
    return f'O total de usuarios online é {usuarios_online}.'


print(online_count(statuses))
