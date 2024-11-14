from datetime import datetime, timedelta, date, time

agora = datetime.now()
data_iso = agora.isoformat()
print("Data e hora em formato ISO:", data_iso)

# Converter uma string ISO de volta para um objeto datetime
data_iso_string = "2023-10-01T14:30:00"
data_iso_obj = datetime.fromisoformat(data_iso_string)
print("Data e hora a partir da strinf ISO:", data_iso_obj)