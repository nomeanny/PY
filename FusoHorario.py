from datetime import datetime, timezone, timedelta

# Criar um objeto timezone para UTC
utc = timezone.utc

# Obter a data e hora atuais em UTC
agora_utc = datetime.now(utc)
print("Data e hora atuais em UTC:", agora_utc)

# Cirar um fuso horario especifico (ex: UTC-3)
brt = timezone(timedelta(hours=-3))
agora_brt = datetime.now(brt)
print("Data e hora atuais em BRT (UTC-3):", agora_brt)