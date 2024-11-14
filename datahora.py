from datetime import datetime, timedelta, date, time

agora = datetime.now()
print("Data e hora atuais: ", agora)
agora_formatado = agora.strftime("%Y-%m-%d %H:%M:%S")
print("Data e hora atuais (formatada): ", agora_formatado)