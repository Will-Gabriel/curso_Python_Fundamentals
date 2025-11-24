"""
Conhecendo o Fatiamento de Strings

Fatiamento de strings é uma técnica utilizada para retornar strings (partes da string original),
informando início (start), fim (stop) e passo (step): [start: stop[, step]]
"""

nome = "Wilian Gabriel da Silva"

# =========================================================================
print("\n============ Exemplos de Fatiamento ============")

print(f"Primeiro nome: {nome[0:7]}")

print(f"Segundo nome: {nome[7:15]}")

print(f"Sobrenome: {nome[15:]}")

print(f"Nome pulando de 2 em 2: {nome[::2]}")

print(f"Nome ao contrario: {nome[::-1]}")
