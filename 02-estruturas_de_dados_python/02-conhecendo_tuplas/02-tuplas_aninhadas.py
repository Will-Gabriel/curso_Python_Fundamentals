"""
Tuplas aninhadas

Tuplas podem armazenar todos os tipos de objetos Python, portanto podemos
ter tuplas que armazenam outras tuplas. Com isso podemos criar estruturas
bidimensionais (tabelas), e acessar informando os índices de linha e coluna.

Sempre adicionar uma vírgula a mais ao final para evitar que o Python se perca.
Ex: frutas = ("laranja", "pera", "uva",)
"""


# =========================================================================
print("============ Criando uma Tupla aninhada ============")

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (5, 6, "c"),
)

print(f"Matriz: {matriz}\n")

print(f"Índice[0] da matriz: {matriz[0]}")
print(f"Índice[0][0] da matriz: {matriz[0][0]}")
print(f"Índice[0][-1] da matriz: {matriz[0][-1]}")
print(f"Índice[-1][-1] da matriz: {matriz[-1][-1]}")
