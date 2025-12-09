"""
Timedelta
Podemos criar e manipoular objetos date, time e datetime de várias maneiras.
Por exemplo, podemos adicionar e subtrair datas, verificar a diferença entre
datas e muito mais.
"""

# =========================================================================
print("============ Exemplo ============")

import datetime

data = datetime.datetime(2025, 7, 7, 19, 47)
print(f"Ano, mês, dia e horas: {data}")

# =========================================================================
print("\n============ Exemplo acrescendo uma semana com timedelta ============")

data = data + datetime.timedelta(weeks=1)
print(f"Ano, mês, dia e horas: {data}")

# =========================================================================
print("\n============ Exemplo com timedelta ============")

from datetime import datetime, timedelta

print(datetime.now().date())

tipo_carro = "P" # "M" "G"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    # data_estimada = data_atual + timedelta(days=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    # data_estimada = data_atual + timedelta(days=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "G":
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    # data_estimada = data_atual + timedelta(days=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    print("Tipo do carro inválido!")
