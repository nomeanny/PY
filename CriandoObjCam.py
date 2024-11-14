from pathlib import Path

# Criar um objeto Path
caminho = Path('documentos/arquivo.txt')
print(caminho)

caminho_completo = Path('documentos').joinpath('arquivo.txt')
print(caminho_completo)

caminho_absoluto = caminho.resolve()
print(caminho_absoluto)

if caminho.exists():
    print("O caminho existe.")
else:
    print("O caminho não existe.")

if caminho.is_file():
    print("É um arquivo.")
elif caminho.is_dir():
    print("É um diretório.")

# Listar todos os arquivos e diretórios
for item in Path('documentos').iterdir():
    print(item)

# Listar arquivos com uma extensão específica
for txt_file in Path('documentos').glob('*.txt'):
    print(txt_file)