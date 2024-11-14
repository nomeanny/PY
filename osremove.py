import os

# Excluir um arquivo
os.remove('arquivo.txt')

# Excluir um diretorio vazio
os.rmdir('diretorio_vazio')

# Excluir um diretorio não vazio
import shutil
shutil.rmtree('diretorio_com_conteudo')