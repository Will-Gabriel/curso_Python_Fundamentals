"""
Acessando os dados

Conjuntos em Python nao suportam indexação e nem fatiamento, caso queira 
acessar os seus valores é necessário converter o conjunto para lista.
"""


# =========================================================================
print("============ Acessando dados de Sets ============")

numeros = {1, 2, 3, 2}

# Descomente para ver o erro
# print(f"Índice[0] do set: {numeros[0]}")

numeros = list(numeros)

print(f"Índice[0] do set: {numeros[0]}")
