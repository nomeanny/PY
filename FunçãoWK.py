import os

# Caminho do diretorio que vocÊ deseja percorrer
caminho = '/caminho/para/o/diretorio'

# Usando os.walk() para visitar toos os subdiretorios
for raiz, diretorios, arquivos, in os.walk(caminho):
    print(f'Diretorio atual: {raiz}')
    for diretorio in diretorios:
        print(f'  Subdiretorio: {diretorio}')
    for arquivo in arquivos:
        print(f'  Arquivo: {arquivo}')