from pathlib import Path

# Criar um objeto Path
caminho = Path('diretorio/arquivo.txt')

# Verificar se o arquivo existe
if caminho.exists():
    print("O arquivo existe.")

# Criar um nvo diretorio
novo_diretorio = Path('novo_diretorio')
novo_diretorio.mkdir(exist_ok=True)

# Listar arquivos em um diretorio
for arquivo in novo_diretorio.iterdir():
    print(arquivo.name)