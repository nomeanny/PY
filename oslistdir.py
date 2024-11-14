import os

# Listar arquivos e diretorios no diretorio atual
for item in os.listdir('.'):
    print(item)

# Usando os.scandir() para obter maisn informações
with os.scandir('.') as entries:
    for entry in entries:
        print(entry.name, entry.is_dir(), entry.is_file())