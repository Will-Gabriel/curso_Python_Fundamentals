"""
O que é o módulo datetime?
O módulo "datetime" em Python é usado para lidar cm datasa e horas.
Eles possui várias vlasses úteis cmo date, time e timedelta.
"""

# =========================================================================
print("============ Exemplo datetime ============")

from datetime import date, datetime, time

data = date(2025, 7, 7)
print(f"Ano, mês e dia: {data}")

# =========================================================================
print("\n============ Exemplo date.today() ============")

print(f"Ano, mês e dia: {date.today()}")

# =========================================================================
print("\n============ Exemplo datetime com horas, minutos e segundos ============")

data_hora = datetime(2025, 7, 7, 19, 30)
print(data_hora)
print(datetime.today())

# =========================================================================
print("\n============ Exemplo time ============")

hora = time(10, 20, 0)
print(f"Hora, minutos e segundos: {hora}")
