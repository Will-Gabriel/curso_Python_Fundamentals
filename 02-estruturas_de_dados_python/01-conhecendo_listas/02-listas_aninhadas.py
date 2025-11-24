"""
Listas aninhadas

Listas podem armazenar todos os tipos de objetos Python, portanto podemos
ter listas que armazenam outras listas. Com isso podemos criar estruturas
bidimensionais (tabelas), e acessar informando os índices de linha e coluna.
"""

# =========================================================================
print("============ Criando uma matriz com lista ============")

print("""
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]
""")

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(f"Dados da matriz: {matriz}\n")

print(f"Dados da matriz no índice[0]: {matriz[0]}")
print(f"Dados da matriz no índice[0][0]: {matriz[0][0]}")
print(f"Dados da matriz no índice[0][-1]: {matriz[0][-1]}")
print(f"Dados da matriz no índice[-1][-1]: {matriz[-1][-1]}")
