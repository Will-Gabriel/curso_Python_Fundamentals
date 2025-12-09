"""
Conversão e formatação de datas e horas

Python também permite converter e formatar datas e horas.
Para isos, usamos os métodos "strftime" (string format time) e 
"strptime" (string parse time).
"""

# =========================================================================
print("============ Exemplo - Formatando data e hora com strftime ============")

import datetime

data = datetime.datetime.now()
print(f"Antes da formatação: {data}")

# Formatando data e hora
print(f"Depois da formatação: {data.strftime("%d/%m/%Y %H:%M")}")


# =========================================================================
print("\n============ Exemplo - Formatando data e hora strptime ============")

# Convertendo string para datime
data_string = "07/07/1999 20:30"
print(f"Antes da formatação: {data_string}")

data = datetime.datetime.strptime(data_string, "%d/%m/%Y %H:%M")
print(f"Depois da formatação: {data}")
