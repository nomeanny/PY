import shutil

# Copiar um arquivo
shutil.copy('arquivo.txt', 'copia_arquivo.txt')

# Copiar um arquivo e preservar metadaddos
shutil.copy2('arquivo.txt', 'copia_arquivo_com_metadados.txt')