"""
Iterar sobre a lista

A forma mais comum para percorrer os dados de uma lista
é utilizando o comando for
"""


# =========================================================================
print("============ Exemplo de iteração ============")

carros = ["gol", "celta", "palio"]

print(f"Lista carros: {carros}")

for carro in carros:
    print(f"Carro: {carro}")


# =========================================================================
print("\n============ Exemplo de iteração com enumerate ============")

carros = ["gol", "celta", "palio"]

print(f"Lista carros: {carros}")

for indice, carro in enumerate(carros):
    print(f"Carro {indice}: {carro}")
