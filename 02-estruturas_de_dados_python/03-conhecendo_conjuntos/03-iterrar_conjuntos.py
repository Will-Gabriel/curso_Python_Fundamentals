"""
Iterar conjuntos

A forma maios comum para percorrer os dados de um conjunto é utilizando o for.

Função enumarate: 
- Às vezes é necessário saber qual o índice do objeto dentro do laço for.
Para isso podemos usar a função enumerate.
"""


# =========================================================================
print("============ Iterar os Conjuntos ============")

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(f"Carro: {carro}")



# =========================================================================
print("\n============ Iterar os Conjuntos com enumerate ============")

carros = {"gol", "celta", "palio"}

for i, carro in enumerate(carros):
    print(f"Carro na posição {i}: {carro}")
