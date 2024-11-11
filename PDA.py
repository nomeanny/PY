# Processamento de arquivo
Largura = 79
with open("entrada.txt", "r") as entrada:
    for linha in entrada.readlines():
        if linha[0] == ";":
            continue
        elif linha[0] == ">":
            print(linha[1:].rjust(Largura))
        elif linha[0] == "*":
            print(linha[1:].center(Largura))
        else:
            print(linha)