from datetime import datetime, timedelta, date, time

data_inicial = datetime(2023, 1, 1)
data_final = datetime(2023, 10, 1)

# Calcular a diferença
diferenca = data_final - data_inicial
print(f"Diferença: {diferenca.days} dias")