"""
Fatiamento de Tuplas

Além de acessar elementos diretamente, podemos extrair um conjunto de valores de
uma sequência. Para isso basta passar o índice inicial e/ou final para acessar o
conjunto. Podemos ainda informar quantas posições o cursor deve "pular" no acesso.

Sempre adicionar uma vírgula a mais ao final para evitar que o Python se perca.
Ex: frutas = ("laranja", "pera", "uva",)
"""


# =========================================================================
print("============ Fatiamento de uma Tupla ============")

tupla = ("p", "y", "t", "h", "o", "n",)

print(f"Dados da Tupla: {tupla}\n")

print(f"Índice[2:] da tupla: {tupla[2:]}")
print(f"Índice[:2] da tupla: {tupla[:2]}")
print(f"Índice[1:3] da tupla: {tupla[1:3]}")
print(f"Índice[0:3:2] da tupla: {tupla[0:3:2]}")
print(f"Índice[::] da tupla: {tupla[::]}")
print(f"Índice[::-1] da tupla: {tupla[::-1]}")
