from datetime import datetime, timedelta, date, time

data1 = datetime(2023, 10, 1)
data2 = datetime(2023, 11, 1)

if data1 < data2:
    print("Data1 é anterior a Data2")
else:
    print("Data1 é posterior ou igual a Data2")