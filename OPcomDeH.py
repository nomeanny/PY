from datetime import datetime, timedelta, date, time

# Define agora
agora = datetime.now()
# Adicionar 10 dias à data atual
nova_data = agora + timedelta(days=10)
print("Data após 10 dias:", nova_data)

# Subtrair 2 horas da hora atual
nova_hora = agora - timedelta(hours=2)
print("Hora após 2 horas:", nova_hora)