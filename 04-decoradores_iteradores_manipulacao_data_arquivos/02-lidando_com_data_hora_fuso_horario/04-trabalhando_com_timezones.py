"""
Quando trabalhamos com data e hora, lidar com fusos horários é uma 
necessidade comum. Python facilita isso através do módulo "pytz".

O Python também permite fazer isso com o módulo datetime padrão, embora
seja um pouco mais complexo do que usando bibliotecas como "pytz".
"""

# =========================================================================
print("============ Exemplo de fuso horário com módulo pytz ============")

import datetime
import pytz


data = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
data_2 = datetime.datetime.now(pytz.timezone("Europe/Oslo"))

print(f"Data America/Sao_Paulo: {data}")
print(f"Data Europe/Oslo: {data_2}")


# =========================================================================
print("\n============ Exemplo de fuso horário com datetime ============")

# Criando datetime com timezone
data = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3), "BRT"))
print(data)

# Convertendo para outro timezone
data_utc = data.astimezone(datetime.timezone.utc)
print(data_utc)
