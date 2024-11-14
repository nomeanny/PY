from pathlib import Path

# Caminho do diretorio que vôce deseja percorrer
caminho = Path('/caminho/para/o/diretorio')

# Usando rglob() para visitar todos os arquivos e subdiretorios
for item in caminho.rglob('*'):
    if item.is_dir():
        print(f'Diretorio: {item}')
    else:
        print(f'Arquivo: {item}')