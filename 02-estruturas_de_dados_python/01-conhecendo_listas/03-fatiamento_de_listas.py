"""
Fatiamento de listas

Além de acessar elementos diretamente, podemos extrair um
conjunto de valores de uma sequência. Para isso basta passar
o índice inicial e/ou final para acessar o conjunto. Podemos
ainda informar quantas posições o cursor deve "pular" no acesso.
"""


# =========================================================================
print("============ Exemplo de fatiamento de lista ============")

print('lista = ["p", "y", "t", "h", "o", "n"]')

lista = ["p", "y", "t", "h", "o", "n"]

print(f"\nDados da Lista no índice[2:]: {lista[2:]}")
print(f"Dados da Lista no índice[:2]: {lista[:2]}")
print(f"Dados da Lista no índice[1:3]: {lista[1:3]}")
print(f"Dados da Lista no índice[0:3:2]: {lista[0:3:2]}")
print(f"Dados da Lista no índice[::]: {lista[::]}")
print(f"Dados da Lista no índice[::-1]: {lista[::-1]}")
