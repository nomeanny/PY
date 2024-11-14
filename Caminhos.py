import os

caminho_relativo = 'documentos/relatorio.txt'
caminho_absoluto = os.path.abspath(caminho_relativo)
print(caminho_absoluto)

if os.path.exists(caminho_absoluto):
    print("O diretório existe")
else:
    print("O diretório não existe")

if os.path.isfile(caminho_absoluto):
    print("É um arquivo.")
elif os.path.isdir(caminho_absoluto):
    print("É um diretório.")