import sys

# O primeiro argumento é o nome do script
script_name = sys.argv[0]

# Verifica se há argumentos suficientes
if len(sys.argv) > 2:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    print(f"Nome do script: {script_name}")
    print(f"Argumento 1: {arg1}")
    print(f"Argumento 2: {arg2}")
else:
    print("Erro: por favor, forneça dois argumentos adicionais.")