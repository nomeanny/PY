from datetime import datetime, timedelta, date, time

data_string = "01/10/2023 14:30:00"
data_hora = datetime.strptime(data_string, "%d/%m/%Y %H:%M:%S")
print("Data e hora a partir da string: ", data_hora)