"""Aqui está a história por trás deste desafio: imagine que você está escrevendo um jogo da velha, onde o tabuleiro se
parece com isso:

1:  X | O | X
   -----------
2:    |   |
   -----------
3:  O |   |

    A   B  C

A placa é representada como uma lista 2D:

board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]
Imagine se seu usuário entrar "C1" e você precisar ver se tem um X ou O naquela célula do quadro. Para fazer isso,
você precisa traduzir da string "C1" para linha 0 e coluna 2 para que você possa verificar board[row][column].
Sua tarefa é escrever uma função que possa traduzir de strings de comprimento 2 para uma tupla (row, column).
Dê um nome à sua função get_row_col; ele deve ter um único parâmetro que é uma string de comprimento 2 consistindo de
uma letra maiúscula e um dígito.
Por exemplo, a chamada get_row_col("A3") deve retornar a tupla (2, 0) porque A3 corresponde à linha no índice 2 e à
coluna no índice 0 no arquivo"""
from random import choice
from time import sleep
# O desafio pedia apenas a função get_row_col, porém já aproveitei e desenvolvi o jogo. jogo está rodando, com todas as
# funcionalidades, impressao de mapa, jogada do computador. Esta simples, tem muito espaço para melhorias ainda, mas o
# desenvolvi usando apenas meus conhecimentos de logica.

board = [  # Mapa do jogo
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]
campos_disponiveis = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]  # lista de jogadas disponiveis

jogador = "X"
maquina = "0"


def adiciona_jogada_mapa(jogada, player):  # funcao para adicionar a jogada no mapa
    linha = get_row_col(jogada)[0]
    coluna = get_row_col(jogada)[1]
    board[linha][coluna] = player
    for x in board:
        print(x)


def get_row_col(jogada: str):  # Função pedida no exercicio, entrada uma str e saída linha e coluna
    linha = int(jogada[1]) - 1
    coluna = jogada[0].upper()
    if coluna == "A":
        coluna = 0
    elif coluna == "B":
        coluna = 1
    else:
        coluna = 2
    return linha, coluna


def verificador_de_jogadas(jogada):  # Usado para verificas se a jogada está disponivel
    if jogada in campos_disponiveis:
        campos_disponiveis.remove(jogada)
        return True
    else:
        return False


def jogada_maquina():  # função que realiza o cumpatador fazendo uma jogada
    escolha_maquina = choice(campos_disponiveis)
    verificador_de_jogadas(escolha_maquina)
    return escolha_maquina


def vitoria(mapa, player):  # função para verificar a condição de vitoria
    for num in range(0, 3):
        if mapa[num][0] == player and mapa[num][1] == player and mapa[num][2] == player:
            return True
        elif mapa[0][num] == player and mapa[1][num] == player and mapa[2][num] == player:
            return True
    if mapa[0][0] == player and mapa[1][1] == player and mapa[2][2] == player:
        return True
    elif mapa[0][2] == player and mapa[1][1] == player and mapa[2][0] == player:
        return True
    else:
        return False


while True:
    jogada_usuario = str(input("Informe a sua jogada: ").upper())
    jogada_liberada = verificador_de_jogadas(jogada_usuario)
    if jogada_liberada:
        adiciona_jogada_mapa(jogada_usuario, jogador)
        venceu = vitoria(board, jogador)
        if venceu:
            print("Você venceu!!! parabéns!!!")
            break
        elif not campos_disponiveis:
            print("Jogo empatou")
            break
        print("Maquina escolhendo...")
        sleep(1)
        jogada_da_maquina = jogada_maquina()
        adiciona_jogada_mapa(jogada_da_maquina, maquina)
        venceu = vitoria(board, maquina)
        if venceu:
            print("DERROTA!!")
            break
    else:
        print("Campo já utilizado")
