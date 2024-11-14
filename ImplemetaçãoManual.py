import os

def visitar_diretorio(caminho):
    # Listar todos os itens no diretorio atual
    for item in os.listdir(caminho):
        caminho_completo = os.path.joib(caminho, item)
        if os.path.isdir(caminho_completo):
            print(f'Diretorio: {caminho_completo}')
            # Chamada recursiva para visitar o subdiretorio
            visitar_diretorio(caminho_completo)
        else:
            print(f'Arquivo: {caminho_completo}')

# Caminho do diretorio que você deseja percorrer
caminho_inicial = '/caminho/para/o/diretorio'
visitar_diretorio(caminho_inicial)