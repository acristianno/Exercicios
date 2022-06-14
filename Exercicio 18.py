"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de
Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

tamanho_arquivo = float(input("Informe o tamanho do arquivo em (MB) para download: "))
velocidade_internet = float(input("Informe a velocidade da conexão com a internet: "))
arquivo_em_kb = tamanho_arquivo * 1024
internet_em_kb = velocidade_internet * 1024 / 8
tempo_de_download = float(arquivo_em_kb / internet_em_kb) / 60
print(arquivo_em_kb, internet_em_kb)
print(f'Seu downloado será efetuado em {tempo_de_download:.2f} Minutos.')
