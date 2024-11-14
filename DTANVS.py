from datetime import datetime, timedelta

# Data de nascimento
data_nascimento = datetime(2004, 5, 24)

# Data atual
data_atual = datetime.now()

# Calcular o proximo aniversario
proximo_aniversario = datetime(data_atual.year, data_nascimento.month, data_nascimento.day)

# Se o aniversario ja passou este ano, calcular para o proximo ano
if proximo_aniversario < data_atual:
    proximo_aniversario = datetime(data_atual.year + 1, data_nascimento.month, data_nascimento.day)

# Calcular a diferença em dias
dias_faltando = (proximo_aniversario - data_atual).days

print(f"Faltam {dias_faltando} dias para o proximo aniversario.")