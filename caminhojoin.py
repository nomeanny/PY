import os

# Combinar partes de um caminho
diretorio = 'documentos'
arquivo = 'relatorio.txt'
caminho_completo = os.path.join(diretorio, arquivo)
print(caminho_completo)