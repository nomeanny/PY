import calendar

ano = 2024
if calendar.isleap(ano):
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')