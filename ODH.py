from datetime import datetime, timedelta, date, time

# Criar um objeto de data
data_especifica = date(2023, 10, 1) # Ano, Mês, Dia
print("Data Especifica: ", data_especifica)

# Criar um objeto de hora
hora_especifica = time(14, 30, 0) # Hora, Minuto, Segundo
print("Hora Especifica: ", hora_especifica)

# Criar um objeto datetime
data_hora_especifica = datetime(2023, 10, 1, 14, 30, 0)
print("Data e Hora Especifica: ", data_hora_especifica)